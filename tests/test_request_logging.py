from datetime import datetime, timezone
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.request_logging import log_error, log_request


def test_log_request_writes_expected_fields(tmp_path: Path) -> None:
    now = datetime(2026, 4, 7, 12, 0, 0, tzinfo=timezone.utc)
    payload = {"page": 1}

    log_request(
        tool="ixspy.search_etsy_goods_all",
        payload=payload,
        now=now,
        base_dir=tmp_path,
    )

    log_path = tmp_path / "logs" / "ixspy-mcp-2026-04-07.jsonl"
    record = json.loads(log_path.read_text(encoding="utf-8").splitlines()[-1])

    assert record["event"] == "request"
    assert record["tool"] == "ixspy.search_etsy_goods_all"
    assert record["payload"] == payload


def test_log_error_writes_error_message(tmp_path: Path) -> None:
    now = datetime(2026, 4, 7, 12, 0, 0, tzinfo=timezone.utc)

    log_error(
        tool="ixspy.search_shopify_goods_all",
        payload={"page": 1},
        error=RuntimeError("boom"),
        now=now,
        base_dir=tmp_path,
    )

    log_path = tmp_path / "logs" / "ixspy-mcp-2026-04-07.jsonl"
    record = json.loads(log_path.read_text(encoding="utf-8").splitlines()[-1])

    assert record["event"] == "error"
    assert record["error"] == "RuntimeError: boom"
