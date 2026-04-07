from typing import Any

from fastmcp import Context, FastMCP
from pydantic import BaseModel, Field

from .config import CredentialManager, RuntimeSettings
from .ixspy_service import IxSpyService
from . import models


credential_manager = CredentialManager()
runtime_settings = RuntimeSettings()
ixspy_service = IxSpyService(credential_manager, runtime_settings)

mcp = FastMCP(
    "IXSPY FastMCP Server",
    tasks=True,
)


class UploadImageBase64Request(BaseModel):
    image_base64: str = Field(..., description="Base64-encoded image content without the data: prefix")


@mcp.tool(
    name="ixspy.upload_image_base64",
    description="上传 Base64 图片到 ixspy，返回图片 URL（url）。入参：image_base64。",
)
async def upload_image_base64(payload: UploadImageBase64Request) -> dict[str, Any]:
    response = await ixspy_service.upload_image_base64(value=payload.image_base64)
    return response


@mcp.tool(
    name="ixspy.generate_image",
    task=True,
    description="提交作图任务并返回 task_id，不做轮询等待。入参：type、original_image、prompt/ratios 等。",
)
async def generate_image(payload: models.GenerationRequest, ctx: Context | None = None) -> dict[str, Any]:
    if ctx is not None:
        await ctx.report_progress(0, 100, message="submitting task")
    result = await ixspy_service.create_generation(payload)
    if ctx is not None:
        await ctx.report_progress(100, 100, message="submitted")
    return result


@mcp.tool(
    name="ixspy.get_task",
    description="查询作图任务状态与结果。入参：task_id。",
)
async def get_task_status(task_id: str) -> dict[str, Any]:
    return await ixspy_service.get_task(task_id)


@mcp.tool(
    name="ixspy.get_hd_image",
    task=True,
    description="获取作图任务的高清图 URL（hd_image_url）。入参：task_id。",
)
async def get_hd_image(task_id: str, ctx: Context | None = None) -> dict[str, Any]:
    if ctx is not None:
        await ctx.report_progress(0, 100, message="requesting_hd")
    response = await ixspy_service.get_hd_image(task_id)
    if ctx is not None:
        await ctx.report_progress(100, 100, message="hd_ready")
    return response


@mcp.tool(
    name="ixspy.list_tasks",
    description="分页查询任务列表。入参：page、page_size、status、type。",
)
async def list_tasks(
    page: int = 1,
    page_size: int = 20,
    status: str = "all",
    type: str = "all",
) -> dict[str, Any]:
    return await ixspy_service.list_tasks(page=page, page_size=page_size, status=status, task_type=type)
