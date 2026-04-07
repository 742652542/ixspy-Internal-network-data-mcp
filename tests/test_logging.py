from datetime import datetime, timezone
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.logging import append_log_record, get_daily_log_path


def test_append_log_record_writes_daily_file(tmp_path: Path) -> None:
    now = datetime(2026, 4, 7, 12, 0, 0, tzinfo=timezone.utc)
    record = {"event": "request", "tool": "ixspy.get_etsy_categories"}

    append_log_record(record, now=now, base_dir=tmp_path)

    log_path = get_daily_log_path(now=now, base_dir=tmp_path)
    assert log_path.exists()
    content = log_path.read_text(encoding="utf-8").splitlines()
    assert len(content) == 1
    assert json.loads(content[0]) == record


def test_append_log_record_creates_logs_dir(tmp_path: Path) -> None:
    now = datetime(2026, 4, 7, 12, 0, 0, tzinfo=timezone.utc)
    record = {"event": "request", "tool": "ixspy.get_shopify_categories"}

    append_log_record(record, now=now, base_dir=tmp_path)

    logs_dir = tmp_path / "logs"
    assert logs_dir.exists()
    assert logs_dir.is_dir()
