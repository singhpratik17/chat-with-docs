from agent.agent import invoke_agent


def extract_text(message):
    content = message.content
    if isinstance(content, str):
        return content.strip()
    elif isinstance(content, list):
        # Collect text parts if any
        texts = [
            c["text"]
            for c in content
            if isinstance(c, dict) and c.get("type") == "text"
        ]
        return " ".join(texts).strip()
    return str(content)


def prompt_gemini(agent, query):
    messages = invoke_agent(agent, query=query)["messages"]
    for msg in messages:
        print(f"\n{type(msg).__name__} : { extract_text(msg)}")
