# Week 5: Advanced RAG & Agentic Workflows

## Focus

This week focuses on improving retrieval quality and moving from a fixed RAG pipeline to an agentic workflow that can plan, use tools, validate results, and retry when needed.

Key topics:

- Advanced RAG patterns
- Query rewriting
- Multi-step retrieval
- Tool-using agents
- Web search integration
- SQL or database lookup
- Response validation
- Self-correction loops

## Weekly Project

### Self-Correcting Research Agent with Tool Access

Build an agent workflow that takes a complex user query, decides which tools to use, gathers information from external and internal sources, checks whether the retrieved information is sufficient, retries with improved queries when needed, and returns a structured final report.

## What Needs to Be Done

- Accept a complex research-style question from the user
- Break the task into smaller retrieval steps
- Connect the agent to one or more tools
- Evaluate whether the retrieved results answer the original intent
- Rewrite the search query when the first attempt is weak or incomplete
- Combine verified findings into a final response
- Return a readable report with sources or evidence
- Handle no-result, low-confidence, and conflicting-result cases gracefully

## Functional Expectations

The project should:

- Support at least two tool types
- Show a clear reasoning flow or execution steps
- Retry retrieval when the first result set is not good enough
- Keep the final answer grounded in retrieved evidence
- Include source references, links, or query results where relevant
- Avoid unsupported claims when evidence is missing

## Recommended Tool Access

For a simple and practical version of this project, start with tools that are easy to connect and easy to validate.

Recommended tools:

- Web search for external research
- Local document retrieval for internal PDFs or text files
- Calculator or Python utility functions for simple analysis

Suggested rules:

- Keep tool access read-only
- Limit tools to approved sources only
- Log which tool was used for each step
- Return evidence from the tool in the final report

## Suggested Folder Structure

```text
Week 5/
├── ProjectREADME.md
├── app.py
├── requirements.txt
├── data/
├── reports/
├── src/
│   ├── config.py
│   ├── agent.py
│   ├── planner.py
│   ├── evaluator.py
│   ├── query_rewriter.py
│   ├── report_generator.py
│   ├── tools/
│   │   ├── web_search.py
│   │   ├── document_search.py
│   │   ├── sql_client.py
│   │   └── calculator.py
│   └── utils.py
└── tests/
```

## Deliverables

- Working research agent application
- Tool integrations for retrieval
- Self-correction or retry mechanism
- Final report generation
- Clear setup instructions

## Suggested Workflow

1. Receive the user query
2. Plan the retrieval steps
3. Call the selected tool
4. Check whether the result is useful
5. Rewrite the query if needed
6. Retrieve again
7. Summarize the validated findings
8. Generate the final report

## Stretch Ideas

- Add memory across research sessions
- Rank tools before choosing one
- Add citation scoring or confidence scoring
- Support export to Markdown or PDF
