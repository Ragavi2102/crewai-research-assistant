
from dotenv import load_dotenv
from crewai import LLM

# Load the API key from .env
load_dotenv()

# Configure Gemini
llm = LLM(
    model="gemini/gemini-3.5-flash",
    temperature=0.2
)

# Send a test question
response = llm.call(
    [{"role": "user", "content": "Explain AI agents in two simple sentences."}]
)

print("Gemini Response:")
print(response)
