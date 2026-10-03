import random

class ResponseGenerator:
    def __init__(self):
        self.response ={
            "greeting": [
                "Hello! How can I help you?",
                "Hi! What can I do for you?",
                "Hey! Nice to chat with you."
            ],

            "name": [
                "I'm your AI Assistant.",
                "You can call me AI Assistant."
            ],

            "capabilities": [
                "I can answer questions, have simple conversations, and help you with supported topics.",
                "I can understand several common intents and generate appropriate responses."
            ],

            "help": [
                "Sure! You can ask me about my name, capabilities, or have a simple conversation with me."
            ],
            "thanks":[
                "You're welcome",
                "Happy to help!",
                "Anytime",
            ],
            "goodbye":[
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Take care!"
            ],

            "how_are_you":[
                "I'm doing great! Thanks for asking.",
                "I'm ready to help!"
            ],
            "unknown":[
                "I'm not sure I understand that yet.",
                "Sorry,I don't know how to respond to that.",
                "I haven't learned how to handle that question yet."
            ],
            "purpose": [
                "My purpose is to assist users with questions and simple conversations.",
                "I'm designed to help users by answering questions and having simple conversations."
            ],

            "creator": [
                "I was created as an AI chatbot project using Python, NLP techniques, and Gemini AI.",
                "I was developed as part of an AI chatbot application project."
            ],

            "age": [
                "I don't have an age like a human. I'm an AI assistant.",
                "I'm an AI, so I don't have a human age."
            ],

            "language": [
                "I primarily understand and respond in English.",
                "I currently work mainly with English conversations."
            ],

            "ai": [
                "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.",
                "Artificial Intelligence is technology that allows computers to learn, reason, understand information, and generate responses."
            ],

            "python": [
                "Python is a high-level, general-purpose programming language known for its simple and readable syntax.",
                "Python is widely used for web development, automation, data science, machine learning, and AI."
            ],

            "nlp": [
                "NLP stands for Natural Language Processing. It helps computers understand and process human language.",
                "Natural Language Processing is a branch of AI that allows computers to work with human language."
            ],
            

        }

    def generate_response(self,intent):
        responses = self.response.get(
            intent,
            self.response["unknown"]
        )
        return random.choice(responses)
