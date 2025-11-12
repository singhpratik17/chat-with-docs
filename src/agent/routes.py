from fastapi import APIRouter

from .agent import invoke_agent

router = APIRouter(prefix="/ask-agent")


@router.get()
async def ask_agent():
    await invoke_agent
