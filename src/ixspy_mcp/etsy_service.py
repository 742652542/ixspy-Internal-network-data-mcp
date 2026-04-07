from __future__ import annotations

from typing import Any

import httpx

from .etsy_models import EtsyGoodsAllRequest


class EtsyGoodsAllService:
    def __init__(self, url: str = "http://etsy.int.ixspy.com/api/etsy-goods-all") -> None:
        self._url = url
        self._timeout = httpx.Timeout(30.0)

    async def search(self, payload: EtsyGoodsAllRequest) -> dict[str, Any]:
        data = payload.model_dump(exclude_none=True)
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.post(self._url, json=data)

        if response.status_code < 200 or response.status_code >= 300:
            snippet = response.text[:200].replace("\n", " ")
            raise RuntimeError(f"HTTP {response.status_code}: {snippet}")

        return response.json()
