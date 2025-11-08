from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from agent.tools import search_db


def init_agent():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1,
        max_tokens=None,
        verbose=False,
        timeout=None,
        max_retries=1,
        model_kwargs={"handle_parsing_errors": True},
    )

    tools = [search_db]

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt="You are an AI Agent which which searches the uploaded documents using the given tools to answer the query. Be concise and accurate.",
        checkpointer=InMemorySaver(),
    )

    return agent


def invoke_agent(agent, query: str, thread_id: str = "1"):
    return agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": thread_id}},
    )
