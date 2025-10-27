from src.utils.file_loader import load_file


def test_file_loader():
    pdf_file = load_file("/Users/pratik/Downloads/aJQgNGM41tvz2bVdkhAF-receipt.pdf")
    assert pdf_file.metadata["Creator"] == "PDFKit"
    assert pdf_file.metadata["Producer"] == "PDFKit"
