from pathlib import Path
import sys


sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.category_data import (
    get_etsy_categories,
    get_shopify_categories,
    search_etsy_categories,
    search_shopify_categories,
)


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


def test_search_etsy_categories_returns_matches() -> None:
    results = search_etsy_categories("Jewelry", limit=5)
    assert isinstance(results, list)
    assert results
    assert "label" in results[0]
    assert "value" in results[0]
    assert "path" in results[0]


def test_search_shopify_categories_returns_matches() -> None:
    results = search_shopify_categories("Jewelry", limit=5)
    assert isinstance(results, list)
    assert results
    assert "label" in results[0]
    assert "value" in results[0]
    assert "path" in results[0]
