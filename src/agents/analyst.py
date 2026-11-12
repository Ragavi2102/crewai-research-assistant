
from crewai import Agent, LLM
from dotenv import load_dotenv

# Load API key
load_dotenv()

# Connect to Gemini
gemini_llm = LLM(
    model="gemini/gemini-3.5-flash",
    temperature=0.2
)

# Create Analysis Agent
analyst = Agent(
    role="Senior Research Analyst",

    goal=(
        "Analyze research findings, identify important insights, "
        "and organize information into meaningful conclusions."
    ),

    backstory=(
        "You are an experienced research analyst. "
        "You specialize in examining information, finding patterns, "
        "identifying important points, and producing logical conclusions."
    ),

    llm=gemini_llm,
    verbose=True,
    allow_delegation=False
)
