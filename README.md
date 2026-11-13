
# AI Chatbot using Python, LangChain & Google Gemini

A simple command-line AI chatbot built using Python,
LangChain, and Google's Gemini LLM.

## Features

- Interactive command-line chatbot.
- Powered by Google Gemini Flash.
- Conversation memory using LangChain message history.
- Maintains context across multiple user queries.
- Secure API key management using environment variables.
- Basic error handling.

## Tech Stack

- Python
- LangChain
- Google Gemini API
- python-dotenv

## Project Structure

AI-Chatbot/
- main.py
- requirements.txt
- .env.example
- .gitignore
- README.md

## Setup Instructions

1. Clone the repository:

   git clone YOUR_REPOSITORY_URL

2. Navigate to the project:

   cd AI-Chatbot

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   Windows:
   venv\Scripts\activate

   Mac/Linux:
   source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

6. Create a .env file and add your Google API key:

   GOOGLE_API_KEY=your_api_key

7. Run the chatbot:

   python main.py

## Usage

Start asking questions directly in the terminal.

Type 'exit' to stop the chatbot.

## Future Improvements

- Add a Streamlit or React-based UI.
- Implement conversation persistence.
- Explore LangGraph for more advanced conversational workflows.
- Add Retrieval-Augmented Generation (RAG).
