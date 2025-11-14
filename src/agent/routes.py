from fastapi import APIRouter, Depends, Request
from .prompt import ask_gemini
from pydantic import BaseModel


def get_agent(request: Request):
    return request.app.state.agent


agent_router = APIRouter(prefix="/ask-agent", dependencies=[Depends(get_agent)])


class UserMessage(BaseModel):
    msg: str


@agent_router.post("/")
async def ask_agent(message: UserMessage, agent=Depends(get_agent)):
    return await ask_gemini(agent, query=message.msg)
