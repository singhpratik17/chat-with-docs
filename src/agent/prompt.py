async def invoke_agent(agent, query: str, thread_id: str = "1"):
    return await agent.ainvoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": thread_id}},
    )


def extract_text(message):
    if isinstance(message, str):
        return message.strip()
    elif isinstance(message, list):
        return message[0]["text"]


def _normalize_answer(answer: dict) -> dict:
    """Turn "null" strings into None and keep page numbers only for PDF sources."""
    file_name = answer.get("file_name")
    if file_name in (None, "", "null", "N/A"):
        file_name = None
    page = answer.get("page")
    try:
        page = int(page)
    except (TypeError, ValueError):
        page = None
    if not (file_name and file_name.lower().endswith(".pdf")):
        page = None
    return {"message": answer.get("message"), "file_name": file_name, "page": page}


async def ask_gemini(agent, query):
    result = await invoke_agent(agent, query)
    return _normalize_answer(result["structured_response"])
    # print("\nAgent: ", extract_text(result["messages"][-1].content))
    # text_content = result["structured_response"]["text_response"]
    # file_name = result["structured_response"]["file_name"]
    # print(f"\nAgent: {text_content}\n\nsource: {file_name}")
