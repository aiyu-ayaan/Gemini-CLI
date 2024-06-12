import os
from rich.console import Console
import argparse

console = Console()

__name__ = 'gemini-cli'
__version__ = '0.2.0'
__author__ = 'Ayaan'
__author_email__ = 'ayaan35200@gmail.com'
__description__ = 'A CLI for Gemini'
__url__ = 'https://github.com/aiyu-ayaan/Gemini-CLI.git'

__info__ = f'''
Name: {__name__}
Version: {__version__}
Author: {__author__}
Email: {__author_email__}
Description: {__description__}
URL: {__url__}
Peace out! 🐼
'''


class SetUpAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=0, **kwargs):
        super().__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        os.system('pip install -r requirements.txt')
        parser.exit()


class InfoAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=0, **kwargs):
        super().__init__(option_strings, dest, nargs=0, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        console.print(__info__, style='bold cyan')
        parser.exit()
