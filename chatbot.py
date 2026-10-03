from nlp_processor import NLPProcessor
from response_generator import ResponseGenerator
from ai_response_generator import AIResponseGenerator

class Chatbot:
    def __init__(self):
        self.nlp_processor = NLPProcessor()
        self.response_generator = ResponseGenerator()
        self.ai_response_generator = AIResponseGenerator()

    def get_response(self,user_input):
        normalized_text = self.nlp_processor.normalize(user_input)
        tokens = self.nlp_processor.tokenize(normalized_text)
        intent =self.nlp_processor.detect_intent(tokens)

        if intent=="unknown":
            return self.ai_response_generator.generate_response(user_input)
        
        response = self.response_generator.generate_response(intent)

        return response

