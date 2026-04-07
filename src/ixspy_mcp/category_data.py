from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _load_categories(filename: str) -> list[dict[str, Any]]:
    data_path = Path(__file__).resolve().parent / "data" / filename
    try:
        raw = data_path.read_text(encoding="utf-8")
        return json.loads(raw)
    except Exception as exc:  # noqa: BLE001 - return a concise error upstream
        raise RuntimeError(f"load categories failed: {exc}") from exc


_ETSY_CATEGORIES = _load_categories("etsy_categories.json")
_SHOPIFY_CATEGORIES = _load_categories("shopify_categories.json")


def get_etsy_categories() -> list[dict[str, Any]]:
    return _ETSY_CATEGORIES


def get_shopify_categories() -> list[dict[str, Any]]:
    return _SHOPIFY_CATEGORIES
