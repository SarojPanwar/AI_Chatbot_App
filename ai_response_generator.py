from google import genai
import os
import time
from dotenv import load_dotenv
from google.genai import errors # type: ignore
load_dotenv()

class AIResponseGenerator:
    def __init__(self):
        api_key=os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set in the .env file.")
        
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.5-flash-lite"

    def generate_response(self,user_input):

        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                model = self.model,
                contents=user_input
                )

                if response and response.text:
                    return response.text
                return "I couldn't generate a response right now."

            except errors.ServerError:
                if attempt < max_retries-1:
                    time.sleep(2 ** attempt)
                else:
                    return(
                        "Sorry, the AI service is temporarily unavaible."
                        "Please try again in a moment."

                    )
            except errors.clientError as error:
                return(
                    "Sorry, I couldn't process that request right now."
                )
            except Exception:
                return(
                    "Something went wrong while connecting to the AI service."
                )
        
    

