
from crewai import Crew, Process

# Import our three agents
from src.agents.researcher import researcher
from src.agents.analyst import analyst
from src.agents.writer import writer

# Import our three tasks
from src.tasks.research_tasks import (
    research_task,
    analysis_task,
    writing_task
)


# Create our Multi-Agent Crew
research_crew = Crew(

    agents=[
        researcher,
        analyst,
        writer
    ],

    tasks=[
        research_task,
        analysis_task,
        writing_task
    ],

    process=Process.sequential,

    verbose=True
)
