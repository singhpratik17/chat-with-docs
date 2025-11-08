# import sys
from dotenv import load_dotenv
from agent.agent import init_agent
from agent.prompt import prompt_gemini


def main():
    load_dotenv()
    agent = init_agent()

    print("Hello from chat-with-docs! Type exit to exit")
    while True:
        query = input("Enter your query: ")
        if len(query):
            if query == "exit":
                break
            else:
                prompt_gemini(agent, query)
        else:
            print("The query can't be empty.")


if __name__ == "__main__":
    main()
