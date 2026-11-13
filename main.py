import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Validate API key
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found. Please add it to your .env file.")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.7,
    timeout=30,
    max_retries=2,
)

# Initialize conversation history
chat_history = [
    SystemMessage(
        content=(
            "You are a helpful AI assistant. Answer questions clearly and concisely."
        )
    )
]

print("AI Chatbot Started! Type 'exit' to stop.")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Chatbot stopped. Goodbye!")
        break

    if not user_input:
        print("Please enter a valid message.")
        continue

    try:
        # Add user message to conversation history
        chat_history.append(HumanMessage(content=user_input))

        # Get response from LLM
        response = llm.invoke(chat_history)

        # Store AI response in conversation history
        chat_history.append(AIMessage(content=response.content))

        print("AI:", response.content)

    except Exception as e:
        print(f"Error communicating with AI: {e}")
        chat_history.pop()  # Remove failed user message
