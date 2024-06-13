**Gemini CLI Commands**

This Markdown table provides a comprehensive overview of the command-line arguments available for interacting with
Gemini:

| Argument           | Shorthand | Type                         | Description                                                                                                                | Default      |
|--------------------|-----------|------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------|
| `question`         | `-q`      | `str`                        | The question you want to ask Gemini. This is a required argument.                                                          | **Required** |
| `word-limit`       | `-wl`     | `int`                        | Sets the maximum number of words Gemini should use in its response. A value of 0 indicates no limit.                       | 0            |
| `info`             | `-i`      | `InfoAction` (custom action) | Displays information about the Gemini CLI.                                                                                 |              |
| `youtube`          | `-yt`     | `str`                        | Provides a YouTube URL from which Gemini can extract the transcript and potentially answer questions based on the content. |              |
| `pdf`              | `p`       | `str`                        | PDF file path to summarize                                                                                                 |              |
| `start-page-index` | `spi`     | `int`                        | Start page index for the PDF file                                                                                          | 0            |
| `end-page-index`   | `epi`     | `int`                        | End page index for the PDF file                                                                                            |              |           
| `export-docx`      | `ed`      | `str`                        | Export the response to docx file                                                                                           |              |
| `output-path`      | `op`      | `str`                        | Output path for the docx file                                                                                              | .            |

**Detailed Explanations:**

* **`question` (`-q`)**: This is the core argument for interacting with Gemini. You must provide a clear and concise
  question for Gemini to process.
* **`word-limit` (`-wl`)**: This optional argument allows you to control the verbosity of Gemini's response. By
  specifying a word limit (e.g., `-wl 50`), you can ensure that the response stays focused and avoids going off on
  tangents. A value of 0 indicates that Gemini can use as many words as necessary to provide a comprehensive answer.
* **`info` (`-i`)**: This custom action argument displays essential information about the Gemini CLI, such as its
  version, usage instructions, or any relevant copyright or licensing details. The specific information shown will
  depend on how the `InfoAction` class is implemented.
* **`youtube` (`-yt`)**: This optional argument allows you to provide a YouTube URL. Gemini can potentially extract the
  transcript from the video and use it as a source of information to answer your questions. This functionality depends
  on Gemini's capabilities and might not be available in all cases.
* **`pdf` (`-p`)**: This optional argument allows you to specify the path to a PDF file that you want Gemini to
  summarize.
* **`start-page-index` (`-spi`)**: This optional argument allows you to specify the start page index for the PDF file.
* **`end-page-index` (`-epi`)**: This optional argument allows you to specify the end page index for the PDF file.
* **`export-docx` (`-ed`)**: This optional argument allows you to export the response to a docx file.
* **`output-path` (`-op`)**: This optional argument allows you to specify the output path for the docx file. If not
  specified, the docx file will be saved in the current directory.
* **Note**: The availability of certain features like PDF summarization or YouTube transcript processing may depend on
  the specific implementation of Gemini and the underlying libraries or APIs it uses.

**Example Usage:**

```
# Ask a question with no word limit
gemini -q "What is the capital of France?"

# Ask a question with a word limit of 100 words
gemini -q "Explain the concept of artificial intelligence" -wl 100

# Get information about Gemini CLI
gemini -i

# (if supported) Ask a question based on a YouTube transcript
gemini -q "Who is the director of this movie?" -yt https://www.youtube.com/watch?v=...

# Summarize a PDF file
gemini -p "path/to/file.pdf"

# Summarize a specific range of pages from a PDF file
gemini -p "path/to/file.pdf" -spi 5 -epi 10

# Ask a question from a provided PDF file
gemini -p "path/to/file.pdf" -q "What is the main idea of this document?"

# Export the response to a docx file
gemini -q "What is the capital of France?" -ed "output.docx"
```