
from crewai import Agent, LLM
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Connect to Gemini
gemini_llm = LLM(
    model="gemini/gemini-3.5-flash",
    temperature=0.2
)

# Create our Research Agent
researcher = Agent(
    role="Senior AI Research Specialist",

    goal=(
        "Research the given topic thoroughly and provide "
        "accurate, relevant, and well-organized information."
    ),

    backstory=(
        "You are an experienced research specialist. "
        "You are skilled at understanding complex topics, "
        "identifying important information, and explaining "
        "findings in a clear and simple way."
    ),

    llm=gemini_llm,
    verbose=True,
    allow_delegation=False
)
