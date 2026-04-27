from crewai import Agent, LLM
from Traveltool import search_web_tool
from dotenv import load_dotenv

load_dotenv()

# LLM (Ollama)
ollama_llm = LLM(
    model="ollama/llama3.2:latest",
    base_url="http://localhost:11434",
    temperature=0
)

# ------------------ Agents ------------------

guide_expert = Agent(
    role="City Local Guide Expert",
    goal="Find best attractions, food, and experiences",
    backstory="""
    You are a local travel expert.

    IMPORTANT:
    - Always use search_web_tool when needed
    - Pass query as plain string
    Example: {"query": "top attractions in Rome"}
    """,
    tools=[search_web_tool],
    verbose=True,
     max_iter=3 ,
    llm=ollama_llm
)

location_expert = Agent(
    role="Travel Logistics Expert",
    goal="Provide travel, visa, and transport info",
    backstory="""
    You are a travel logistics expert.

    Always use search_web_tool for latest info.
    """,
    tools=[search_web_tool],
    verbose=True,
     max_iter=3,
    llm=ollama_llm
)

planner_expert = Agent(
    role="Travel Planner Expert",
    goal="Create a full travel itinerary",
    backstory="Expert in planning complete trips.",
    verbose=True,
     max_iter=2,
    llm=ollama_llm
)