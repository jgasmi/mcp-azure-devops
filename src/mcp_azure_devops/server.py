import os
import argparse
from mcp.server.fastmcp import FastMCP
from mcp_azure_devops.features import register_all
from mcp_azure_devops.utils import register_all_prompts

# ✅ Use Render-compatible binding
PORT = int(os.environ.get("PORT", 8000))
mcp = FastMCP("azure-devops", host="0.0.0.0", port=PORT)

# Register all features
register_all(mcp)
register_all_prompts(mcp)

def main():
    """Entry point for the command-line script."""
    parser = argparse.ArgumentParser(
        description="Run the Azure DevOps MCP server")
    parser.parse_args()

    # Explicitly run with SSE for local testing
    mcp.run(transport="sse")

if __name__ == "__main__":
    main()
