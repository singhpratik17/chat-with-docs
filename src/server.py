from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncio
from agent.agent import init_agent
from chroma_db.client import create_client, embeddings_generator


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.agent = await asyncio.to_thread(init_agent)
    app.state.embeddingsGenerator = await asyncio.to_thread(embeddings_generator)
    app.state.chroma_client = await asyncio.to_thread(create_client)


app = FastAPI(lifespan=lifespan)
