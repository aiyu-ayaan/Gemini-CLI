**Gemini CLI Commands**

This Markdown table provides a comprehensive overview of the command-line arguments available for interacting with
Gemini:

| Argument     | Shorthand | Type                         | Description                                                                                                                | Default      |
|--------------|-----------|------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------|
| `question`   | `-q`      | `str`                        | The question you want to ask Gemini. This is a required argument.                                                          | **Required** |
| `word-limit` | `-wl`     | `int`                        | Sets the maximum number of words Gemini should use in its response. A value of 0 indicates no limit.                       | 0            |
| `info`       | `-i`      | `InfoAction` (custom action) | Displays information about the Gemini CLI.                                                                                 |              |
| `youtube`    | `-yt`     | `str`                        | Provides a YouTube URL from which Gemini can extract the transcript and potentially answer questions based on the content. |              |

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
```