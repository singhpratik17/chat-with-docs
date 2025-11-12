from fastapi import APIRouter, Depends, Request
from .prompt import ask_gemini

agent_router = APIRouter(prefix="/ask-agent")


def get_agent(request: Request):
    return request.app.state.agent


def get_vector_store(request: Request):
    return request.app.state.vector_store


@agent_router.get("/")
async def ask_agent(query: str, agent=Depends(get_agent)):
    return await ask_gemini(agent, query)
