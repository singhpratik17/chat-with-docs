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


async def ask_gemini(agent, query):
    result = await invoke_agent(agent, query)
    return result["structured_response"]
    # print("\nAgent: ", extract_text(result["messages"][-1].content))
    # text_content = result["structured_response"]["text_response"]
    # file_name = result["structured_response"]["file_name"]
    # print(f"\nAgent: {text_content}\n\nsource: {file_name}")
