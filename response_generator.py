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
            ]

        }

    def generate_response(self,intent):
        responses = self.response.get(
            intent,
            self.response["unknown"]
        )
        return random.choice(responses)
if __name__ == "__main__":

    generator = ResponseGenerator()

    test_intents = [
        "greeting",
        "name",
        "capabilities",
        "thanks",
        "goodbye",
        "unknown"
    ]

    for intent in test_intents:
        response = generator.generate_response(intent)

        print(f"{intent}: {response}")