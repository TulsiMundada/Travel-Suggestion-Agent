import dotenv
from . import tools
from google.adk.agents import LlmAgent

dotenv.load_dotenv()

import os
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "false"

print("USE_VERTEX:", os.getenv("GOOGLE_GENAI_USE_VERTEXAI"))
print("PROJECT:", os.getenv("GOOGLE_CLOUD_PROJECT"))

# 🔍 Wrap tool for debugging
maps_toolset = tools.get_maps_mcp_toolset()

# OPTIONAL: debug wrapper if supported
try:
    for tool in maps_toolset.tools:
        def make_debug_run(tool):
            original_run = tool.run

            def debug_run(*args, **kwargs):
                print("\n🔍 TOOL CALLED:", tool.name)
                print("ARGS:", args, kwargs)
                try:
                    result = original_run(*args, **kwargs)
                    print("✅ TOOL RESULT:", result)
                    return result
                except Exception as e:
                    print("❌ TOOL ERROR:", str(e))
                    raise e

            return debug_run

        tool.run = make_debug_run(tool)
except Exception as e:
    print("Debug wrapper not applied:", e)


root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name='travel_agent',
    instruction="""
    You are a Travel Suggestion Assistant.

    You MUST use the Maps MCP tool to answer any query about:
    - cafes
    - restaurants
    - places
    - tourist attractions

    DO NOT use your own knowledge for places.

    TOOL USAGE RULES:
    - ALWAYS call Maps MCP tool for place queries
    - Call tool ONLY ONCE
    - Extract real data from tool response

    OUTPUT FORMAT:
    Return top 5 places with:
    • Name
    • Rating
    • FULL ADDRESS (street + area + city)

    IMPORTANT:
    - If tool returns results → DO NOT modify addresses
    - DO NOT return just city names
    - ALWAYS include full formatted address
    - If tool fails → then fallback to general knowledge

    """,

    tools=[maps_toolset]
)
