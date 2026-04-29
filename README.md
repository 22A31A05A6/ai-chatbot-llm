# AI Chatbot using LLM API

A conversational AI chatbot built in Python using the **Groq LLM API** (Meta's Llama 3.3 70B model). The chatbot supports multi-turn conversations, maintains context across the session, and uses prompt engineering to control response quality.

---

## Features

- Multi-turn conversation with full memory across the session
- Prompt engineering using a structured system prompt
- Specific error handling for API authentication and rate limit failures
- Session commands: `history`, `clear`, `exit`
- Token usage tracking per response

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Groq API | LLM inference (free, no credit card) |
| Llama 3.3 70B | Underlying language model by Meta |
| OpenAI SDK | API client (Groq is OpenAI-compatible) |

---

## How to Run

**Step 1 — Install dependencies**
```bash
pip install openai
```

**Step 2 — Add your Groq API key**

Get a free key from [console.groq.com](https://console.groq.com) — no credit card needed.

Open `chatbot.py` and paste your key on line 4:
```python
API_KEY = "your-groq-api-key-here"
```

**Step 3 — Run the chatbot**
```bash
python chatbot.py
```

---

## Demo

```
=============================================
   AI Chatbot  |  Powered by Groq (Free)
=============================================
Commands: 'history' | 'clear' | 'exit'

You: what is machine learning?

Bot: Machine learning is a branch of AI where systems learn 
from data to make predictions or decisions without being 
explicitly programmed. Key types include:
- Supervised learning (labeled data)
- Unsupervised learning (finds patterns)
- Reinforcement learning (learns from feedback)
     [tokens used: 187]

You: give me an example

Bot: A great example is email spam detection. The model is 
trained on thousands of emails labeled "spam" or "not spam". 
It learns patterns — certain words, senders, structure — and 
then classifies new emails automatically.
     [tokens used: 243]
```

---

## Project Structure

```
ai-chatbot-llm/
└── chatbot.py       # Main chatbot with all logic
└── README.md        # Project documentation
```

---

## Key Concepts Demonstrated

- **LLM API Integration** — calling Groq's API and parsing responses
- **Prompt Engineering** — system prompt controls model persona and behavior
- **Conversation Memory** — full message history sent each API call for context
- **Error Handling** — specific handling for AuthenticationError and RateLimitError

---

## Author

**Samuel Guttula**  
B.Tech Computer Science — Pragati Engineering College  
[LinkedIn](https://www.linkedin.com/in/samuel-guttula/) • [GitHub](https://github.com/22A31A05A6)
