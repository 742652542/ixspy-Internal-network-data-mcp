import asyncio
from pathlib import Path
import sys
from unittest.mock import AsyncMock, patch


sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.facebook_models import (
    FacebookAdProductsRequest,
    FacebookLibraryAdListRequest,
)
from ixspy_mcp.tools import (
    search_facebook_ad_products,
    search_facebook_library_ad_list,
)


def test_search_facebook_ad_products_tool_passthrough() -> None:
    payload = FacebookAdProductsRequest(product_name="dress")
    response = {"error": {"code": 0, "message": ""}, "data": {"count": 1, "list": []}}

    with patch(
        "ixspy_mcp.tools.facebook_service.search_ad_products",
        new=AsyncMock(return_value=response),
    ):
        result = asyncio.run(search_facebook_ad_products(payload))

    assert result == response


def test_search_facebook_library_ad_list_tool_passthrough() -> None:
    payload = FacebookLibraryAdListRequest(page_id="498299853562013")
    response = {"error": {"code": 0, "message": ""}, "data": {"count": 1, "list": []}}

    with patch(
        "ixspy_mcp.tools.facebook_service.search_library_ad_list",
        new=AsyncMock(return_value=response),
    ):
        result = asyncio.run(search_facebook_library_ad_list(payload))

    assert result == response
