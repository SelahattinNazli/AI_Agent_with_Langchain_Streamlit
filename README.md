# AI Agent with LangGraph and Streamlit

## Overview
This project demonstrates a web-based AI Agent built using the **LangGraph** framework and **Streamlit**. The agent can perform web searches, visit websites, and analyze content using **GPT-4o-mini**. It implements **ReAct reasoning**, combining thought, actions, and tools for complex problem solving.

The project is structured with a **`tools/` directory**, which contains custom tools like `visit_website.py`. This modular design allows the agent to easily integrate additional tools in the future without modifying the core agent logic. For example, new tools for data scraping, API access, or custom analytics can simply be added to the `tools/` folder and included in the agent’s configuration.

This approach ensures the project remains **extensible and maintainable**, supporting future enhancements or experimentation with new capabilities without major refactoring.


## Features
- Interactive **Streamlit** frontend for user queries
- **DuckDuckGo** search integration
- Custom tool to visit websites and extract markdown content
- ReAct-style reasoning using **GPT-4o-mini**
- Memory persistence with **MemorySaver** checkpointing
- Unit testing for agent and app behavior

## Project Structure

```plaintext
AI_Agent_with_Langchain_Streamlit/
│
├── app.py → Streamlit frontend
├── agent.py → Agent configuration and tool integration
├── tools/
│   └── visit_website.py → Custom website visit tool
├── tests/
│   ├── test_agent.py → Unit tests for agent logic
│   └── test_app.py → Unit tests for Streamlit app integration
└── requirements.txt → Python dependencies
```

## Installation

1. **Clone the repository**

```bash
git clone <repository_url>
cd AI_Agent_with_Langchain_Streamlit
```

## Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Set your OpenAI API key

```bash
export OPENAI_API_KEY="your_api_key_here"   # macOS/Linux
setx OPENAI_API_KEY "your_api_key_here"     # Windows
```

## Run the Streamlit app

```bash
streamlit run app.py
```

## Example Usage

Ask the agent anything in the chat interface:

User: "Find recent AI news"
Assistant: "Here are the top results from DuckDuckGo..."


Screenshots or GIFs of the interaction can be added here for better visualization.

## Unit Testing

Tests are provided for both the agent logic and Streamlit app using pytest and unittest.mock for safe API testing without a real OpenAI key.

## Run tests

```bash
PYTHONPATH=src pytest tests/ -v
```

## Test Coverage

test_agent.py: Validates call_agent function with responses.

test_app.py: Ensures the Streamlit app correctly calls call_agent with responses.

## Dependencies

Python 3.12+

Streamlit

LangGraph & LangChain

OpenAI Python SDK

DuckDuckGo Search (ddgs)

python-doten
