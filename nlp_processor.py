import re 

class NLPProcessor:

    def normalize(self ,text):
        text = text.lower()
        text = re.sub(r"[^\w\s]","",text)
        text = re.sub(r"\s+"," ",text).strip()
        return text

    def tokenize(self,text):
        return text.split()

    def detect_intent(self,tokens):
        from intents import INTENTS

        for intent,examples in INTENTS.items():
            for example in examples:
                example_tokens = self.tokenize(self.normalize(example))

                if all(word in tokens for word in example_tokens):
                    return intent
        return "unknown"


if __name__ == "__main__":

    processor = NLPProcessor()

    text = "  HELLO!!!   How are YOU?  "

    normalized_text = processor.normalize(text)
    tokens = processor.tokenize(normalized_text)

    print("Original:", text)
    print("Normalized:", normalized_text)
    print("Tokens:", tokens)
    test_messages = [
        "HELLO!!!",
        "What's your name?",
        "What can you do?",
        "Thank you",
        "Bye",
        "Explain quantum physics"
    ]

    for message in test_messages:

        normalized = processor.normalize(message)
        tokens = processor.tokenize(normalized)
        intent = processor.detect_intent(tokens)

        print("\nMessage:", message)
        print("Normalized:", normalized)
        print("Tokens:", tokens)
        print("Intent:", intent)