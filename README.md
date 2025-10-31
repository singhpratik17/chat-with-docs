# Chat with your docs

An AI agent that can answer questions from internal documents (HR policies, manuals, guides).

# MVP Outputs:

### Uploaded pdf: sample document

### Sample prompt 1
```
src/tests/test_agent.py

HumanMessage : Summarise the doc in 3 sentences

AIMessage : 

ToolMessage : [retrieved chunks removed]

AIMessage : [removed]

```

### Sample prompt 2
```
src/tests/test_agent.py

HumanMessage : Where is Tax card office? How can I reach them?

AIMessage : 

ToolMessage : [retrieved chunks removed]

AIMessage : The Tax card office is located at Hämeentie 15. You can also reach them by calling +35829497050. If you have online banking details, you can create a tax card through Mytax services.
```

### Sample prompt 3

```
src/tests/test_agent.py

HumanMessage : Why is Halloween celebrated?

AIMessage : 

ToolMessage : [retrieved chunks removed]

AIMessage : [removed]
```

# Development:

- Project initialized using uv

# Project Structure

```
src/
    ├── main.py
    ├── agent/
    ├── ingestion/
    ├── retrieval/
    └── tests/
pyproject.toml
README.md
```