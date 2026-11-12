
from crewai import Agent, LLM
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Connect to Gemini
gemini_llm = LLM(
    model="gemini/gemini-3.5-flash",
    temperature=0.4
)

# Create Writer Agent
writer = Agent(
    role="Professional Research Report Writer",

    goal=(
        "Create a clear, structured, informative, "
        "and beginner-friendly research report."
    ),

    backstory=(
        "You are a professional report writer. "
        "You transform research findings and analysis "
        "into well-organized reports with headings, "
        "examples, and clear explanations."
    ),

    llm=gemini_llm,
    verbose=True,
    allow_delegation=False
)
