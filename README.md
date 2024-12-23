# Tidy-mac

A Python utility for automatically organizing and renaming screenshot files on macOS using AI-powered content detection.

## Overview

Tidy-mac streamlines the process of managing the countless screenshots that accumulate on macOS systems. It uses OpenAI's Vision API to analyze screenshot contents and generate meaningful filenames, making it easier to find and organize your screenshots quickly and efficiently.

## Features

* Automatically analyzes screenshot contents using GPT-4 Vision API
* Generates descriptive, filesystem-safe filenames based on image content
* Processes all screenshots in a specified directory
* Outputs `mv` commands for review before executing any changes
* Preserves original files until user confirms renaming

## Prerequisites

* Python 3.6+
* OpenAI API key
* Required Python packages:

```bash
openai
python-dotenv
```

## Installation

Clone the repository:

```bash
git clone https://github.com/augustweinbren/tidy-mac.git
cd tidy-mac
```

Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Unix/macOS
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file in the project directory and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script by providing the directory containing your screenshots:

```bash
python tidy-mac.py ~/Desktop
```

The script will:

Scan the specified directory for files matching "Screenshot*.png"
Analyze each screenshot's content using GPT-4 Vision
Generate appropriate filenames based on the content
Output mv commands for each file

Example output:

```bash
mv '/Users/username/Desktop/Screenshot 2024-01-23 at 15.30.45.png' '/Users/username/Desktop/code_editor_python.png'
mv '/Users/username/Desktop/Screenshot 2024-01-23 at 15.31.12.png' '/Users/username/Desktop/browser_documentation.png'
```

## Safety Notes

The script generates mv commands but doesn't execute them automatically
This allows you to review the proposed changes before applying them
Always ensure you have backups of important files before running batch renaming operations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

Built using OpenAI's GPT-4 Vision API
Inspired by the need to manage an ever-growing collection of screenshots on my macOS computer

## Future Improvements

### Performance

In the future the script will utilize concurrent processing to handle multiple screenshots simultaneously using Python's asyncio
