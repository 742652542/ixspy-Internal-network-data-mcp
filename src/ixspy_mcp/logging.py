from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def get_log_dir(base_dir: Path | None = None) -> Path:
    root = base_dir or _repo_root()
    return root / "logs"


def get_daily_log_path(
    *, now: datetime | None = None, base_dir: Path | None = None
) -> Path:
    current = now or datetime.now().astimezone()
    date_str = current.strftime("%Y-%m-%d")
    return get_log_dir(base_dir) / f"ixspy-mcp-{date_str}.jsonl"


def append_log_record(
    record: dict[str, Any], *, now: datetime | None = None, base_dir: Path | None = None
) -> None:
    log_path = get_daily_log_path(now=now, base_dir=base_dir)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def safe_append_log_record(
    record: dict[str, Any], *, now: datetime | None = None, base_dir: Path | None = None
) -> None:
    try:
        append_log_record(record, now=now, base_dir=base_dir)
    except Exception as exc:  # noqa: BLE001 - never fail requests on logging errors
        print(f"log write failed: {exc}", file=sys.stderr)
