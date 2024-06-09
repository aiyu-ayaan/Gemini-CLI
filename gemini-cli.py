import gemini as gemini
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gemini CLI')
    parser.add_argument('question', type=str, help='Question to ask Gemini')
    # add optional arguments here"
    parser.add_argument('--word-limit', '-wl', help='Word limit for the response', type=int, default=0)
    # parse the arguments
    args = parser.parse_args()
    question = args.question.strip()
    max_words = args.word_limit
    # check if the question is empty
    if len(question) == 0:
        print('Question cannot be empty')
        sys.exit(1)
    # create a Gemini instance
    g = gemini.Gemini()
    g.ask(question, max_words)
