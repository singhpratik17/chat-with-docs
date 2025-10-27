import pdfplumber

def load_file(file_path: str):
    with pdfplumber.open(file_path) as pdf:
        return pdf