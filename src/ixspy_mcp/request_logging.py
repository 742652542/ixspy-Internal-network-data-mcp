from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

from fastmcp.server.dependencies import get_http_request

from .logging import safe_append_log_record


def _now() -> datetime:
    return datetime.now().astimezone()


def _get_client_ip() -> str:
    try:
        request = get_http_request()
    except RuntimeError:
        return "unknown"
    client = request.client
    if client and client.host:
        return client.host
    return "unknown"


def _serialize_payload(payload: Any) -> Any:
    if payload is None:
        return {}
    model_dump = getattr(payload, "model_dump", None)
    if callable(model_dump):
        return payload.model_dump(exclude_none=True)
    if isinstance(payload, dict):
        return payload
    return payload


def log_request(
    *,
    tool: str,
    payload: Any,
    now: datetime | None = None,
    base_dir: Path | None = None,
) -> None:
    record = {
        "ts": (now or _now()).isoformat(),
        "event": "request",
        "tool": tool,
        "ip": _get_client_ip(),
        "payload": _serialize_payload(payload),
    }
    safe_append_log_record(record, now=now, base_dir=base_dir)


def log_error(
    *,
    tool: str,
    payload: Any,
    error: Exception,
    now: datetime | None = None,
    base_dir: Path | None = None,
) -> None:
    record = {
        "ts": (now or _now()).isoformat(),
        "event": "error",
        "tool": tool,
        "ip": _get_client_ip(),
        "payload": _serialize_payload(payload),
        "error": f"{type(error).__name__}: {error}",
    }
    safe_append_log_record(record, now=now, base_dir=base_dir)
