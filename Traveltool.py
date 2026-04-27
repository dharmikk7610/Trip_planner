from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

# Web search tool using DuckDuckGo
@tool("search_web_tool")  # Only tool name
def search_web_tool(query: str) -> str:
    """
    Search the web using DuckDuckGo.

    IMPORTANT:
    - Always pass query as a plain string
    - Example: "best food in Rome"
    """
    try:
        search_tool = DuckDuckGoSearchResults(num_results=5)
        return search_tool.run(query)
    except Exception as e:
        return f"Search failed: {str(e)}"