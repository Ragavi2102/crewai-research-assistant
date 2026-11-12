
from src.agents.researcher import researcher
from crewai import Task, Crew, Process

# Define a task for our Research Agent
research_task = Task(
    description=(
        "Explain what AI agents are. "
        "Include their working process and three real-world applications."
    ),

    expected_output=(
        "A beginner-friendly explanation of AI agents, "
        "their working process, and three real-world applications."
    ),

    agent=researcher
)

# Create a Crew with our Research Agent
research_crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,
    verbose=True
)

# Execute the task
result = research_crew.kickoff()

print("\n========== RESEARCH RESULT ==========")
print(result)
