# PDF Processing Pipeline

A robust PDF processing pipeline using LLMWhisperer for high-quality text extraction.

## Features

- High-quality PDF text extraction with layout preservation

## Setup

1. Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Mac/Linux
# or
.\.venv\Scripts\activate  # On Windows
```

2.Install requirements:

```bash
pip install -r requirements.txt
```

3.Create a `.env` file with your API key:

LLMWHISPERER_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

## Project Structure

.
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── main.py               # Main processing script
├── pdfs/                 # Input PDF directory (Create this folder in root)
    └── extracted_content/    # Processed output

## Usage

Simple directory processing:

```bash
python main.py ./pdfs
```

## Output Format

The script generates one type of output for each processed PDF:

Text file (`.txt`):

- Raw extracted text with preserved layout

## Requirements

- Python 3.8+
- llmwhisperer-client

## License

MIT
