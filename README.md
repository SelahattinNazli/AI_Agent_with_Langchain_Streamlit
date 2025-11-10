
# AI Agent with LangGraph, Streamlit & Notion Integration

## Overview

This project demonstrates a **local, privacy-first AI Agent** powered by **Ollama**, orchestrated via **LangGraph**, and deployed with a **Streamlit** interface.  

The agent follows the **ReAct (Reasoning + Acting)** paradigm — it reasons step by step, chooses tools, performs actions (like searching the web or saving to Notion), and then responds intelligently.

The system is extended with a **Notion integration**, allowing the agent to **automatically save results, summaries, or structured knowledge directly into your Notion workspace** — bridging AI reasoning with long-term knowledge storage.

This architecture combines:
- **Ollama** for local LLM inference  
- **LangGraph** for multi-step reasoning  
- **Streamlit** for a modern interactive UI  
- **Notion API** for persistent knowledge saving  

---

## Key Features

- **Local LLM via Ollama** — Runs completely offline, no API costs.  
- **LangGraph ReAct Agent** — Combines reasoning with tool-based actions.  
- **DuckDuckGo Search Tool** — Fetches up-to-date web content.  
- **Website Visitor Tool** — Visits and extracts structured content.  
- **Notion Integration** — Saves query–answer pairs into a Notion database.  
- **Memory Persistence** — Uses LangGraph `MemorySaver` for checkpointing.  
- **Extensible Tool Design** — Plug new tools easily (e.g., PDF reader, API fetcher).  
- **Unit Testing Ready** — Testable with `pytest`.

---

## Project Structure

```plaintext
AI_Agent_with_Langchain_Streamlit/
│
├── src/
│   ├── app.py              → Streamlit UI and input/output flow
│   ├── agent.py            → Agent logic and Ollama model configuration
│   └── tools/
│       ├── visit_website.py → Website analysis tool
│       ├── search_tool.py   → Web search via DuckDuckGo
│       └── notion_tool.py   → Save generated results to Notion
│
├── tests/
│   ├── test_agent.py       → Unit tests for reasoning pipeline
│   └── test_app.py         → Streamlit integration tests
│
├── requirements.txt        → Dependencies list
└── README.md               → Project documentation
```

## Installation
1️⃣ **Clone the repository**
```bash
git clone https://github.com/SelahattinNazli/AI_Agent_with_Langchain_Streamlit.git
cd AI_Agent_with_Langchain_Streamlit
```
2️⃣ **Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```
4️⃣ **Install Ollama (if not already)**
```bash
Follow official setup: https://ollama.ai/download

Then pull the model you want to use (e.g. GPT-4o-mini):

ollama pull gpt-4o-mini
```
5️⃣ **Configure Notion (optional)**
Create a .env file in your project root:
```bash
NOTION_API_KEY=your_notion_integration_token
NOTION_DATABASE_ID=your_database_id
```
**Run the App**
```bash
streamlit run src/app.py
```

The app will open automatically at:
👉 http://localhost:8501

**Example Usage**

User:

Research the MLOps trends in 2024 and save them to Notion.

Agent:

🧠 Thinking...
🔍 Searching the web for “MLOps trends 2024”
📄 Analyzing sources
💾 ✅ Successfully saved the summarized insights to Notion!

🔗 Notion Integration (New Feature)

Your AI agent can now act as a knowledge collector — every meaningful answer, summary, or insight can be automatically stored in Notion.

Setup Steps

Go to https://www.notion.so/my-integrations

Create an integration → copy the token

Share your database with that integration

Copy your Database ID

Add both values to .env

That’s it — the agent can now log insights in your Notion workspace.

## Testing

Run all tests:
```bash
pytest -v
```

Run only agent tests:
```bash
PYTHONPATH=src pytest tests/test_agent.py -v
```
## Tech Stack
Component	Purpose

Ollama	Local LLM hosting and inference

LangGraph	Agent reasoning orchestration

Streamlit	Interactive web interface

DuckDuckGo Search	Retrieve live web data

Markdownify	Convert HTML into clean markdown

Notion SDK	Connect and save insights to Notion

## Vision

This project goes beyond Q&A — it represents a new generation of self-hosted AI assistants capable of:

Understanding context

Taking structured actions

Interfacing with real-world APIs and tools

Storing knowledge persistently

With Ollama + LangGraph + Notion, you have a foundation for autonomous, private, and extensible AI workflows.

## License

MIT License © 2025 Selahattin Nazlı
