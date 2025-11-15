import tempfile
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document
from fastapi import HTTPException


async def load_files(files: list[str]) -> list[Document]:
    """Loads a pdf or txt file and returns list of langchain documents."""

    documents = []

    for file in files:
        filename = file.filename
        extension = filename.split(".")[-1]
        doc = []
        with tempfile.NamedTemporaryFile(delete=True, suffix=extension) as tmp:
            content = await file.read()
            tmp.write(content)
            tmp.flush()
            file_path = tmp.name
            # if not Path(file).is_file():
            #     return f"{file} - Input not a file."
            if extension == "pdf":
                try:
                    loader = PyPDFLoader(
                        file_path=file_path,
                        mode="single",
                        pages_delimiter="\n--THIS IS A CUSTOM END OF PAGE--\n",
                    )
                    doc = await loader.aload()
                except Exception as e:
                    return f"Error loading pdf file {filename} : {e}"
            elif extension == "txt":
                try:
                    loader = TextLoader(file_path=file_path, encoding="utf-8")
                    doc = await loader.aload()
                except Exception as e:
                    return f"Error loading txt file {filename} : {e}"
            else:
                raise HTTPException(
                    status_code=400, detail=f"Unsupported file type: {filename}"
                )
            doc[0].metadata["source"] = filename
            documents.extend(doc)
    return documents
