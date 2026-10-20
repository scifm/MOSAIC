"""What an agent does with the shared files.

Board posts, mail, roster heartbeats, request submission and the digest.
Agents never open the store; everything they read is a file the broker or
another agent wrote atomically.
"""

from __future__ import annotations

import os
import shutil
import socket
import subprocess
from datetime import timedelta
from pathlib import Path
from typing import Optional

from mosaic.swarm.config import SwarmConfig, load_swarm
from mosaic.swarm.files import (
    atomic_write_json,
    new_id,
    parse_iso,
    read_json,
    read_markdown_with_front_matter,
    utc_iso,
    utc_now,
    visible_entries,
    write_markdown_with_front_matter,
)
from mosaic.swarm.layout import ArmLayout
from mosaic.swarm.validate import normalise, parse_agent_input

KINDS = ("hypothesis", "result", "claim", "refutation", "abandon", "request", "note")
STALE_AFTER = timedelta(minutes=30)


class Ctx:
    """The calling agent: config, arm layout, name. Built from the environment
    the launcher sets (``SWARM_CONFIG``, ``SWARM_AGENT``)."""

    def __init__(self, cfg: SwarmConfig, agent: str):
        self.cfg, self.agent = cfg, agent
        self.arm = cfg.arm_of(agent)
        self.L = ArmLayout(cfg, self.arm)

    @classmethod
    def from_env(cls) -> "Ctx":
        try:
            return cls(load_swarm(os.environ["SWARM_CONFIG"]), os.environ["SWARM_AGENT"])
        except KeyError as exc:
            raise SystemExit(f"{exc.args[0]} is not set; agents are launched with SWARM_CONFIG and SWARM_AGENT") from None


# ----------------------------------------------------------------------
# board and mail
# ----------------------------------------------------------------------


def post(ctx: Ctx, kind: str, family: str, title: str, body: str, *, hashes: list[str] = (),
         refs: list[str] = (), to: Optional[str] = None) -> str:
    if kind not in KINDS:
        raise SystemExit(f"kind must be one of {KINDS}")
    pid = new_id(ctx.agent, kind)
    meta = {"id": pid, "agent": ctx.agent, "kind": kind, "family": family, "title": title,
            "hashes": list(hashes), "refs": list(refs), "posted_at": utc_iso()}
    if to:
        meta["to"] = to
    write_markdown_with_front_matter(ctx.L.board_dir(ctx.agent) / f"{pid}.md", meta, body)
    return pid


def mail(ctx: Ctx, to: str, subject: str, body: str, *, refs: list[str] = ()) -> str:
    if ctx.L.private:
        raise SystemExit("mail is not available in a private arm")
    if to not in ctx.L.agents or to == ctx.agent:
        raise SystemExit(f"no such peer {to!r}; peers: {[a for a in ctx.L.agents if a != ctx.agent]}")
    mid = new_id(ctx.agent, "mail")
    meta = {"id": mid, "from": ctx.agent, "to": to, "subject": subject, "refs": list(refs), "sent_at": utc_iso()}
    write_markdown_with_front_matter(ctx.L.mail_dir(to) / f"{mid}.md", meta, body)
    return mid


def human_post(cfg: SwarmConfig, arm: str, title: str, body: str, *, to: Optional[str] = None,
               refs: list[str] = ()) -> str:
    """The operator's answer channel (agents escalate with ``request`` posts).

    Shared arm: a board post by ``human``, plus mail to ``to`` if given.
    Private arm: a post on ``to``'s own board (``to`` required)."""

    L = ArmLayout(cfg, arm)
    if to is not None and to not in L.agents:
        raise SystemExit(f"{to!r} is not an agent of arm {arm!r}")
    if L.private and to is None:
        raise SystemExit("a private arm has no shared board; name the agent with --to")
    pid = new_id("human", "note")
    meta = {"id": pid, "agent": "human", "kind": "note", "family": "-", "title": title,
            "hashes": [], "refs": list(refs), "posted_at": utc_iso()}
    if to:
        meta["to"] = to
    write_markdown_with_front_matter(L.board_dir(to) / f"{pid}.md", meta, body)
    if to and not L.private:
        mid = new_id("human", "mail")
        write_markdown_with_front_matter(L.mail_dir(to) / f"{mid}.md", {
            "id": mid, "from": "human", "to": to, "subject": title, "refs": list(refs) + [pid],
            "sent_at": utc_iso()}, body)
    return pid


def read_item(ctx: Ctx, item_id: str) -> str:
    for d in ctx.L.board_dirs_visible_to(ctx.agent) + ([] if ctx.L.private else [ctx.L.mail_dir(ctx.agent)]):
        p = d / f"{item_id}.md"
        if p.exists():
            return p.read_text()
    raise SystemExit(f"no post or mail {item_id!r} visible to {ctx.agent}")


# ----------------------------------------------------------------------
# roster
# ----------------------------------------------------------------------


def heartbeat(ctx: Ctx, **fields) -> dict:
    path = ctx.L.agent_dir(ctx.agent) / "status.json"
    status = read_json(path, {}) or {}
    session = read_json(ctx.L.agent_dir(ctx.agent) / "session.json", {}) or {}
    status.update({k: v for k, v in fields.items() if v is not None})
    status.update(name=ctx.agent, host=socket.gethostname(), slurm_job=os.environ.get("SLURM_JOB_ID"),
                  session_uuid=session.get("uuid"), last_heartbeat=utc_iso())
    status.setdefault("state", "active")
    atomic_write_json(path, status)
    return status


def roster(ctx: Ctx) -> list[dict]:
    names = [ctx.agent] if ctx.L.private else ctx.L.agents
    out = []
    for a in names:
        s = read_json(ctx.L.agent_dir(a) / "status.json") or {"name": a, "state": "not started"}
        if s.get("last_heartbeat") and utc_now() - parse_iso(s["last_heartbeat"]) > STALE_AFTER and s.get("state") != "done":
            s = {**s, "state": f"{s.get('state')} (stale)"}
        if (ctx.L.agent_dir(a) / "done").exists():
            s = {**s, "state": "done"}
        out.append(s)
    return out


# ----------------------------------------------------------------------
# requests
# ----------------------------------------------------------------------


def _git_sha() -> Optional[str]:
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
        return sha + ("+dirty" if dirty else "")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _parent(ctx: Ctx, parent: Optional[str]) -> str:
    names = ctx.cfg.request_parents
    if parent is None:
        if len(names) == 1:
            return names[0]
        raise SystemExit(f"name a parent with --parent: one of {names}")
    if parent not in names:
        raise SystemExit(f"unknown parent {parent!r}; one of {names}")
    return parent


def template(ctx: Ctx, parent: Optional[str] = None) -> dict:
    """The named parent's input, to start a request from: add a
    ``form_factor.deformation`` block and submit."""

    from mosaic.swarm.parents import build_parents

    name = _parent(ctx, parent)
    ed = build_parents(ctx.cfg)[name]
    return ed.model_dump(mode="json", exclude={"config_hash", "campaign_id", "seed", "proposer_x"})


def check(ctx: Ctx, ed_input_path: Path, parent: Optional[str] = None, *, control: bool = False) -> dict:
    """Run the broker's validation locally (the broker re-runs it); returns its
    measurements (admissibility, search boundary)."""

    import json

    from mosaic.swarm.parents import build_parents

    cfg = ctx.cfg
    if control:
        cfg = cfg.model_copy(update={"regime": cfg.regime.model_copy(update={"pin_static": False})})
    report: dict = {}
    normalise(json.loads(Path(ed_input_path).read_text()), build_parents(ctx.cfg)[_parent(ctx, parent)], cfg, report)
    return report


def submit(ctx: Ctx, ed_input_path: Path, family: str, *, parent: Optional[str] = None, note: str = "",
           parents: list[str] = (), control: bool = False, clusters: list[str] = (),
           diagnostic: bool = False) -> str:
    """Queue one request. ``parents`` are request ids this one builds on;
    ``parent`` is the static parent it is scored against."""

    import json

    if clusters and not control:
        raise SystemExit("--clusters is for --control requests only; search requests climb the ladder")
    if control and diagnostic:
        raise SystemExit("a request is either --control or --diagnostic")
    unknown = [c for c in clusters if c not in ctx.cfg.all_clusters]
    if unknown:
        raise SystemExit(f"unknown clusters {unknown}; one of {ctx.cfg.all_clusters}")
    raw = json.loads(Path(ed_input_path).read_text())
    parse_agent_input(raw)
    name = _parent(ctx, parent)
    check(ctx, ed_input_path, name, control=control)
    rid = new_id(ctx.agent, "req")
    inbox = ctx.L.inbox(ctx.agent)
    tmp = inbox / f".tmp-{rid}"
    tmp.mkdir(parents=True)
    shutil.copyfile(ed_input_path, tmp / "ed_input.json")
    atomic_write_json(tmp / "request.json", {
        "agent": ctx.agent, "family": family, "note": note, "parent": name,
        "kind": "control" if control else ("diagnostic" if diagnostic else "search"), "builds_on": list(parents),
        **({"clusters": list(clusters)} if clusters else {}),
        "submitted_at": utc_iso(), "git_sha": _git_sha(), "cwd": str(Path.cwd()),
        "source": str(Path(ed_input_path).resolve())})
    os.rename(tmp, inbox / rid)  # the broker only ever sees complete request directories
    return rid


def withdraw(ctx: Ctx, req_ids: list[str], reason: str = "") -> list[str]:
    """Withdraw your own requests: no further promotion, and their queued runs
    go to the back unless another active request shares them. Results already
    measured stay recorded."""

    done = []
    for rid in req_ids:
        d = ctx.L.inbox(ctx.agent) / rid
        if not d.is_dir():
            raise SystemExit(f"no request {rid!r} of yours")
        atomic_write_json(d / "withdrawn.json", {"at": utc_iso(), "reason": reason})
        done.append(rid)
    return done


def submit_batch(ctx: Ctx, directory: Path, family: str, *, parent: Optional[str] = None,
                 note: str = "", diagnostic: bool = False) -> list[tuple[str, str]]:
    """Submit every ``*.json`` in ``directory`` (sorted). Returns (file, request
    id or "rejected: reason") pairs; one bad input does not stop the rest."""

    from mosaic.swarm.validate import RequestRejected

    out = []
    for f in sorted(Path(directory).glob("*.json")):
        try:
            out.append((f.name, submit(ctx, f, family, parent=parent, note=note, diagnostic=diagnostic)))
        except (RequestRejected, SystemExit) as exc:
            out.append((f.name, f"rejected: {exc}"))
    return out


def requests(ctx: Ctx) -> list[dict]:
    out = []
    for d in visible_entries(ctx.L.inbox(ctx.agent)):
        req = read_json(d / "request.json") or {}
        res = read_json(d / "result.json")
        acc = read_json(d / "accepted.json")
        out.append({"req_id": d.name, "family": req.get("family"), "note": req.get("note"),
                    "status": (res or {}).get("status", "queued (waiting for a slot)" if acc is None else "?"),
                    "result": res, "accepted": acc})
    return out


def show(ctx: Ctx, req_id: str) -> dict:
    """Any request visible to this agent: every agent's in a shared arm (so
    nobody has to mail for another agent's input), only one's own in a
    private arm."""

    owners = [ctx.agent] if ctx.L.private else ctx.L.agents
    for a in owners:
        d = ctx.L.inbox(a) / req_id
        if d.is_dir():
            return {"req_id": req_id, "agent": a, "request": read_json(d / "request.json"),
                    "ed_input": str(d / "ed_input.json"), "accepted": read_json(d / "accepted.json"),
                    "result": read_json(d / "result.json")}
    raise SystemExit(f"no request {req_id!r} visible to {ctx.agent}")


def reference_report(ctx: Ctx) -> str:
    """Parents, clusters, gates and the stage ladder, with the parents' gaps."""

    cfg = ctx.cfg
    table = read_json(ctx.L.root / "parents.json") or {}
    lines = ["Parents (request one with --parent; `swarm template --parent NAME` prints its input):"]
    for name, spec in cfg.parents.items():
        if spec.role != "parent":
            continue
        t = table.get(name, {})
        src = f"shell weights {spec.shells}" if spec.shells else spec.ed_input
        lines.append(f"- {name}: {src}, M2 = {t.get('M2', float('nan')):.5f}")
        for c, e in (t.get("clusters") or {}).items():
            g = f"Δ {e['gap']:.6e}" if e.get("gap") else e.get("state")
            lines.append(f"    {c}: {g}, C = {e.get('chern')}, gate {e.get('verdict', '…')}")
    lines += ["", "Pinned (broker-enforced): " + ("the static density W_G and a_n of the parent; only "
              "form_factor.deformation is yours" if cfg.regime.pin_static else "interaction and normalization extras"),
              "Integer G labels are in the solver's 120° basis (ADR-0035): G = m G1 + n G2, |G|² ∝ m² + n² − mn.",
              "Broker-owned extras (replaced if you set them): nk1, nk2, symcluster, ed_accuracy, pes.", ""]
    if cfg.gates.admissibility_min_ratio is not None:
        lines.append(f"Admissibility: S00(k) > 0 and min/max ≥ {cfg.gates.admissibility_min_ratio:g} on a "
                     f"{cfg.gates.admissibility_grid}² grid plus every rectangular mesh (`swarm check` runs it).")
    lines += [f"Gates: splitting/Δ < {cfg.gates.split_max}; PES PASS if the expected counts separate with "
              f"entanglement gap ≥ {cfg.gates.pes_gap_pass}, AMBIGUOUS if they separate with a smaller gap, FAIL "
              "otherwise.", "", "Stage ladder (promotion by threshold on your own results, never by rank):"]
    for i, st in enumerate(cfg.stages):
        rule = "" if i == 0 else f" (enter if all verdicts in {st.promote_verdicts} and min R_gap ≥ {st.promote_min_R_gap})"
        lines.append(f"{i}. {st.name}{rule}:")
        for name in st.clusters:
            c = cfg.clusters[name]
            shape = f"symmetric {c.sites}-site" if c.symcluster is not None else f"{c.nk1}×{c.nk2} (k = i/{c.nk1} b1 + j/{c.nk2} b2)"
            extras = f", overrides {c.extra_overrides} {c.deformation_overrides}" if (c.extra_overrides or c.deformation_overrides) else ""
            lines.append(f"   - {name}: {shape}, accuracy {c.ed_accuracy or 'default'}, Chern {c.chern}, "
                         f"PES N_A = {c.pes_na}{extras}")
    if cfg.claims:
        lines += ["", "Claims (strongest first):"]
        for cl in cfg.claims:
            lines.append(f"- {cl.name}: PASS and R_gap > 1 on {cl.all_clusters}"
                         + (f", R_gap ≥ {cl.min_R_gap}" if cl.min_R_gap else ""))
    return "\n".join(lines) + "\n"


def done(ctx: Ctx, summary: str) -> str:
    pid = post(ctx, "note", "-", "final summary", summary)
    heartbeat(ctx, state="done")
    (ctx.L.agent_dir(ctx.agent) / "done").write_text(utc_iso() + "\n")
    return pid


# ----------------------------------------------------------------------
# digest
# ----------------------------------------------------------------------


def _clusters_line(res: dict) -> str:
    parts = []
    for name, c in (res.get("clusters") or {}).items():
        if c.get("verdict") is None:
            parts.append(f"{name} …")
        else:
            rg = c.get("R_gap")
            parts.append(f"{name} {'' if rg is None else f'{rg:.4f} '}{c['verdict']}"
                         + (f" ({'; '.join(c.get('reasons') or [])})" if c["verdict"] != "PASS" else ""))
    out = "R_gap: " + ", ".join(parts)
    if res.get("R_gap_min") is not None:
        out += f"; min {res['R_gap_min']:.4f}, stage {res.get('stage_reached')}"
    return out


def _pct(x) -> str:
    return "—" if x is None else f"{100 * x:+.2f}%"


def _first_line(text: str, n: int = 140) -> str:
    for line in text.strip().splitlines():
        if line.strip():
            return line.strip()[:n]
    return ""


def digest(ctx: Ctx, *, mark: bool = True, max_posts: int = 40) -> str:
    L, cfg = ctx.L, ctx.cfg
    heartbeat(ctx)
    cur_path = L.agent_dir(ctx.agent) / "cursor.json"
    cur = read_json(cur_path, {}) or {}
    seen_posts, seen_mail = set(cur.get("seen_posts", [])), set(cur.get("seen_mail", []))
    lines = [f"# Digest for {ctx.agent} (arm {ctx.arm}, {'private' if L.private else 'shared'}) — {utc_iso()}", ""]

    halt = cfg.root_path / "HALT"
    b = read_json(L.root / "broker.json")
    if halt.exists():
        lines.append(f"**BROKER HALTED:** {halt.read_text().strip()} — do not submit; post a `request` to the human.")
    elif b is None:
        lines.append("Broker: not started yet.")
    else:
        age = (utc_now() - parse_iso(b["last_tick"])).total_seconds()
        lines.append(f"Broker: last tick {age:.0f} s ago" + (" — **looks dead**" if age > 10 * cfg.broker.tick_seconds else ""))
    table = read_json(L.root / "parents.json") or {}
    for name, t in table.items():
        if t.get("role") == "parent":
            gaps = ", ".join(f"{c} {e['gap']:.4e}" if e.get("gap") else f"{c} pending"
                             for c, e in (t.get("clusters") or {}).items())
            lines.append(f"Parent {name} Δ: {gaps or 'pending'}")

    reqs = requests(ctx)
    lb_path = (L.agent_dir(ctx.agent) if L.private else L.root) / "leaderboard.json"
    lb = read_json(lb_path) or {}
    charged = ((lb.get("budget") or {}).get(ctx.agent) or {}).get("charged")
    in_flight = sum(1 for r in reqs if r["result"] and not r["result"].get("first_stage_done", True)
                    and r["status"] == "pending")
    lines.append(f"Budget: {charged if charged is not None else '?'}/{cfg.quotas.evaluations_per_agent} evaluations charged; "
                 f"{in_flight}/{cfg.quotas.max_in_flight_per_agent} in flight"
                 + (f"; deadline {cfg.deadline_utc}" if cfg.deadline_utc else ""))
    lines.append("")

    if not L.private:
        lines.append("## Roster")
        for s in roster(ctx):
            seen = s.get("last_heartbeat", "never")
            lines.append(f"- {s['name']}: {s.get('state')}, family={s.get('current_family', '—')}, "
                         f"last seen {seen}" + (f" — {s['note']}" if s.get("note") else ""))
        lines.append("")

    new_posts = []
    for d in L.board_dirs_visible_to(ctx.agent):
        for p in visible_entries(d, ".md"):
            if p.stem not in seen_posts:
                new_posts.append(p)
    new_posts.sort(key=lambda p: p.name)
    # Oldest first, and only what is shown is marked read, so a backlog is
    # worked through over several digests instead of being skipped.
    shown = new_posts[:max_posts]
    lines.append(f"## New board posts ({len(new_posts)})"
                 + (f", showing the oldest {max_posts}; run digest again for the rest" if len(new_posts) > max_posts else ""))
    for p in shown:
        meta, body = read_markdown_with_front_matter(p)
        h = f" hashes={[x[:12] for x in meta.get('hashes', [])]}" if meta.get("hashes") else ""
        r = f" refs={meta['refs']}" if meta.get("refs") else ""
        lines.append(f"- `{meta['id']}` **{meta['agent']}** {meta['kind']} [{meta['family']}] {meta['title']} — "
                     f"{_first_line(body)}{h}{r}")
    lines.append("")

    new_mail = []
    if not L.private:
        new_mail = [p for p in visible_entries(L.mail_dir(ctx.agent), ".md") if p.stem not in seen_mail]
        lines.append(f"## Unread mail ({len(new_mail)})")
        for p in new_mail:
            meta, body = read_markdown_with_front_matter(p)
            lines += [f"### from {meta['from']}: {meta['subject']} (`{meta['id']}`)", body.strip(), ""]
        lines.append("")

    lines.append("## Your requests")
    for r in reqs[-20:]:
        res = r["result"] or {}
        extra = ""
        if res.get("status") == "rejected":
            extra = f" — {res.get('reason')}"
        elif res.get("clusters"):
            extra = f" [{res.get('parent')}] " + _clusters_line(res)
            if res.get("claim"):
                extra += f" **{res['claim'].upper()}**"
        lines.append(f"- `{r['req_id']}` [{r['family']}] {r['status']}{extra}")
    lines.append("")

    boards = lb.get("leaderboards") or {}
    lines.append("## Leaderboards (top 5 per parent" + (", your requests only" if L.private else "") + ")")
    for parent, rows in boards.items():
        lines.append(f"### {parent}")
        for i, row in enumerate(rows[:5], 1):
            lines.append(f"{i}. {row['agent']} [{row['family']}] `{row['req_id']}` " + _clusters_line(row)
                         + (f" **{row['claim'].upper()}**" if row.get("claim") else ""))
        if not rows:
            lines.append("(empty)")
    other = lb.get("other_phases") or []
    if other:
        lines.append(f"Other phases (gate FAIL with R_gap > 1 somewhere): {len(other)} requests; see the leaderboard.")

    if mark:
        atomic_write_json(cur_path, {"seen_posts": sorted(seen_posts | {p.stem for p in shown}),
                                     "seen_mail": sorted(seen_mail | {p.stem for p in new_mail})})
    return "\n".join(lines) + "\n"
