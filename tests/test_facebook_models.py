from pathlib import Path
import sys

import pytest
from pydantic import ValidationError

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ixspy_mcp.facebook_models import (
    FacebookAdProductsRequest,
    FacebookLibraryAdListRequest,
)


def test_facebook_ad_products_request_allows_documented_fields() -> None:
    payload = FacebookAdProductsRequest(
        page=1,
        size=20,
        category_id=121,
        product_name="dress",
        source_content="wedding&shower|bride&shower",
        domain="example.com",
        created_time_start=0,
        created_time_end=0,
        orderBy="update_time",
        orderType="desc",
    )

    data = payload.model_dump(exclude_none=True)
    assert data["page"] == 1
    assert data["category_id"] == 121


def test_facebook_library_ad_list_request_allows_documented_fields() -> None:
    payload = FacebookLibraryAdListRequest(
        page=1,
        size=20,
        link="example.com",
        cta_type="SHOP_NOW",
        is_aaa_eligible="1",
        body="wedding shower",
        ad_type="DCO",
        is_active="1",
        start_date=0,
        end_date=0,
        active_days_start=1,
        active_days_end=30,
        collation_count_start=1,
        collation_count_end=10,
        collect_start_date=0,
        collect_end_date=0,
        orderBy="update_time",
        orderType="desc",
        collation_id="2850136788652291",
        page_id="498299853562013",
        archive_id="968188512259537",
        product_id="0",
    )

    data = payload.model_dump(exclude_none=True)
    assert data["link"] == "example.com"
    assert data["page_id"] == "498299853562013"


def test_facebook_request_rejects_undocumented_fields() -> None:
    with pytest.raises(ValidationError) as exc_info:
        FacebookAdProductsRequest(unknown_field="x")

    assert "unknown_field" in str(exc_info.value)
