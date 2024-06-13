import pypandoc as pydoc
import subprocess
from rich import console

console = console.Console()


def _is_pandoc_installed():
    """Check if Pandoc is installed
    Returns:
        bool: True if Pandoc is installed, False otherwise
    """
    try:
        output = subprocess.check_output(['pandoc', '--version'])
        return True
    except FileNotFoundError:
        return False


def export_md_to_docx(input_text: str, file_name='output.docx', output_file_path: str = '.'):
    """Export Markdown text to docx file
    Args:
        input_text (str): Markdown text
        file_name (str): Name of the output docx file. Default to 'output.docx'.
        output_file_path (str): Path to the output docx file. Default to current directory.
    """
    # Check if Pandoc is installed
    if not _is_pandoc_installed():
        console.log("Pandoc is not installed. Installing Pandoc is required to export to docx format.")
        try:
            console.log("Installing Pandoc...", style="bold")
            pydoc.download_pandoc()
            console.log("Pandoc installation complete.")
        except Exception as e:
            console.log(f"Error installing Pandoc: {e}\nPlease install Pandoc manually and try again.",
                        style="bold red")
            return None

    # check output file path end with / or not if yes then remove it
    if output_file_path.endswith('/'):
        output_file_path = output_file_path[:-1]

    # check filename ends with .docx or not if not then add it
    if not file_name.endswith('.docx'):
        file_name = file_name + '.docx'
    # Convert and save the output to the specified file
    try:
        with console.status("Exporting to docx...", spinner="dots"):
            pydoc.convert_text(input_text, 'docx', format='md', outputfile=f'{output_file_path}/{file_name}')
        console.log(f"Markdown text exported to docx: {output_file_path}/{file_name}", style="bold green")
    except Exception as e:
        console.log(f"Error converting to docx: {e}", style="bold red")
        return None
