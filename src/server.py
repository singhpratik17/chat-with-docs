from functools import lru_cache
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .agent.agent import init_agent
from .chroma_db.client import (
    create_client,
    embeddings_generator,
    create_vector_store,
)
from .config import Settings
from .agent.routes import agent_router
from .ingestion.routes import ingestion_router


@lru_cache
def get_settings():
    return Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting initialization...")
    settings = get_settings()
    chroma_client = create_client()
    embedding_function = embeddings_generator(google_api_key=settings.google_api_key)
    # Chroma Vector Store
    app.state.vector_store = create_vector_store(
        client=chroma_client,
        collection_name="test_2",
        embedding_function=embedding_function,
    )
    # Gemini Agent
    app.state.agent = init_agent(
        google_api_key=settings.google_api_key, vector_store=app.state.vector_store
    )
    print("Initialization Complete...")

    yield
    print("Application shutting down.")


app = FastAPI(title="Chat with docs api server", lifespan=lifespan)

app.include_router(agent_router)
app.include_router(ingestion_router)
