
from crewai import Task

from src.agents.researcher import researcher
from src.agents.analyst import analyst
from src.agents.writer import writer


# Task 1: Research
research_task = Task(
    description=(
        "Research the topic: {topic}. "
        "Explain its meaning, background, important concepts, "
        "working process, and real-world applications."
    ),

    expected_output=(
        "Detailed research findings about the topic, "
        "organized with headings and relevant examples."
    ),

    agent=researcher
)


# Task 2: Analysis
analysis_task = Task(
    description=(
        "Analyze the research findings about {topic}. "
        "Identify the most important insights, advantages, "
        "limitations, and practical implications."
    ),

    expected_output=(
        "A structured analysis containing key insights, "
        "advantages, limitations, and conclusions."
    ),

    agent=analyst,
    context=[research_task]
)


# Task 3: Report Writing
writing_task = Task(
    description=(
        "Create a professional research report about {topic} "
        "using the research and analysis provided. "
        "Include an introduction, key findings, advantages, "
        "limitations, applications, and conclusion."
    ),

    expected_output=(
        "A complete, well-structured research report "
        "with clear headings and beginner-friendly explanations."
    ),

    agent=writer,
    context=[research_task, analysis_task]   #use output research,analysis output
)
