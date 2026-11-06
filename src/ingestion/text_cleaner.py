import re
from collections import Counter, defaultdict
from langchain_core.documents import Document


def _repeated_lines(pages: list[Document]) -> set[str]:
    """Short lines that appear on at least half the pages of a file (headers, footers, nav labels)."""
    if len(pages) < 3:
        return set()
    counts = Counter()
    for page in pages:
        counts.update(
            {
                line.strip()
                for line in page.page_content.splitlines()
                if 0 < len(line.strip()) <= 40
            }
        )
    return {line for line, n in counts.items() if n >= len(pages) / 2}


def _clean(text: str, drop: set[str]) -> str:
    lines = [line for line in text.splitlines() if line.strip() not in drop]
    text = "\n".join(lines)
    # Re-join words hyphenated across line breaks: "require-\nments" -> "requirements"
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)
    return " ".join(text.split())


def clean_text(documents: list[Document]) -> dict:
    """Clean langchain documents and drop pages left empty.

    Returns the cleaned documents and the full cleaned text per source file.
    """
    by_source = defaultdict(list)
    for doc in documents:
        by_source[doc.metadata["source"]].append(doc)

    cleaned_documents = []
    file_contents = {}

    for source, pages in by_source.items():
        drop = _repeated_lines(pages)
        texts = []
        for page in pages:
            page.page_content = _clean(page.page_content, drop)
            if page.page_content:
                cleaned_documents.append(page)
                texts.append(page.page_content)
        file_contents[source] = " ".join(texts)

    return {"cleaned_documents": cleaned_documents, "file_contents": file_contents}
