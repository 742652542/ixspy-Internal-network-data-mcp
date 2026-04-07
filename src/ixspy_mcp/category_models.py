from __future__ import annotations

from pydantic import BaseModel, Field


class CategorySearchRequest(BaseModel):
    """分类搜索请求参数（字段可选，提供提示用）"""

    query: str = Field(..., description="分类关键词，支持 | 或 & 组合")
    limit: int | None = Field(None, ge=1, description="返回条数上限")
