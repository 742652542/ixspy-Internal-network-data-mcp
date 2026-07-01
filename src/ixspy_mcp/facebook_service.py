from __future__ import annotations

from typing import Any

import httpx

from .facebook_models import FacebookAdProductsRequest, FacebookLibraryAdListRequest


class FacebookService:
    def __init__(
        self,
        ad_products_url: str = "http://etsy.int.ixspy.com/api/facebook/public/ad-products",
        library_ad_list_url: str = "http://etsy.int.ixspy.com/api/facebook/public/library/ad-list",
    ) -> None:
        self._ad_products_url = ad_products_url
        self._library_ad_list_url = library_ad_list_url
        self._timeout = httpx.Timeout(30.0)

    async def search_ad_products(self, payload: FacebookAdProductsRequest) -> dict[str, Any]:
        data = payload.model_dump(exclude_none=True)
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.post(self._ad_products_url, json=data)

        if response.status_code < 200 or response.status_code >= 300:
            snippet = response.text[:200].replace("\n", " ")
            raise RuntimeError(f"HTTP {response.status_code}: {snippet}")

        return response.json()

    async def search_library_ad_list(
        self, payload: FacebookLibraryAdListRequest
    ) -> dict[str, Any]:
        data = payload.model_dump(exclude_none=True)
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.post(self._library_ad_list_url, json=data)

        if response.status_code < 200 or response.status_code >= 300:
            snippet = response.text[:200].replace("\n", " ")
            raise RuntimeError(f"HTTP {response.status_code}: {snippet}")

        return response.json()
