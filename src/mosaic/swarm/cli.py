"""``python -m mosaic.swarm`` (agents call it as ``swarm`` via ``swarm/bin/swarm``).

Agent commands read ``SWARM_CONFIG`` / ``SWARM_AGENT`` from the environment
the launcher sets. Operator commands take ``--config``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import click

from mosaic.swarm import agent as A
from mosaic.swarm.config import load_swarm


def _body(body_file: str | None) -> str:
    if body_file:
        return Path(body_file).read_text()
    if sys.stdin.isatty():
        raise click.UsageError("pass the body on stdin or with --body-file")
    return sys.stdin.read()


@click.group()
def main() -> None:
    """Leaderless agent swarm for the gLL gap search."""


# ---------------------------------------------------------------- agent side


@main.command()
@click.option("--no-mark", is_flag=True, help="do not mark posts and mail as read")
def digest(no_mark: bool) -> None:
    """What changed since you last looked."""
    click.echo(A.digest(A.Ctx.from_env(), mark=not no_mark))


@main.command()
@click.option("--parent", default=None)
@click.option("--out", "out_path", default=None, type=click.Path(dir_okay=False))
def template(parent, out_path) -> None:
    """A parent's input to start from: add form_factor.deformation, then submit."""
    text = json.dumps(A.template(A.Ctx.from_env(), parent), indent=1)
    if out_path:
        Path(out_path).write_text(text + "\n")
    else:
        click.echo(text)


@main.command()
def reference() -> None:
    """Parents, their gaps, the gates and the stage ladder."""
    click.echo(A.reference_report(A.Ctx.from_env()), nl=False)


@main.command()
@click.argument("req_id")
def show(req_id: str) -> None:
    """Any visible request: its request.json, input path, and result."""
    click.echo(json.dumps(A.show(A.Ctx.from_env(), req_id), indent=1))


@main.command()
@click.argument("ed_input", type=click.Path(exists=True, dir_okay=False))
@click.option("--parent", default=None)
@click.option("--control", is_flag=True, help="a control (static density not pinned, never ranked)")
def check(ed_input: str, parent, control) -> None:
    """Validate an input exactly as the broker will (pinning, admissibility)."""
    from mosaic.swarm.validate import RequestRejected

    try:
        report = A.check(A.Ctx.from_env(), Path(ed_input), parent, control=control)
    except RequestRejected as exc:
        raise click.ClickException(f"rejected: {exc}")
    click.echo("ok")
    if report.get("boundary"):
        click.echo("search boundary: " + ", ".join(f"{k} {v:.4g}" for k, v in report["boundary"].items()))


@main.command()
@click.argument("ed_input", type=click.Path(exists=True, dir_okay=False))
@click.option("--family", required=True, help="short id of the family this request belongs to")
@click.option("--parent", default=None, help="static parent it is scored against")
@click.option("--note", default="")
@click.option("--builds-on", "builds_on", multiple=True, help="request id(s) this one builds on")
@click.option("--control", is_flag=True, help="a control (static density not pinned, never ranked)")
@click.option("--clusters", default="", help="control only: comma-separated clusters to run on (default: the first stage)")
@click.option("--diagnostic", is_flag=True, help="a probe: first stage only, never promoted or ranked")
def submit(ed_input: str, family: str, parent, note: str, builds_on: tuple[str, ...], control: bool, clusters: str,
           diagnostic: bool) -> None:
    """Queue one request (first stage of the ladder; promotion is automatic)."""
    from mosaic.swarm.validate import RequestRejected

    try:
        rid = A.submit(A.Ctx.from_env(), Path(ed_input), family, parent=parent, note=note,
                       parents=list(builds_on), control=control,
                       clusters=[c for c in clusters.split(",") if c], diagnostic=diagnostic)
    except RequestRejected as exc:
        raise click.ClickException(f"rejected before submission: {exc}")
    click.echo(rid)


@main.command()
@click.argument("req_ids", nargs=-1, required=True)
@click.option("--reason", default="")
def withdraw(req_ids: tuple[str, ...], reason: str) -> None:
    """Withdraw your own requests (no further promotion; queued runs to the back)."""
    for rid in A.withdraw(A.Ctx.from_env(), list(req_ids), reason):
        click.echo(f"withdrawn {rid}")


@main.command("submit-batch")
@click.argument("directory", type=click.Path(exists=True, file_okay=False))
@click.option("--family", required=True)
@click.option("--parent", default=None)
@click.option("--note", default="")
@click.option("--diagnostic", is_flag=True, help="probes: first stage only, never promoted or ranked")
def submit_batch(directory: str, family: str, parent, note: str, diagnostic: bool) -> None:
    """Submit every *.json in DIRECTORY (one line per file: id or rejection)."""
    for name, rid in A.submit_batch(A.Ctx.from_env(), Path(directory), family, parent=parent, note=note,
                                    diagnostic=diagnostic):
        click.echo(f"{name}\t{rid}")


@main.command()
@click.argument("req_id", required=False)
def status(req_id: str | None) -> None:
    """Your requests and their results (one request in full with REQ_ID)."""
    reqs = A.requests(A.Ctx.from_env())
    if req_id:
        match = [r for r in reqs if r["req_id"] == req_id]
        if not match:
            raise click.ClickException(f"no request {req_id}")
        click.echo(json.dumps(match[0], indent=1))
        return
    for r in reqs:
        res = r["result"] or {}
        line = A._clusters_line(res) if res.get("clusters") else (res.get("reason") or "")
        click.echo(f"{r['req_id']}  [{r['family']}]  {r['status']}  {line}")


@main.command()
@click.option("--kind", required=True, type=click.Choice(A.KINDS))
@click.option("--family", required=True)
@click.option("--title", required=True)
@click.option("--hash", "hashes", multiple=True)
@click.option("--ref", "refs", multiple=True, help="ids of posts or requests this refers to")
@click.option("--to", default=None, help="addressee for a `request` (e.g. human)")
@click.option("--body-file", default=None)
def post(kind, family, title, hashes, refs, to, body_file) -> None:
    """Add an immutable post to the board (body on stdin)."""
    click.echo(A.post(A.Ctx.from_env(), kind, family, title, _body(body_file), hashes=list(hashes),
                      refs=list(refs), to=to))


@main.command()
@click.option("--to", "to", required=True)
@click.option("--subject", required=True)
@click.option("--ref", "refs", multiple=True)
@click.option("--body-file", default=None)
def mail(to, subject, refs, body_file) -> None:
    """Directed message to one agent (body on stdin)."""
    click.echo(A.mail(A.Ctx.from_env(), to, subject, _body(body_file), refs=list(refs)))


@main.command()
@click.argument("item_id")
def read(item_id: str) -> None:
    """Full text of a post or mail."""
    click.echo(A.read_item(A.Ctx.from_env(), item_id))


@main.command()
@click.option("--family", default=None)
@click.option("--state", default=None, type=click.Choice(["active", "waiting"]))
@click.option("--note", default=None)
def heartbeat(family, state, note) -> None:
    """Update your roster entry."""
    s = A.heartbeat(A.Ctx.from_env(), current_family=family, state=state, note=note)
    click.echo(json.dumps(s, indent=1))


@main.command()
def leaderboard() -> None:
    """The leaderboard visible to you."""
    ctx = A.Ctx.from_env()
    p = (ctx.L.agent_dir(ctx.agent) if ctx.L.private else ctx.L.root) / "leaderboard.md"
    click.echo(p.read_text() if p.exists() else "(no leaderboard yet)")


@main.command()
@click.option("--body-file", default=None)
def done(body_file) -> None:
    """Post your final summary and stop (your loop should end after this)."""
    click.echo(A.done(A.Ctx.from_env(), _body(body_file)))


# ---------------------------------------------------------------- operator side


@main.command()
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("--arm", required=True)
@click.option("--title", required=True)
@click.option("--to", default=None, help="agent to address (required in a private arm)")
@click.option("--ref", "refs", multiple=True)
@click.option("--body-file", default=None)
def human(config_path, arm, title, to, refs, body_file) -> None:
    """Answer the agents as the human operator (body on stdin)."""
    click.echo(A.human_post(load_swarm(config_path), arm, title, _body(body_file), to=to, refs=list(refs)))


@main.command()
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("--once", is_flag=True, help="one tick per arm, then exit")
def broker(config_path: str, once: bool) -> None:
    """Run the ED broker (login node; sole Slurm submitter and store writer)."""
    from mosaic.swarm.broker import run

    sys.exit(run(config_path, once=once))


@main.command()
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("--no-worktrees", is_flag=True)
@click.option("--no-solver", is_flag=True)
def setup(config_path: str, no_worktrees: bool, no_solver: bool) -> None:
    """Prepare directories, worktrees, solver snapshot and job scripts. Launches nothing."""
    from mosaic.swarm.setup import setup as do_setup

    report = do_setup(load_swarm(config_path), Path(config_path), worktrees=not no_worktrees, solver=not no_solver)
    click.echo(json.dumps(report, indent=1))


@main.command("pes-cases")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, dir_okay=False))
def pes_cases(config_path: str) -> None:
    """Cases for scripts/pes_expected_counts.jl, one per PES cluster."""
    cfg = load_swarm(config_path)
    cases = []
    for name, c in cfg.clusters.items():
        if c.pes_na:
            extra = {"symcluster": c.symcluster} if c.symcluster is not None else {"nk1": c.nk1, "nk2": c.nk2}
            cases.append({"name": f"{name}:{c.pes_na}", "n_k": c.sites, "extra": extra, "NA": c.pes_na})
    click.echo(json.dumps(cases, indent=1))


@main.command("agent-env")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("--agent", required=True)
def agent_env_cmd(config_path: str, agent: str) -> None:
    """Shell exports for scripts/swarm_agent.sh."""
    from mosaic.swarm.setup import agent_env

    click.echo(agent_env(load_swarm(config_path), agent, Path(config_path)), nl=False)


@main.command("sandbox-hide")
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, dir_okay=False))
def sandbox_hide_cmd(config_path: str) -> None:
    """What scripts/swarm_agent.sh empties in the agent's sandbox: the config's
    agent_deny_read paths that exist, one "d PATH" or "f PATH" per line."""
    cfg = load_swarm(config_path)
    for p in map(cfg.path, cfg.agent_deny_read):
        if p.exists():
            click.echo(f"{'d' if p.is_dir() else 'f'} {p}")


@main.command()
@click.option("--config", "config_path", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("--interval", default=600, show_default=True)
@click.option("--once", is_flag=True)
@click.option("--dry-run", is_flag=True, help="report only; never sbatch")
def supervise(config_path: str, interval: int, once: bool, dry_run: bool) -> None:
    """Resubmit agent allocations that ended while agents remain (login node)."""
    from mosaic.swarm.setup import supervise as loop, supervise_once

    if once or dry_run:
        click.echo(json.dumps(supervise_once(load_swarm(config_path), submit=not dry_run), indent=1))
    else:
        loop(config_path, interval=interval)
