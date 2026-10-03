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

        user_text = " ".join(tokens)

        best_intent = "unknown"
        best_score = 0

        stop_words ={
            "what", "is", "are", "your", "you",
            "tell", "me", "about", "the",
            "can", "do", "i", "a", "an",
            "how", "who", "which", "please",
            "explain"
        }
       
        for intent,examples in INTENTS.items():
            for example in examples:
                normalized_example = self.normalize(example)
                example_tokens = self.tokenize(normalized_example)

                # 1.Exact phrase matching
                if normalized_example == user_text:
                    return intent

                # 2.keyword matching
                example_keywords =[
                    word for word in example_tokens
                    if word not in stop_words
                ]

                user_keywords =[
                    word for word in tokens
                    if word not in stop_words
                ]
                if not example_keywords:
                    continue
               
                matches = sum(
                    1 for word in example_keywords
                    if word in user_keywords
                )
                score = matches / len(example_keywords)

                if score > best_score:
                    best_score = score
                    best_intent = intent
       
        if best_score>0.5:
            return best_intent

        return "unknown"


