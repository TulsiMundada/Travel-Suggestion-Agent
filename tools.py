import os
import dotenv

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams 

MAPS_MCP_URL = "https://mapstools.googleapis.com/mcp"

def get_maps_mcp_toolset():
    dotenv.load_dotenv()
    
    maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')

    if not maps_api_key:
        raise ValueError("MAPS_API_KEY not found in environment variables")

    tools = MCPToolset(
        connection_params=StreamableHTTPConnectionParams(
            url=MAPS_MCP_URL,
            headers={    
                "X-Goog-Api-Key": maps_api_key
            },
            timeout=30.0,
            sse_read_timeout=300.0
        )
    )

    print("Maps MCP Toolset configured.")
    return tools
