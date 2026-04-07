from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


IXSPY_TYPES: tuple[str, ...] = (
    "custom_composition_multi",
    "custom_composition",
    "scene_replacement",
    "product_replacement",
    "product_recoloring",
    "partial_redraw",
    "smart_expand",
    "translation",
    "ai_upscale_2k",
)


class GenerationRequest(BaseModel):
    type: Literal[*IXSPY_TYPES] = Field(..., description="Generation type supported by ixspy")
    original_image: list[HttpUrl] = Field(
        ..., min_length=1, max_length=5, description="List of input image URLs (1-5)"
    )
    prompt: str | None = Field(None, description="Optional text prompt")
    reference_image: str | None = Field(None, description="Optional reference image URL")
    ratios: str | None = Field(None, description="Output aspect ratio")
    color: str | None = Field(None, description="Color adjustment or palette hint")
    direction: str | None = Field(None, description="Directional guidance for generation")
    source_language: str | None = Field(None, description="Source language for translation")
    target_language: str | None = Field(None, description="Target language for translation")


class ErrorPayload(BaseModel):
    code: int
    message: str
    time: str | None = None


class TaskStatusResponse(BaseModel):
    task_id: str
    status: str
    sd_image_url: HttpUrl | None = None
    hd_image_url: HttpUrl | None = None
    type: str | None = None
