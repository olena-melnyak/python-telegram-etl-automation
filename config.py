"""Application configuration loaded from environment variables."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
BOT_NAME = os.getenv("TELEGRAM_BOT_NAME", "")
SESSION_NAME = os.getenv("TELEGRAM_SESSION_NAME", "osint_session")

EXCEL_PATH = BASE_DIR / os.getenv("EXCEL_PATH", "data/phones.xlsx")
HTML_FOLDER = BASE_DIR / os.getenv("HTML_FOLDER", "html")
LOG_FOLDER = BASE_DIR / os.getenv("LOG_FOLDER", "logs")

DEMO_MODE = os.getenv("DEMO_MODE", "true").lower() == "true"


def validate_runtime_config() -> None:
    """Validate settings only when real Telegram mode is enabled."""
    if DEMO_MODE:
        return

    missing = []
    if not API_ID:
        missing.append("TELEGRAM_API_ID")
    if not API_HASH:
        missing.append("TELEGRAM_API_HASH")
    if not BOT_NAME:
        missing.append("TELEGRAM_BOT_NAME")

    if missing:
        raise RuntimeError(
            "Missing environment variables: " + ", ".join(missing)
        )
