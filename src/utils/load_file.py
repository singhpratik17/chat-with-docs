import pdfplumber
from pathlib import Path


def load_file(file_path: str) -> str:
    """Loads a pdf or txt file and returns contents of the file or errors as str."""
    if not Path(file_path).is_file():
        return "Input not a file."

    if file_path.endswith(".pdf"):
        try:
            with pdfplumber.open(file_path) as pdf:
                contents = "".join(
                    [
                        page.extract_text_simple(x_tolerance=3, y_tolerance=3)
                        for page in pdf.pages
                    ]
                )
                return contents

        except Exception as e:
            return f"Error loading pdf file {e}"

    elif file_path.endswith(".txt"):
        try:
            with open(file_path) as txt_file:
                contents = txt_file.read()
                return contents
        except Exception as e:
            return f"Error loading txt file {e}"
    else:
        return "Unsupported file format."
