from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.structured_output import ToolStrategy
from src.agent.tools import make_search_db_tool


agent_answer_format = {
    "type": "object",
    "description": "Answer to the query with reference to the docs.",
    "properties": {
        "message": {
            "type": "string",
            "description": "Final answer to the query",
        },
        "file_name": {
            "type": "string",
            "description": "Source file name",
        },
    },
    "required": ["message", "file_name"],
}


def init_agent(google_api_key, vector_store):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.1,
        max_tokens=None,
        verbose=False,
        timeout=None,
        max_retries=1,
        model_kwargs={"handle_parsing_errors": True},
        google_api_key=google_api_key,
    )

    search_db = make_search_db_tool(vector_store)

    tools = [search_db]

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt="You are an AI Agent which searches the uploaded documents using the provided tools to answer the query. Search the memory first and then the documents before answering. Be concise and accurate.",
        checkpointer=InMemorySaver(),
        response_format=ToolStrategy(agent_answer_format),
    )

    return agent
