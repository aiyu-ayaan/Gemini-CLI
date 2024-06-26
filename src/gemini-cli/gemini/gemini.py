import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

from gemini.youtube_transcript import YoutubeTranscript

console = Console()


class Gemini:
    """Clas to interact with the Gemini API
    """

    def __init__(self, key):
        if key is None or len(key) == 0:
            console.print('❌', 'API key is required', style='bold red')
            exit(1)
        genai.configure(api_key=key)
        self.__model = genai.GenerativeModel('gemini-1.5-flash')

    def ask(self, question: str, max_words: int = 0) -> str | None:
        """Ask a question to the model

        Args:
            question (str): Question to ask
            max_words (int, optional): Word limit. Default to 0.
        Returns:
            str | None: Response from the model
        """
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
            return None
        else:
            markdown = Markdown(response)
            console.print(markdown, style='bold green')
        return response

    def summarize_transcript(self, youtube_url: str, question: str = '', max_words: int = 0) -> str | None:
        """Summarize a transcript from a YouTube video or can answer a question from the transcript

        Args:
            youtube_url (str): link to the YouTube video
            question (str, optional): Question to want to ask. Defaults to ''.
            max_words (int, optional): Word limit. Default to 0.
        Returns:
            str | None: Response from the transcript
        """
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
            return None
        else:
            markdown = Markdown(response)
            console.print(markdown, style='bold green')
        return response

    def generate_response_from_pdf(self, text: str, question: str, max_words: int = 0) -> str | None:
        """Generate a response from the PDF

        Args:
            text (str): Text to generate a response from
            question (str): Question to ask
            max_words (int, optional): Word limit. Default to 0.
        Returns:
            str | None: Response from the PDF
        """
        console.print(f'🐼', f'Generating response from the PDF\n', style='bold blue')
        with console.status('[bold green]Generating response...', spinner='moon'):
            try:
                has_error = False
                question = text + '\n\nSummaries the context as elaborated possible' if len(
                    question) == 0 else text + f'\n\nQuestion: {question}'
                response = self.__model.generate_content(
                    question if max_words == 0 else question + f' Word limit {max_words}'
                ).text
            except Exception as e:
                has_error = True
                response = e

        if has_error:
            console.print('❌', f' Error: {response}', style='bold red')
            return None
        else:
            markdown = Markdown(response)
            console.print(markdown, style='bold green')
        return response
