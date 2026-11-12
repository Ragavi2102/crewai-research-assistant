
from pathlib import Path
from crew import research_crew


def run_research(topic):

    print("\nStarting AI Research Assistant...")
    print(f"\nResearch Topic: {topic}")

    result = research_crew.kickoff(
        inputs={"topic": topic}
    )

    # Convert the final result into text
    report = str(result)

    # Create the outputs folder if it doesn't exist
    output_folder = Path("outputs")
    output_folder.mkdir(exist_ok=True)

    # Save the report
    report_path = output_folder / "research_report.md"
    report_path.write_text(report, encoding="utf-8")

    print("\n========== FINAL RESEARCH REPORT ==========\n")
    print(report)

    print(f"\nReport saved successfully at: {report_path}")

    return result


if __name__ == "__main__":

    topic = input("Enter a research topic: ")
    run_research(topic)
