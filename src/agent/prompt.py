from agent.agent import invoke_agent


# def extract_text(message):
#     content = message.content
#     if isinstance(content, str):
#         return content.strip()
#     elif isinstance(content, list):
#         # Collect text parts if any
#         texts = [
#             c["text"]
#             for c in content
#             if isinstance(c, dict) and c.get("type") == "text"
#         ]
#         return " ".join(texts).strip()
#     return str(content)


def extract_text(message):
    if isinstance(message, str):
        return message.strip()
    elif isinstance(message, list):
        return message[0]["text"]


async def prompt_gemini(agent, query):
    # messages = invoke_agent(agent, query=query)["messages"]
    # for msg in messages:
    #     print(f"\n{type(msg).__name__} : { extract_text(msg)}")
    result = await invoke_agent(agent, query=query)
    # print("\nAgent: ", extract_text(result["messages"][-1].content))
    text_content = result["structured_response"]["text_response"]
    file_name = result["structured_response"]["file_name"]
    print(f"\nAgent: {text_content}\n\nsource: {file_name}")
