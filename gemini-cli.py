from rich import console

import gemini as gemini
import argparse
import sys
from version import InfoAction

console = console.Console()


def load_key_from_root():
    try:
        with open('key.txt', 'r') as f:
            #         check if the key is empty
            if len(f.read()) == 0:
                console.print(
                    'Key cannot be empty.\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                    style='bold red')
                exit(1)
            f.seek(0)
            return f.readline().strip()
    except FileNotFoundError as e:
        console.print('Key file not found\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                      style='bold red')
        exit(1)
    except Exception as e:
        console.print('Error reading key file\nLink to generate key https://ai.google.dev/gemini-api/docs/api-key',
                      style='bold red')
        exit(1)


if __name__ == '__main__':
    # load the key from the root
    key = load_key_from_root()
    parser = argparse.ArgumentParser(description='Gemini CLI')
    parser.add_argument('--question', '-q', type=str, help='Question to ask Gemini')
    parser.add_argument('--word-limit', '-wl', help='Word limit for the response', type=int, default=0)
    # parser.add_argument('--version', '-v', action='version', version=f'%(prog)s {__version__}', help='Show version')
    parser.add_argument('--info', '-i', action=InfoAction, help='About Gemini CLI')

    # parse the arguments
    args = parser.parse_args()
    question = args.question.strip()
    max_words = args.word_limit
    # check if the question is empty
    if len(question) == 0:
        print('Question cannot be empty')
        sys.exit(1)
    # create a Gemini instance
    g = gemini.Gemini(key=key)
    g.ask(question, max_words)
