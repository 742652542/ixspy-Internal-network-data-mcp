# Repo Guidance for OpenCode

- Entry point: run the MCP server with `python server.py` (binds HTTP on `0.0.0.0:8080`).
- MCP tool wiring lives in `src/ixspy_mcp/tools.py`; the Etsy search HTTP call is in `src/ixspy_mcp/etsy_service.py` with a fixed URL.
- There is no build config or dependency manifest in this repo; avoid assuming a package manager.
- Tests (if any) are run with `pytest`.
