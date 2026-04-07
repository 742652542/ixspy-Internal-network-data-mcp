from pathlib import Path
import sys

import pytest
from pydantic import ValidationError

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.shopify_models import ShopifyGoodsAllRequest


def test_shopify_request_allows_documented_fields() -> None:
    payload = ShopifyGoodsAllRequest(
        page=1,
        size=20,
        orderBy="created_time",
        orderType="desc",
        rank_type="search",
        customized="-1",
        product_name="dress",
        domain="example.myshopify.com",
        category_id=0,
        min_price_start=10,
        min_price_end=100,
        created_time_start=1772380800,
        created_time_end=1774972800,
    )

    data = payload.model_dump(exclude_none=True)
    assert data["page"] == 1
    assert data["category_id"] == 0


def test_shopify_request_rejects_removed_fields() -> None:
    with pytest.raises(ValidationError) as exc_info:
        ShopifyGoodsAllRequest(shop_id="123")

    assert "shop_id" in str(exc_info.value)
