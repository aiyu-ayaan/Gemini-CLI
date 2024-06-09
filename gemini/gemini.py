import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(override=True)


class Gemini:
    def __init__(self):
        google_api_key = os.getenv('GEMINI_KEY')
        genai.configure(api_key=google_api_key)
        self.__model = genai.GenerativeModel('gemini-1.5-flash')

    def ask(self, question: str):
        print('Thinking...')
        return self.__model.generate_content(question).text
