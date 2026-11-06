# Chat with your docs

An AI agent that can answer questions from internal documents (HR policies, manuals, guides).

# Sample outputs

The examples below use three public pages from [InfoFinland](https://www.infofinland.fi/en), saved as plain text in [`samples/`](samples/):

- [Tax card](https://www.infofinland.fi/en/work-and-enterprise/taxation/tax-card)
- [Registering as a resident](https://www.infofinland.fi/en/moving-to-finland/registering-as-a-resident)
- [Rental home](https://www.infofinland.fi/en/housing/rental-home)

Source: InfoFinland.fi (public information for people moving to Finland), retrieved November 2026.

### Ingest the documents

```bash
curl -X POST http://127.0.0.1:8000/ingest/files \
  -F files=@samples/infofinland-tax-card.txt \
  -F files=@samples/infofinland-registering-as-a-resident.txt \
  -F files=@samples/infofinland-rental-home.txt
```

```json
{"msg": "Uploaded"}
```

### Sample prompt 1: answer drawn from one document

```bash
curl -X POST http://127.0.0.1:8000/ask-agent/ -H 'Content-Type: application/json' \
  -d '{"msg": "I just moved to Finland. How do I get a tax card, and how can I contact the Tax Administration in English?"}'
```

```json
{
  "file_name": "infofinland-tax-card.txt",
  "message": "To get a tax card in Finland after moving there, visit a Tax Administration service point. You will need to estimate your annual income and have a Finnish personal identity code. You can obtain a personal identity code by registering as a resident with the Digital and Population Data Services Agency or at certain Tax Administration service points. To contact the Tax Administration in English, you can call their telephone service at 029 497 050, use the MyTax online service, or visit a tax office."
}
```

### Sample prompt 2: specific fact lookup

```bash
curl -X POST http://127.0.0.1:8000/ask-agent/ -H 'Content-Type: application/json' \
  -d '{"msg": "What happens if I don'"'"'t show my tax card to my employer?"}'
```

```json
{
  "file_name": "infofinland-tax-card.txt",
  "message": "If you do not show your tax card to your employer, they will deduct 60% of your salary as taxes."
}
```

### Sample prompt 3: partial answer, gap stated

The rental page links to a separate page for deposit details, so the agent answers what it can and says what is missing.

```bash
curl -X POST http://127.0.0.1:8000/ask-agent/ -H 'Content-Type: application/json' \
  -d '{"msg": "What do I need to sign a lease and what is a typical rental deposit?"}'
```

```json
{
  "file_name": "infofinland-rental-home.txt",
  "message": "To sign a lease in Finland, lessors typically require a good credit history, sufficient income or funds to pay rent (Kela's benefits are included), and proof of identity. Some landlords may also require you to have registered your right of residence in Finland or possess a residence permit valid for at least one year, as well as a Finnish personal identity code. You may need to provide documents such as your latest payslip, a copy of your taxation decision (showing assets), loan certificates, and a copy of your residence permit or passport if you are not an EU citizen. A credit check is also common, and most landlords require you to take out home insurance. The provided documents do not specify a typical rental deposit amount."
}
```

### Sample prompt 4: off-topic question

```bash
curl -X POST http://127.0.0.1:8000/ask-agent/ -H 'Content-Type: application/json' \
  -d '{"msg": "Why is Halloween celebrated?"}'
```

```json
{
  "file_name": "N/A",
  "message": "I am sorry, but I cannot answer questions about the celebration of Halloween as this information is not available in the documents I have access to. My knowledge is limited to the provided documents, which focus on practical information for living in Finland."
}
```

# Development:

- Project initialized using uv

# Project Structure

```
src/
    ├── main.py
    ├── agent/
    ├── ingestion/
    ├── retrieval/
    └── tests/
pyproject.toml
README.md
```