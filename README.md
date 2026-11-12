# 🤖 CrewAI Multi-Agent Research Assistant

A simple AI-powered research assistant built using **CrewAI, Google Gemini, and Streamlit**.

Instead of relying on a single AI agent, this project uses a small team of AI agents that work together to research a topic, analyze the findings, and create a structured report.

## ✨ How It Works

The application follows a three-step workflow:

**🔍 Researcher Agent**  
Researches the given topic and gathers important information, including key concepts, background, working processes, and real-world applications.

**📊 Analyst Agent**  
Reviews the research findings and identifies important insights, advantages, limitations, and practical implications.

**✍️ Writer Agent**  
Uses the research and analysis to create a clear, structured, and beginner-friendly report.

### Workflow

```text
User enters a topic
        ↓
Researcher Agent
        ↓
Analyst Agent
        ↓
Writer Agent
        ↓
Final Research Report
```

## 🛠️ Technologies Used

- **Python**
- **CrewAI** – for building and coordinating AI agents
- **Google Gemini API** – as the language model
- **Streamlit** – for the web interface
- **UV** – for Python project and dependency management

## 📁 Project Structure

```text
crewai-research-assistant/
│
├── app/
│   └── app.py
│
├── src/
│   ├── agents/
│   │   ├── researcher.py
│   │   ├── analyst.py
│   │   └── writer.py
│   │
│   └── tasks/
│       └── research_tasks.py
│
├── outputs/
│   └── research_report.md
│
├── crew.py
├── main.py
├── pyproject.toml
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd crewai-research-assistant
```

### 2. Install dependencies

This project uses UV for dependency management.

```bash
uv sync
```

### 3. Add your Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

**Important:** Never upload your `.env` file or API key to GitHub.

### 4. Run the application

```bash
uv run streamlit run app/app.py
```

Open the local URL shown in your terminal, enter a research topic, and click **Generate Research Report**.

## 📄 Output

The application displays the final research report in the Streamlit interface and also saves it as a Markdown file inside the `outputs` folder.

## 💡 Example Topic

You can try a topic such as:

> Generative AI and its applications in healthcare

The agents will work together to research, analyze, and create a structured report about the topic.

## 🔮 Future Improvements

Some ideas for improving the project include:

- Adding web search tools for research
- Including source citations in reports
- Allowing users to download reports
- Adding more specialized agents
- Supporting different report formats

## 👩‍💻 Author

**Ragavi**

---

If you found this project useful, feel free to explore, modify, and build on it!
