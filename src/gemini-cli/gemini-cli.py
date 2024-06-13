from rich import console
import gemini as gemini
import pdf as pdf
import argparse
import sys
from version import InfoAction
from export import export_md_to_docx

console = console.Console()


def create_key_file():
    """Create a key file if it does not exist."""
    try:
        print('Generating key file from https://ai.google.dev/gemini-api/docs/api-key')
        api_key = input('Enter your key: ')
        while len(api_key) == 0:
            console.print('Key cannot be empty.\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                          style='bold red')
            api_key = input('Enter your key: ')
        with open('key.txt', 'w') as f:
            f.write(api_key)
        console.print('Key file created successfully')
    except IOError as e:
        console.print(f'IOError: {e}', style='bold red')
        exit(1)
    except Exception as e:
        console.print(f'Unexpected error: {e}', style='bold red')
        exit(1)


def load_key_from_root() -> str:
    """Loads the key from the root

    Returns:
        str: API key
    """
    try:
        with open('key.txt', 'r') as f:
            # Check if the key is empty
            l_key = f.read().strip()
            if len(l_key) == 0:
                console.print(
                    'Key cannot be empty.\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                    style='bold red')
                exit(1)
            return l_key
    except FileNotFoundError:
        create_key_file()
        return load_key_from_root()
    except IOError as e:
        console.print(f'IOError: {e}', style='bold red')
        exit(1)
    except Exception as e:
        console.print(f'Unexpected error: {e}', style='bold red')
        exit(1)


if __name__ == '__main__':
    """Main function
    """
    # load the key from the root
    key = load_key_from_root()
    parser = argparse.ArgumentParser(description='Gemini CLI')
    parser.add_argument('--question', '-q', type=str, help='Question to ask Gemini', default='')
    parser.add_argument('--word-limit', '-wl', help='Word limit for the response', type=int, default=0)
    parser.add_argument('--info', '-i', action=InfoAction, help='About Gemini CLI')
    parser.add_argument('--youtube', '-yt', type=str, help='YouTube URL to get transcript from')
    parser.add_argument('--pdf', '-p', type=str, help='PDF file path to summarize')
    parser.add_argument('--start-page-index', '-spi', type=int, help='Start page index for the PDF file', default=0)
    parser.add_argument('--end-page-index', '-epi', type=int, help='End page index for the PDF file', default=None)
    parser.add_argument('--export-docx', '-ed', type=str, help='Export the response to docx file')
    parser.add_argument('--output-path', '-op', type=str, help='Output path for the docx file', default='.')

    # parse the arguments
    args = parser.parse_args()
    question = args.question
    max_words = args.word_limit
    youtube_url = args.youtube
    pdf_file_path = args.pdf
    start_page_index = args.start_page_index
    end_page_index = args.end_page_index
    export_docx = args.export_docx
    output_path = args.output_path

    g = gemini.Gemini(key=key)

    # check if the pdf file path is not empty
    if pdf_file_path:
        p = pdf.PyPdfHelper(pdf_file_path)
        console.print('Summarizing PDF...\nThis will take a significant time', style='bold blue')
        text = p.get_text(
            start=start_page_index,
            end=end_page_index
        )
        # console.print(text, style='bold green')
        response = g.generate_response_from_pdf(text, question, max_words)
        if export_docx and len(response) > 0 and response:
            export_md_to_docx(response, export_docx, output_path)
        sys.exit(0)

    if youtube_url:
        response = g.summarize_transcript(youtube_url=youtube_url, max_words=max_words,
                                          question=question if question else '')
        if export_docx and len(response) > 0 and response:
            export_md_to_docx(response, export_docx, output_path)
        sys.exit(0)
    # check if the question is empty
    if len(question) == 0:
        print('Question cannot be empty')
        sys.exit(1)
    # create a Gemini instance
    response = g.ask(question.strip(), max_words)
    if export_docx and len(response) > 0 and response:
        export_md_to_docx(response, export_docx, output_path)
