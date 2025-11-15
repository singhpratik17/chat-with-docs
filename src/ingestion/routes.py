from fastapi import APIRouter, Request, Depends, UploadFile, File
from .ingest import ingest


def get_vector_store(request: Request):
    return request.app.state.vector_store


ingestion_router = APIRouter(prefix="/ingest", dependencies=[Depends(get_vector_store)])


@ingestion_router.post("/files")
async def ingest_files(
    files: list[UploadFile] = File(...), vector_store=Depends(get_vector_store)
):
    await ingest(files=files, vector_store=vector_store)
    return {"msg": "Uploaded"}
