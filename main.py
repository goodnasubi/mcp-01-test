import mcp

@mcp.tool
def add(a: int, b: int) -> int:
    """2つの数値を加算します。"""
    return a + b

if __name__ == "__main__":
    server = mcp.FastMCP(tools=[add]) # または `mcp_os_name`のようなクラス名を使用
    server.run(transport='stdio') # 通信方法を指定
