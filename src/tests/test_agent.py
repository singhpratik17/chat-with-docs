from ingestion.document_loader import propmt_gemini


prompts = [
    "What health services are included in occupational health?",
    "Where is Tax card office? How can I reach them?",
    "Who is this doc from?",
    "Summarise the doc in 3 sentences",
]


def test_invoke_prompt():
    propmt_gemini(prompts[1])
