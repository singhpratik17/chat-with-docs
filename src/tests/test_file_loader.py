import json
from pathlib import Path
from fpdf import FPDF
from src.utils.file_loader import load_file


def test_pdf_file_loader(tmp_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    content = "This is a pdf file created by pytest using FPDF."
    pdf.write(text=content)
    pdf.output(str(tmp_path / "dummy_pdf.pdf"))

    pdf_file_content = load_file(str(tmp_path / "dummy_pdf.pdf"))
    assert pdf_file_content == content


def test_txt_file_loader(tmp_path: Path):
    txt_file_path = tmp_path / "dummy_txt.txt"
    content = "This is a text file created by pytest."

    with open(txt_file_path, "w") as txt_file:
        txt_file.write(content)

    loaded_file_content = load_file(str(txt_file_path))
    assert loaded_file_content == content


def test_unsupported_file_format(tmp_path: Path):
    json_file_path = tmp_path / "dummy_json.json"
    content = {
        "creator": "pytest",
        "description": "This is a json file created by pytest.",
    }

    with open(json_file_path, "w") as json_file:
        json.dump(content, json_file)

    unsupported_file = load_file(str(tmp_path / "dummy_json.json"))
    assert unsupported_file == "Unsupported file format."


def test_file_not_exists(tmp_path: Path):
    pdf_not_exists = load_file(str(tmp_path / "not_exists.pdf"))
    assert pdf_not_exists == "Input not a file."

    txt_not_exists = load_file(str(tmp_path / "not_exists.txt"))
    assert txt_not_exists == "Input not a file."

    invalid_dir = load_file(str(tmp_path / "some_dir"))
    assert invalid_dir == "Input not a file."
