# 产品全局搜索 MCP 设计文档

- 日期：2026-04-07
- 主题：Etsy 商品全局搜索 MCP（`ixspy.search_etsy_goods_all`）
- 目标：提供一个 MCP 工具封装 `http://etsy.int.ixspy.com/api/etsy-goods-all`，对外暴露清晰的参数提示，响应原样透传
- 鉴权：无（当前版本不做鉴权）

## 背景与范围

该功能需要参考现有 `demo/` 目录中的 FastMCP 结构，实现一个新 MCP 工具，用于调用 Etsy 商品全局搜索接口。当前范围仅包含：

- 新增 MCP 工具 `ixspy.search_etsy_goods_all`
- 请求参数提示完整（类型 + 说明），不做严格枚举/区间硬校验
- 调用固定接口地址，响应结构透传
- 完成后移除 `demo/` 目录

不包含：鉴权接入、缓存、批量任务、复杂可观测性或自动化测试体系。

## 设计目标

1. **最小改动、可复用结构**：沿用 `demo` 的 service + models + tools 分层。
2. **参数提示清晰**：在 Pydantic 模型里补齐字段说明，便于 AI/调用方理解。
3. **保持与后端一致**：只做基础类型校验，业务约束交给后端。

## 架构与组件

### 组件划分

1. `ixspy_mcp/etsy_service.py`
   - 负责 HTTP 调用与错误处理
   - 提供 `search_etsy_goods_all(payload)` 方法
2. `ixspy_mcp/etsy_models.py`
   - 定义请求模型（所有字段可选）与响应载荷类型（保持透传）
3. `ixspy_mcp/tools.py`
   - 注册 MCP 工具 `ixspy.search_etsy_goods_all`
   - 仅做参数模型解析并转交 service
4. `server.py`
   - 保持现有入口不变

### 数据流

1. MCP 工具接收请求模型
2. Service 发送 POST JSON 到固定地址
3. 返回 JSON 响应，工具原样透传

## 接口设计

### MCP 工具

- 名称：`ixspy.search_etsy_goods_all`
- 说明：根据多维度筛选条件搜索 Etsy 商品，返回接口响应
- 入参：`EtsyGoodsAllRequest`（全字段可选）
- 出参：原样透传 `{code, message, data}`

### 请求字段（提示型）

模型字段将覆盖文档所有参数，包含：

- 基础：`page`, `size`, `orderBy`, `orderType`
- 文本搜索：`search_content`, `search_content_not`, `store_id`, `materials`, `categoryIds`, `category_path`
- 标志位筛选：`best_seller`, `personalization`, `is_ad`, `netfly_tag`, `etsy_pick`, `rare_find`
- 时间筛选：`day`, `latest_sale_time`, `ad_time_start`, `ad_time_end`
- 24 小时购买：`sales_24hours`
- 区间筛选：`offer_price_*`, `max_price_*`, `total_price_*`, `cost_*`, `favorites_total_*`, `reviews_total_*`, `sales_total_*`, `carts_total_*`, `est_sales_total_*`, `rating_*`, `process_*`, `received_*`
- 发货地：`ships_from`

字段类型与说明将基于接口文档写入 `Field(..., description=...)`，用于提示。

### 响应

不做结构改写与字段映射，直接透传接口响应。

## 错误处理

- HTTP 失败或非 2xx：抛出 `RuntimeError`，包含状态码与摘要信息
- 业务错误（`code != 0`）：不在 MCP 侧特殊处理，直接透传
- 超时：设置请求超时（默认 30 秒），超时报错

## 测试与验证

- 不新增自动化测试
- 手动验证示例请求（参考文档 4.x）

## 交付与清理

- 新增 MCP 工具与对应模块
- 删除 `demo/` 目录

## 开放问题

- 无
