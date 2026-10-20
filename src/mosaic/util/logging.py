"""Tiny structured-logging helper.

The orchestration loop runs unattended for days; logs are how we debug
post-hoc. Use one logger name per module and stick to ``extra={...}``
for structured fields.
"""

from __future__ import annotations

import logging
import sys


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    handler = logging.StreamHandler(sys.stderr)
    fmt = logging.Formatter(
        "%(asctime)s %(levelname)-7s %(name)s :: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger
