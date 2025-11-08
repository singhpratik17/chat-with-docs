from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from agent.tools import search_db
from langchain.agents.structured_output import ToolStrategy


contact_info_schema = {
    "type": "object",
    "description": "Answer to the Query.",
    "properties": {
        "text_response": {
            "type": "string",
            "description": "Final formatted answer to the query",
        },
        "file_name": {
            "type": "string",
            "description": "The file name where the answer was found. Obtain from source in metadata, only the file name and not the whole path",
        },
    },
    "required": ["text_response", "file_name"],
}


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
        system_prompt="You are an AI Agent which searches the uploaded documents using the provided tools to answer the query. Search the memory first and then the documents before answering. Address the user with name if provided. Be concise and accurate. Use a conversational tone.",
        checkpointer=InMemorySaver(),
        response_format=ToolStrategy(contact_info_schema),
    )

    return agent


def invoke_agent(agent, query: str, thread_id: str = "1"):
    return agent.invoke(
        {"messages": [{"role": "user", "content": query}]},
        {"configurable": {"thread_id": thread_id}},
    )
