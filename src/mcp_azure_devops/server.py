"""
Azure DevOps MCP Server

A simple MCP server that exposes Azure DevOps capabilities.
"""
import argparse

from mcp.server.fastmcp import FastMCP

from mcp_azure_devops.features import register_all
from mcp_azure_devops.utils import register_all_prompts

# Create a FastMCP server instance with a name
mcp = FastMCP("Azure DevOps")

# Register all features
register_all(mcp)
register_all_prompts(mcp)


def main():
    """Entry point for the command-line script."""
    import os
    parser = argparse.ArgumentParser(
        description="Run the Azure DevOps MCP server")
    parser.parse_args()

    # Get the port from Render (default to 8000 locally)
    port = int(os.environ.get("PORT", 8000))

    # Run server on all interfaces using SSE transport
    mcp.run(host="0.0.0.0", port=port, transport="sse")

if __name__ == "__main__":
    main()

