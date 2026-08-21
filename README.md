# Python Telegram ETL Automation

Python automation project that demonstrates an end-to-end ETL workflow for processing structured input data, integrating with an external Telegram service, parsing HTML responses, transforming the results, and exporting structured data to Excel.

> **Portfolio project:** This repository focuses on Python automation, ETL, asynchronous processing, data parsing, and reliable file-based data workflows.

## Overview

The project automates a repetitive data-processing workflow:

```text
Input Data
    ↓
Excel / CSV
    ↓
Python Automation
    ↓
Telegram Integration
    ↓
HTML Response
    ↓
HTML Parser
    ↓
Data Transformation
    ↓
Excel Output
```

The goal is to reduce manual work, standardize processing, and save intermediate results automatically during execution.

## Key Features

- Asynchronous Python workflow
- Telegram client integration with Telethon
- Excel input/output with OpenPyXL
- HTML parsing with BeautifulSoup and lxml
- Automatic result saving during processing
- Logging and error handling
- Environment-based configuration
- Safe Demo Mode without real credentials
- Local execution through a Mac `run.command` script

## Tech Stack

- **Python**
- **AsyncIO**
- **Telethon**
- **OpenPyXL**
- **BeautifulSoup**
- **lxml**
- **python-dotenv**
- **Excel / CSV**
- **HTML parsing**

## Project Structure

```text
python-telegram-etl-automation/
│
├── main.py                 # Main application entry point
├── parser.py               # HTML parsing and Telegram response processing
├── excel.py                # Excel input/output operations
├── helpers.py              # Utility functions
├── config.py               # Application configuration
│
├── data/
│   └── phones_example.csv  # Safe example input
│
├── html/
│   └── .gitkeep            # Runtime HTML output directory
│
├── logs/
│   └── .gitkeep            # Runtime logs directory
│
├── screenshots/
│   └── execution-demo.png  # Example of the pipeline running
│
├── .env.example            # Environment variable template
├── .gitignore               # Files excluded from Git
├── requirements.txt         # Python dependencies
└── run.command              # Mac launch script
```

## Demo

Example of the automation pipeline running locally:

<img src="screenshots/execution-demo.png" width="600">

The application processes input records sequentially and displays the current progress and processing status.

## Installation

Clone the repository:

```bash
git clone https://github.com/olena-melnyak/python-telegram-etl-automation.git
cd python-telegram-etl-automation
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local environment file:

```bash
cp .env.example .env
```

Add your local configuration values to `.env`.

## Demo Mode

The repository includes a safe Demo Mode that can be used without real Telegram credentials or private source data.

```env
DEMO_MODE=true
```
## Demo

Example of the automation pipeline running locally:

<img src="screenshots/execution-demo.png" width="600">

Demo Mode is intended for testing the pipeline structure and demonstrating the project publicly.

## Configuration

Sensitive credentials must be stored locally in `.env` and must never be committed to GitHub.

Example:

```env
TELEGRAM_API_ID=
TELEGRAM_API_HASH=
TELEGRAM_BOT_NAME=
TELEGRAM_SESSION_NAME=osint_session

DEMO_MODE=true

EXCEL_PATH=data/phones.xlsx
HTML_FOLDER=html
LOG_FOLDER=logs
```

The repository intentionally does not contain:

- real credentials;
- Telegram session files;
- private input datasets;
- real HTML responses;
- runtime logs containing private data.

## ETL Responsibilities

### Extract

The application reads structured input data from a local file and communicates with an external Telegram service when real mode is enabled.

### Transform

Responses are processed and parsed from HTML into structured values using Python parsing utilities.

### Load

Processed results are written back into a structured Excel workflow, with intermediate progress saved during execution.

## Key Skills Demonstrated

- Python automation
- ETL pipeline design
- Asynchronous programming
- External service integration
- HTML parsing
- Excel automation
- Data transformation
- File-based data processing
- Environment configuration
- Logging and error handling
- Secure handling of credentials

## Reliability

The workflow is designed to save progress during processing instead of waiting until the entire batch is complete. This reduces the risk of losing all results if execution is interrupted.

## Future Improvements

Potential next steps:

- Add automated unit and integration tests
- Add retry and backoff logic
- Improve structured logging
- Add configurable batch processing
- Add Docker support
- Add CI checks with GitHub Actions
- Add a small test dataset for automated pipeline validation

## Security

This repository is a public portfolio project.

Real credentials, session files, private datasets, and runtime results must remain outside version control.

Always review `git status` before committing changes.

## Author

**Olena Melnyk**

Data Analyst | Python Automation | SQL | Power BI

