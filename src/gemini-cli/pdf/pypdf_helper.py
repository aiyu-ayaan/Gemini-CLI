from PyPDF2 import PdfReader
from rich import console
import logging
from concurrent.futures import ThreadPoolExecutor

console = console.Console()

# logging.basicConfig(level=logging.INFO)
# Disable all logging
logging.disable(logging.CRITICAL)


class PyPdfHelper:
    def __init__(self, path: str):
        """Initializes the PyPdfHelper class to read PDF files using PyPDF2 library
        Args:
            path (str): Path to the PDF file
        """
        try:
            self.path = path
            self.reader = PdfReader(path)
        except Exception as e:
            logging.error('Error reading PDF file: %s', e)
            raise

    def _extract_page_text(self, page_num: int) -> str:
        try:
            return self.reader.pages[page_num].extract_text()
        except Exception as e:
            logging.error('Error extracting text from page %d: %s', page_num, e)
            return ""

    def get_text(self, start: int = 0, end: int = None) -> str:
        """Extracts text from the PDF file from the given start and end page numbers
        Args:
            start (int, optional): Start page index. Default to 0.
            end (int, optional): End page index. Defaults to None.
        Returns:
            str: Extracted text from the PDF file
        """
        try:
            end = end if end is not None else self.reader.getNumPages()
            pages = range(start, end)

            with ThreadPoolExecutor() as executor:
                texts = executor.map(self._extract_page_text, pages)

            return "".join(texts)
        except Exception as e:
            logging.error('Error reading PDF file: %s', e)
            raise
