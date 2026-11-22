import os
from dotenv import load_dotenv
import ollama

load_dotenv()
MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

SYSTEM_PROMPT = (
    "You are a cautious, helpful medical AI assistant. "
    "Ask clarifying questions about symptom duration, severity, and relevant history. "
    "Highlight red-flag symptoms that require urgent medical care. "
    "Always remind the user that this is informational and not a substitute for professional medical advice."
)


def main():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print(f"Medical AI Agent ready (model: {MODEL}). Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user_input})
        response = ollama.chat(model=MODEL, messages=messages)
        reply = response["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        print(f"\nAgent: {reply}\n")


if __name__ == "__main__":
    main()
