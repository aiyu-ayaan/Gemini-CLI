from rich import console
import gemini as gemini
import argparse
import sys
from version import InfoAction

console = console.Console()


def create_key_file():
    """Create a key file if it does not exist
    """
    try:
        print('Generating key file from  https://ai.google.dev/gemini-api/docs/api-key')
        api_key = input('Enter your key: ')
        while len(api_key) == 0:
            console.print('Key cannot be empty.\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                          style='bold red')
            api_key = input('Enter your key: ')
        with open('../../key.txt', 'w') as f:
            f.write(api_key)
            f.close()
            console.print('Key file created successfully')
    except Exception as e:
        console.print('Error creating key file.',
                      style='bold red')
        exit(1)


def load_key_from_root() -> str:
    """Loads the key from the root

    Returns:
        str: API key
    """
    try:
        with open('../../key.txt', 'r') as f:
            #         check if the key is empty
            if len(f.read()) == 0:
                console.print(
                    'Key cannot be empty.\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                    style='bold red')
                exit(1)
            f.seek(0)
            return f.readline().strip()
    except FileNotFoundError as e:
        create_key_file()
        return load_key_from_root()
    except Exception as e:
        console.print('Error reading key file\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                      style='bold red')
        exit(1)


if __name__ == '__main__':
    """Main function
    """
    # load the key from the root
    key = load_key_from_root()
    parser = argparse.ArgumentParser(description='Gemini CLI')
    parser.add_argument('--question', '-q', type=str, help='Question to ask Gemini')
    parser.add_argument('--word-limit', '-wl', help='Word limit for the response', type=int, default=0)
    parser.add_argument('--info', '-i', action=InfoAction, help='About Gemini CLI')
    parser.add_argument('--youtube', '-yt', type=str, help='YouTube URL to get transcript from')

    # parse the arguments
    args = parser.parse_args()
    question = args.question
    max_words = args.word_limit
    youtube_url = args.youtube

    g = gemini.Gemini(key=key)

    if youtube_url:
        g.summarize_transcript(youtube_url=youtube_url, max_words=max_words, question=question if question else '')
        sys.exit(0)
    # check if the question is empty
    if len(question) == 0:
        print('Question cannot be empty')
        sys.exit(1)
    # create a Gemini instance
    g.ask(question.strip(), max_words)
