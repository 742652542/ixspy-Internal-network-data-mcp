import asyncio
from pathlib import Path
import sys


sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.category_models import CategorySearchRequest
from ixspy_mcp.tools import (
    get_etsy_categories,
    get_shopify_categories,
    search_etsy_categories,
    search_shopify_categories,
)


def test_get_etsy_categories_tool() -> None:
    result = asyncio.run(get_etsy_categories())
    assert result["code"] == 0
    assert isinstance(result["data"], list)


def test_get_shopify_categories_tool() -> None:
    result = asyncio.run(get_shopify_categories())
    assert result["code"] == 0
    assert isinstance(result["data"], list)


def test_search_etsy_categories_tool() -> None:
    payload = CategorySearchRequest(query="Jewelry", limit=5)
    result = asyncio.run(search_etsy_categories(payload))
    assert result["code"] == 0
    assert isinstance(result["data"], list)
    assert result["data"]


def test_search_shopify_categories_tool() -> None:
    payload = CategorySearchRequest(query="Jewelry", limit=5)
    result = asyncio.run(search_shopify_categories(payload))
    assert result["code"] == 0
    assert isinstance(result["data"], list)
    assert result["data"]
