# ixspy Internal Network Data MCP

一个轻量级 FastMCP 服务，用于封装公司内部 Etsy 商品全局搜索接口，并以 MCP 工具形式提供给上层调用。

## 功能

- MCP 工具：`ixspy.search_etsy_goods_all`
- 支持完整筛选参数（关键词、价格区间、销量、收藏、评分、时间、发货地等）
- 请求参数通过 Pydantic 模型提供字段说明
- 响应结构透传 `{code, message, data}`
- 固定接口地址：`http://etsy.int.ixspy.com/api/etsy-goods-all`

## 目录结构

- `server.py`：MCP 服务入口
- `src/ixspy_mcp/tools.py`：工具注册
- `src/ixspy_mcp/etsy_service.py`：HTTP 调用与错误处理
- `src/ixspy_mcp/etsy_models.py`：请求参数模型

## 快速启动

```bash
python server.py
```

默认监听 `0.0.0.0:8080`。

## 测试

```bash
pytest
```
