# 🤖 AI Chatbot Application

An interactive AI chatbot built with **Python and Streamlit**, combining basic **Natural Language Processing (NLP)** techniques with **Google Gemini AI** to understand user queries and generate appropriate responses.

## ✨ Features

- 💬 Interactive chat interface
- 🧠 Text normalization and tokenization
- 🎯 Intent-based response generation
- 🤖 Gemini AI fallback for unknown queries
- 🛡️ API error handling
- 🗑️ Clear chat functionality
- 🎨 Custom dark-themed UI

## 🛠️ Tech Stack
- Python
- Streamlit
- NLP (Normalization, Tokenization, Intent Detection)
- Google Gemini AI
- Google GenAI SDK
- python-dotenv

### Conversation Flow

User Input
     ↓
Text Normalization
     ↓
Tokenization
     ↓
Intent Detection
     ↓
Known Intent?
   ↙       ↘
 Yes       No
  ↓         ↓
Predefined  Gemini AI
Response    Response
   ↘       ↙
    Final Response


### 📂 Project Files

- app.py – Handles the Streamlit interface, user input, chat display, and session state.
- chatbot.py – Connects the NLP processor, response generator, and AI response generator.
- nlp_processor.py – Performs text normalization, tokenization, and intent detection.
- intents.py – Contains predefined intents and example user queries.
- response_generator.py – Generates predefined responses for recognized intents.
- ai_response_generator.py – Uses the Gemini API to generate responses for unknown queries.
- requirements.txt – Contains the Python packages required to run the project.
- .env – Stores the Gemini API key securely.

## How to Run

Make sure Python is installed on your system.
Run the following command from the project directory:
Install the required dependencies:
```bash
pip install -r requirements.txt
streamlit run app.py