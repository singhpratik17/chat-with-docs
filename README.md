# Chat with your docs

An AI agent that answers questions from uploaded documents (HR policies, manuals, guides), citing the source file and page.

# Sample outputs

The examples use public documents stored in [`samples/`](samples/):

- [`migri-information-package-work.pdf`](samples/migri-information-package-work.pdf): the Finnish Immigration Service's information package on residence permits for work ([source](https://migri.fi/documents/5202425/175318957/Information%20package%20-%20Work.pdf/b4e71128-27b9-cae5-300f-b66a52a50fec/Information%20package%20-%20Work.pdf)).
- Three [InfoFinland](https://www.infofinland.fi/en) pages saved as text: [Tax card](https://www.infofinland.fi/en/work-and-enterprise/taxation/tax-card), [Registering as a resident](https://www.infofinland.fi/en/moving-to-finland/registering-as-a-resident) and [Rental home](https://www.infofinland.fi/en/housing/rental-home).

Upload them together:

```bash
curl -X POST http://127.0.0.1:8000/ingest/files \
  -F files=@samples/migri-information-package-work.pdf \
  -F files=@samples/infofinland-tax-card.txt \
  -F files=@samples/infofinland-registering-as-a-resident.txt \
  -F files=@samples/infofinland-rental-home.txt
```

Questions go to `POST /ask-agent/` as `{"msg": "..."}`. Each answer comes back with the file it was drawn from and, for PDFs, the page.

### Can I start working in Finland before my residence permit is approved?

> No, you cannot start working in Finland before your residence permit is approved if you are a citizen from outside the EU. Your right to work depends on the residence permit granted to you.

`file_name`: `migri-information-package-work.pdf` · `page`: `14`

### What are the steps to apply for a residence permit as an employee?

> **Prepare:**
> 1. Check if you need a residence permit (if you are from outside the EU, yes; if from the EU, register your residence).
> 2. Determine which application to fill in based on your work using the Application Finder.
> 3. Learn about the requirements for entry into Finland and for a residence permit.
> 4. Prepare all necessary attachments for your residence permit application.
>
> **Apply:**
>
> 5. Apply for a residence permit in Enter Finland and add the attachments to your application.
> 6. Pay for the application (and for any family member moving to Finland with you).
> 7. Your employer supplements the terms of your employment in your application.
>
> **Prove your identity:**
>
> 8. Book an appointment to prove your identity.
>
> **Follow the processing of the application:**
>
> 9. Follow the processing of the application in Enter Finland.
> 10. If necessary, add more information to your application.

`file_name`: `migri-information-package-work.pdf` · `page`: `3`

### What is the employer's role in the application?

> The employer's role in the employee's residence permit process includes advising the employee on choosing the correct application and encouraging them to apply through Enter Finland. The employer must also deliver the terms of employment, information, and attachments, preferably through Enter Finland for Employers. If they cannot use Enter Finland for Employers, they must provide the necessary information and attachments to the employee using a terms of employment form so the employee can attach them to their application. It's important to note that the employer cannot apply for a residence permit on behalf of the employee.

`file_name`: `migri-information-package-work.pdf` · `page`: `10`

### What happens if I don't show my tax card to my employer?

> If you do not show your tax card to your employer, they will deduct 60% of your salary as taxes.

`file_name`: `infofinland-tax-card.txt` · `page`: `null` (text files have no pages)

### Why is Halloween celebrated?

> I am sorry, but I cannot answer your question about why Halloween is celebrated as this information is not available in the documents I have access to. My documents primarily focus on information regarding residence permits, working in Finland, and rental homes.

`file_name`: `null` · `page`: `null`

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