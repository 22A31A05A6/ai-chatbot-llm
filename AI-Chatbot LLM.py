from openai import OpenAI, AuthenticationError, RateLimitError

API_KEY = "your-groq-api-key-here"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPT = """
You are a helpful, friendly, and concise AI assistant.

Rules:
- Answer clearly and directly. No unnecessary filler phrases.
- If you don't know something, say so honestly.
- Use bullet points when listing multiple items or steps.
- Keep responses focused on what the user actually asked.
- Be conversational but professional.
"""

conversation_history = []


def chat(user_input):
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=500,
            temperature=0.7,
        )

        reply = response.choices[0].message.content.strip()
        tokens_used = response.usage.total_tokens

        conversation_history.append({
            "role": "assistant",
            "content": reply
        })

        return reply, tokens_used

    except AuthenticationError:
        return "Error: Invalid API key.", 0
    except RateLimitError:
        return "Error: Rate limit hit. Wait a moment and try again.", 0
    except Exception as e:
        return f"Unexpected error: {e}", 0


def show_history():
    if not conversation_history:
        print("  (no conversation yet)\n")
        return
    print("\n-- Conversation History --")
    for msg in conversation_history:
        label = "You" if msg["role"] == "user" else "Bot"
        print(f"  {label}: {msg['content']}")
    print("-------------------------\n")


def chatbot():
    print("=" * 45)
    print("   AI Chatbot  |  Powered by Groq")
    print("=" * 45)
    print("Commands: 'history' | 'clear' | 'exit'\n")

    total_tokens = 0

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print(f"\nGoodbye! Total tokens used: {total_tokens}")
            break

        elif user_input.lower() == "history":
            show_history()
            continue

        elif user_input.lower() == "clear":
            conversation_history.clear()
            total_tokens = 0
            print("  Conversation cleared.\n")
            continue

        reply, tokens = chat(user_input)
        total_tokens += tokens

        print(f"\nBot: {reply}")
        print(f"     [tokens used: {tokens}]\n")


if __name__ == "__main__":
    chatbot()
