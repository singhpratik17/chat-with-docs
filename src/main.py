import sys
from dotenv import load_dotenv
from src.agent.agent import init_agent
from src.agent.prompt import prompt_gemini


def main():
    load_dotenv()
    agent = init_agent()

    print("Hello from chat-with-docs!")

    if len(sys.argv) < 2:
        print("Usage: uv run src/main.py '<your prompt here>'")
        sys.exit(1)
    prompt = sys.argv[1]

    prompt_gemini(agent, prompt)


if __name__ == "__main__":
    main()
