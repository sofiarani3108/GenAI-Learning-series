# Week 5: Advanced RAG & Agentic Workflows

## Overview
This project upgrades a standard Retrieval-Augmented Generation (RAG) pipeline into an **Agentic Workflow**. Instead of a fixed pipeline, the application uses an AI agent that can break down complex questions, decide which tools to use, evaluate if the retrieved data is sufficient, self-correct if it fails, and compile a final comprehensive report.

## Features
* **Self-Correcting Agent Loop**: The system doesn't just blindly return the first search result. It evaluates the output and will rewrite its own search query and retry if the initial results are poor.
* **Multi-Step Planning**: The agent breaks complex user questions into 1-3 smaller, manageable sub-tasks.
* **Multi-Tool Access**: The agent has native access to three distinct tools:
  * 🌐 **Web Search**: Fetches real-time internet data using DuckDuckGo.
  * 📄 **Local Document Search**: Performs semantic search on uploaded PDFs using a Pinecone vector database and local `sentence-transformers` embeddings.
  * 🧮 **Calculator**: Safely evaluates mathematical expressions.
* **Streamlit Interface**: A chat-based UI that allows users to upload PDFs and view the agent's internal "thought process" and logs as it reasons through the query.

## Architecture
1. **Planner (`planner.py`)**: Receives the user query and decomposes it into steps.
2. **Tool Execution (`agent.py`)**: Uses Gemini's native tool-calling capabilities to select the correct tool for the current step.
3. **Evaluator (`evaluator.py`)**: Checks if the tool's output sufficiently answers the sub-query.
4. **Query Rewriter (`query_rewriter.py`)**: If the evaluator rejects the output, rewrites the query for better retrieval.
5. **Report Generator (`report_generator.py`)**: Synthesizes all gathered evidence into a final Markdown report.

## Setup & Installation

**1. Clone the repository and navigate to the Week 5 folder:**
```bash
cd "Week 5"
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**3. Environment Variables:**
Create a `.env` file in the root directory and add your API keys:
```env
GOOGLE_API_KEY=your_google_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash

PINECONE_API_KEY=your_pinecone_api_key
PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1
```

**4. Run the Application:**
```bash
streamlit run app.py
```

## How to Test
Once the Streamlit app is running, try asking varied questions to test the different tools:
* **Math**: *"What is 4532 divided by 12?"* (Triggers Calculator)
* **Web**: *"What is the latest news regarding AI today?"* (Triggers Web Search)
* **Documents**: Upload a company PDF and ask: *"What is the company leave policy?"* (Triggers Document Search)
