# from pathlib import Path
# from fpdf import FPDF
from src.ingestion.document_loader import ingest

# from src.ingestion.embeddings_generator import generate_embeddings

# def create_valid_test_files(tmp_path: Path) -> list[str]:
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Helvetica", size=12)
#     content = "This is a pdf file created by pytest using FPDF.\n\n\nTesting new line."
#     pdf.write(text=content)
#     pdf.add_page()
#     pdf.write(text="Some random text")
#     pdf.output(str(tmp_path / "dummy_pdf.pdf"))

#     txt_file_path = tmp_path / "dummy_txt.txt"
#     content = "This is a text file created by pytest."

#     with open(txt_file_path, "w") as txt_file:
#         txt_file.write(content)

#     return [str(tmp_path / "dummy_pdf.pdf"), str(txt_file_path)]


# def test_load_pdf_file(tmp_path: Path):
#     file_paths = create_valid_test_files(tmp_path)

#     file_contents = load_files(file_paths)

#     assert len(file_contents) == 2
#     assert file_contents[0].page_content.startswith(
#         "This is a pdf file created by pytest using FPDF."
#     )
#     assert file_contents[0].page_content.endswith("Some random text")
#     assert file_contents[0].metadata["creator"] == "PyPDF"
#     assert file_contents[0].metadata["total_pages"] == 2
#     assert file_contents[1].page_content.endswith("This is a text file created by pytest.")


# def test_load_txt_file(tmp_path: Path):
#     txt_file_path = tmp_path / "dummy_txt.txt"
#     content = "This is a text file created by pytest."

#     with open(txt_file_path, "w") as txt_file:
#         txt_file.write(content)

#     loaded_file_content = load_files(str(txt_file_path))
#     assert len(loaded_file_content) == 1
#     assert loaded_file_content[0].page_content == content


# def test_unsupported_file_format(tmp_path: Path):
#     json_file_path = tmp_path / "dummy_json.json"
#     content = {
#         "creator": "pytest",
#         "description": "This is a json file created by pytest.",
#     }

#     with open(json_file_path, "w") as json_file:
#         json.dump(content, json_file)

#     unsupported_file = load_files(str(tmp_path / "dummy_json.json"))
#     assert unsupported_file == "Unsupported file format."


# def test_file_not_exists(tmp_path: Path):
#     pdf_not_exists = load_files(str(tmp_path / "not_exists.pdf"))
#     assert pdf_not_exists == "Input not a file."

#     txt_not_exists = load_files(str(tmp_path / "not_exists.txt"))
#     assert txt_not_exists == "Input not a file."

#     invalid_dir = load_files(str(tmp_path / "some_dir"))
#     assert invalid_dir == "Input not a file."


def test_ingest():
    out = ingest(
        [
            "samples/migri-information-package-work.pdf",
            "samples/infofinland-tax-card.txt",
        ]
    )
    print(f"Embedded document: {out}")


# def test_generate_embeddings():
#     out = generate_embeddings()
#     print(f"Generated embedding: {out}")
