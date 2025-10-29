from src.ingestion.loaders import load_file


def main():
    print("Hello from chat-with-docs!")
    f = load_file("/Users/pratik/Downloads/aJQgNGM41tvz2bVdkhAF-receipt.pdf")
    print(f)


if __name__ == "__main__":
    main()
