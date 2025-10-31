from ingestion.document_loader import propmt_gemini


def test_invoke_prompt():
    propmt_gemini("Where is kela?")
