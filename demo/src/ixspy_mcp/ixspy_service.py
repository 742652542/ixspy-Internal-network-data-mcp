from __future__ import annotations

import asyncio
from typing import Any

from ixspy_img_api.AIImage import AIImageAPIError
from ixspy_img_api import AIImageGenerator

from .config import CredentialManager, RuntimeSettings
from . import models


class IxSpyService:
    def __init__(self, credentials: CredentialManager, settings: RuntimeSettings | None = None) -> None:
        self._credentials = credentials
        self._settings = settings or RuntimeSettings()
        self._lock = asyncio.Lock()
        self._client: AIImageGenerator | None = None
        self._client_key: str | None = None

    async def _get_client(self) -> AIImageGenerator:
        api_key = await self._credentials.get_api_key()
        if not api_key:
            raise RuntimeError("API key not configured")
        async with self._lock:
            if self._client is None or self._client_key != api_key:
                self._client = AIImageGenerator(api_key=api_key)
                self._client_key = api_key
        return self._client

    async def _call(self, func, *args, **kwargs):
        try:
            return await asyncio.to_thread(func, *args, **kwargs)
        except AIImageAPIError as exc:
            raise RuntimeError(f"[{exc.code}] {exc.message}") from exc

    @staticmethod
    def _single_image(images: list[str]) -> str:
        if len(images) != 1:
            raise ValueError("requires a single original_image")
        return images[0]

    async def upload_image_base64(self, value: str) -> dict[str, Any]:
        client = await self._get_client()
        url = await self._call(client.upload_image, image_base64=value)
        return {"url": url}

    async def create_generation(self, payload: models.GenerationRequest) -> dict[str, Any]:
        client = await self._get_client()
        task_type = payload.type
        images = [str(item) for item in payload.original_image]

        if task_type == "custom_composition_multi":
            task_id = await self._call(
                client.create_custom_composition_multi,
                images,
                payload.prompt or "",
                payload.ratios or "auto",
            )
        elif task_type == "custom_composition":
            task_id = await self._call(
                client.create_custom_composition,
                self._single_image(images),
                payload.prompt or "",
                payload.ratios or "auto",
            )
        elif task_type == "scene_replacement":
            task_id = await self._call(
                client.create_scene_replacement,
                self._single_image(images),
                prompt=payload.prompt,
                reference_image=payload.reference_image,
                ratios=payload.ratios or "auto",
            )
        elif task_type == "product_replacement":
            task_id = await self._call(
                client.create_product_replacement,
                self._single_image(images),
                payload.reference_image,
                prompt=payload.prompt,
            )
        elif task_type == "product_recoloring":
            task_id = await self._call(
                client.create_product_recoloring,
                self._single_image(images),
                payload.color,
            )
        elif task_type == "partial_redraw":
            task_id = await self._call(
                client.create_partial_redraw,
                self._single_image(images),
                payload.prompt or "",
                reference_image=payload.reference_image,
            )
        elif task_type == "smart_expand":
            task_id = await self._call(
                client.create_smart_expand,
                self._single_image(images),
                payload.direction or "auto",
                payload.ratios or "auto",
            )
        elif task_type == "translation":
            task_id = await self._call(
                client.create_translation,
                self._single_image(images),
                payload.source_language or "auto",
                payload.target_language or "auto",
            )
        elif task_type == "ai_upscale_2k":
            task_id = await self._call(
                client.create_ai_upscale_2k,
                self._single_image(images),
            )
        else:
            raise ValueError(f"Unsupported ixspy type: {task_type}")

        return {"task_id": str(task_id)}

    async def get_task(self, task_id: str) -> dict[str, Any]:
        client = await self._get_client()
        return await self._call(client.get_task_status, task_id)

    async def get_hd_image(self, task_id: str) -> dict[str, Any]:
        client = await self._get_client()
        url = await self._call(client.get_hd_image, task_id)
        return {"hd_image_url": url}

    async def list_tasks(
        self,
        *,
        page: int = 1,
        page_size: int = 20,
        status: str | None = None,
        task_type: str | None = None,
    ) -> dict[str, Any]:
        client = await self._get_client()
        return await self._call(
            client.list_tasks,
            page=page,
            page_size=page_size,
            status=None if status == "all" else status,
            task_type=None if task_type == "all" else task_type,
        )
