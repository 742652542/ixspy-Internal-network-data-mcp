# import sys
# from pathlib import Path

# sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

# from ixspy_mcp.tools import mcp
from src.ixspy_mcp.tools import mcp  # noqa: F401


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8081)
