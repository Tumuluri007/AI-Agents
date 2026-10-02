# LangChain- Develop AI Agents with LangChain & LangGraph 🦜🔗

A ReAct AI agent built with LangChain that searches the web using Tavily and runs on a local Llama 3.2 model.

# AI Agents: ReAct Agent with LangChain

A **ReAct agent** (Reason + Act) built with LangChain. The agent thinks about a question, decides whether it needs a tool, calls it, reads the result, and then answers.

## What it does

- Takes a question such as *"What is the weather in Tokyo?"*
- The model decides it needs live information and **calls a search tool**
- The tool searches the web with **Tavily**
- The agent reads the results and writes the final answer

## How it works

```
You ask a question
      ↓
Agent (Llama 3.2) reasons: "I need to search"
      ↓
Tool call: search("weather in Tokyo")
      ↓
Tavily searches the web and returns results
      ↓
Agent reads the results and answers
```

## Two ways to build the search tool

| Approach | How |
|---|---|
| Custom tool | `TavilyClient` + the `@tool` decorator, with my own function and docstring |
| Ready-made tool | `TavilySearch` from `langchain-tavily`, set up in one line |

## Tech stack

| Tool | Purpose |
|---|---|
| LangChain (`create_agent`) | Builds the ReAct agent |
| Ollama + Llama 3.2 | Local language model with tool calling |
| Tavily | Web search API for AI agents |
| uv | Python package and project manager |
| python-dotenv | Loads API keys from `.env` |

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/download), installed and running
- A free [Tavily API key](https://tavily.com/)

## Setup

```bash
git clone https://github.com/Tumuluri007/AI-Agents.git
cd AI-Agents
uv sync
ollama pull llama3.2
```

Create a `.env` file in the project folder:

```
TAVILY_API_KEY=your-key-here
```

`.env` is listed in `.gitignore`, so your key is never uploaded.

## Run it

```bash
uv run main.py
```

## Key concepts learned

- **Tools**: Python functions the AI can ask to run
- **Tool calling**: the model returns a structured request (tool name + inputs) instead of a final answer
- **ReAct loop**: think, act (call a tool), observe the result, repeat until done
- **Messages**: `HumanMessage`, `AIMessage` and `ToolMessage` keep track of who said what

## Acknowledgements



