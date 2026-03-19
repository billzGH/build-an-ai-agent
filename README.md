# Build an AI Agent

A CLI AI agent built with Python and the Google Gemini API, capable of reading, writing, and executing files within a sandboxed working directory.

> ⚠️ **Warning:** Do not give this program to others for them to use! It doesn't have all the security and safety features that a production AI agent would have. This is for learning purposes only.

---

## What It Does

This agent accepts a natural language prompt and uses Gemini to decide which tools to call to fulfill the request. It can:

- List files and directories
- Read file contents
- Write content to files
- Execute Python files

All file operations are sandboxed to a working directory — the agent cannot read or write outside of it.

---

## Project Structure

```file-tree
build-an-ai-agent/
├── main.py                  # Entry point and agent loop
├── prompts.py               # System prompt
├── config.py                # Configuration (e.g. MAX_CHARS)
├── call_function.py         # Function dispatcher and tool registry
├── functions/
│   ├── get_files_info.py    # List directory contents
│   ├── get_file_content.py  # Read file contents
│   ├── write_files.py       # Write content to a file
│   └── run_python_file.py   # Execute a Python file
└── calculator/              # Sample working directory for the agent
    ├── main.py
    ├── tests.py
    └── pkg/
        ├── calculator.py
        └── render.py
```

---

## Setup

### Prerequisites

- Python 3.13+
- [`uv`](https://github.com/astral-sh/uv) package manager
- A [Google AI Studio](https://aistudio.google.com/) account and API key

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/build-an-ai-agent.git
cd build-an-ai-agent
uv sync
```

### Configuration

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY='your_api_key_here'
```

---

## Usage

```bash
uv run main.py "what files are in the root?"
uv run main.py "read the contents of main.py"
uv run main.py "write 'hello world' to hello.txt"
uv run main.py "run tests.py"
```

Add `--verbose` to see token usage and full function call details:

```bash
uv run main.py --verbose "list the contents of the pkg directory"
```

---

## Built With

- [Google Gemini API](https://ai.google.dev/) (`gemini-2.5-flash`)
- [google-genai](https://pypi.org/project/google-genai/) Python SDK
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [uv](https://github.com/astral-sh/uv)

---

## Course

Built as part of the [Boot.dev](https://boot.dev) backend development curriculum.
