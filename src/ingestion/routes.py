from fastapi import APIRouter, Request, Depends, UploadFile
from .ingest import ingest


def get_vector_store(request: Request):
    return request.app.state.vector_store


ingestion_router = APIRouter(prefix="/ingest", dependencies=[Depends(get_vector_store)])


@ingestion_router.post("/files")
async def ingest_files(
    uploads: list[UploadFile], vector_store=Depends(get_vector_store)
):
    print(f"Uploads: {uploads}")
    file_paths = [file.filename for file in uploads]
    print(f"file_paths: {file_paths}")
    res = await ingest(file_paths=file_paths, vector_store=vector_store)
    print("res", res)
    return f"Uploaded {file_paths}"
