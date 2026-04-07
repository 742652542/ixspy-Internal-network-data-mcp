# 分类资源 MCP 设计说明

## 背景与目标
- 需要在 MCP 中提供 Etsy / Shopify 分类树数据，供上层查询接口使用分类 ID。
- 分类数据为静态资源，随服务发布，无需运行时更新。
- 返回格式与现有搜索接口一致的 `{code, message, data}` 结构。

## 范围
### 包含
- 新增两个 MCP 工具：`ixspy.get_etsy_categories`、`ixspy.get_shopify_categories`。
- 分类数据以 JSON 文件形式内置。
- 服务启动时加载并缓存分类数据。

### 不包含
- 分类数据在线更新或热更新机制。
- 对分类树进行搜索/筛选的接口。

## 方案与取舍
### 方案 A（采用）
- 内置 JSON 文件 + 新增 MCP 工具直接返回。
- 优点：结构清晰、数据与逻辑分离、调用简单。
- 缺点：更新需要替换文件并重启服务。

### 方案 B
- 分类树写入 Python 常量。
- 缺点：文件巨大、维护困难、diff 噪音高。

### 方案 C
- 运行时解析 JS 文件（`var X = [...]`）。
- 缺点：格式脆弱、运行时解析成本高。

## 设计细节
### 接口定义
- `ixspy.get_etsy_categories`
- `ixspy.get_shopify_categories`

### 入参
- 无。

### 返回
- 统一返回：`{"code": 0, "message": "", "data": <categories>}`
- `data` 为 JSON 数组（形如 `[{"label": "...", "value": 1, "children": [...]}, ...]`）。
- 失败时返回：`{"code": 1, "message": "load categories failed: <error>", "data": null}`。

### 目录结构
- `src/ixspy_mcp/data/etsy_categories.json`
- `src/ixspy_mcp/data/shopify_categories.json`

### 加载与缓存
- 服务启动时读取 JSON 并缓存到模块级变量。
- 工具调用时直接返回缓存数据。

## 数据流
1. 服务启动：读取 `data/*.json` -> 解析为 Python 对象 -> 缓存。
2. 调用工具：返回 `{code, message, data}`，其中 `data` 为缓存对象。

## 错误处理
- 文件不存在、JSON 解析失败、读取异常：捕获并返回 `code=1` 的错误结构。
- 错误信息包含简短原因，避免输出长堆栈。

## 测试点（如需添加）
- 工具可被调用且无入参。
- 正常返回结构，`data` 为数组并包含 `label`、`value`。
- 当文件缺失时，返回结构完整且 `code=1`。

## 兼容性与影响
- 不影响现有搜索工具。
- 不引入新的依赖。

## 发布与运维
- 更新分类数据：替换 JSON 文件并重启服务。
