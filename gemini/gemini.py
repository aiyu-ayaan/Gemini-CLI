import os
from dotenv import load_dotenv
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

load_dotenv(override=True)
console = Console()


class Gemini:
    def __init__(self):
        google_api_key = os.getenv('GEMINI_KEY')
        genai.configure(api_key=google_api_key)
        self.__model = genai.GenerativeModel('gemini-1.5-flash')

    def ask(self, question: str, max_words: int = 0):
        console.print(f'🐼', f'Asking: {question}\n', style='bold blue')
        with console.status('Generating response...') as status:
            try:
                has_error = False
                response = self.__model.generate_content(
                    question if max_words == 0 else question + f'Word limit {max_words}').text

            except Exception as e:
                has_error = True
                response = e

        if has_error:
            console.print('❌', f' Error: {response}', style='bold red')
        else:
            markdown = Markdown(response)
            console.print(markdown, style='bold green')
