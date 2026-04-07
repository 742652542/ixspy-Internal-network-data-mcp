from pathlib import Path
import sys


sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.category_data import get_etsy_categories, get_shopify_categories


def test_get_etsy_categories_returns_list() -> None:
    data = get_etsy_categories()
    assert isinstance(data, list)
    assert data
    assert "label" in data[0]
    assert "value" in data[0]


def test_get_shopify_categories_returns_list() -> None:
    data = get_shopify_categories()
    assert isinstance(data, list)
    assert data
    assert "label" in data[0]
    assert "value" in data[0]
