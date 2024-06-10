import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

from gemini.youtube_transcript import YoutubeTranscript

console = Console()


class Gemini:
    def __init__(self, key):
        if key is None or len(key) == 0:
            console.print('❌', 'API key is required', style='bold red')
            exit(1)
        genai.configure(api_key=key)
        self.__model = genai.GenerativeModel('gemini-1.5-flash')

    def ask(self, question: str, max_words: int = 0):
        console.print(f'🐼', f'Asking: {question}\n', style='bold blue')
        with console.status('[bold green]Generating response...', spinner='moon'):
            try:
                has_error = False
                response = self.__model.generate_content(
                    question if max_words == 0 else question + f' Word limit {max_words}').text

            except Exception as e:
                has_error = True
                response = e

        if has_error:
            console.print('❌', f' Error: {response}', style='bold red')
        else:
            markdown = Markdown(response)
            console.print(markdown, style='bold green')

    def summarize_transcript(self, youtube_url: str, question: str = '', max_words: int = 0):
        console.print(f'🐼', f'Getting transcript from: {youtube_url}\n', style='bold blue')
        with console.status(f'[bold green]{'Generating answer...' if question else 'Generating summary...'}',
                            spinner='earth'):
            try:
                has_error = False
                transcript = YoutubeTranscript.get_transcript(youtube_url)
                if transcript:
                    base_question = 'Summaries this transcript from youtube \n' + transcript
                    q = base_question if len(question) == 0 \
                        else base_question + f'\n\nQuestion: {question}'
                    response = self.__model.generate_content(
                        q if max_words == 0 else q + f' Word limit {max_words}'
                    ).text
                else:
                    has_error = True
                    response = 'No transcript found'
            except Exception as e:
                has_error = True
                response = e
        if has_error:
            console.print('❌', f' Error: {response}', style='bold red')
        else:
            markdown = Markdown(response)
            console.print(markdown, style='bold green')
