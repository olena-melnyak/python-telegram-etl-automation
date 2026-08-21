"""Response parsing layer for the Telegram automation pipeline.

The public repository intentionally demonstrates parsing of non-sensitive
metadata only. Real-world integrations should use only authorized data
sources and must not expose personal data in logs, fixtures, or repositories.
"""

import asyncio
import os
from pathlib import Path

from bs4 import BeautifulSoup

from config import BOT_NAME, DEMO_MODE, HTML_FOLDER


async def process_phone(client, phone: str, debug: bool = False) -> dict:
    """Run one input through the configured adapter and return safe metadata.

    In DEMO_MODE no network request is made. In live mode this function sends
    the input to the configured Telegram bot and stores the returned HTML as a
    local artifact. The public example extracts only a generic status field.
    """
    if DEMO_MODE:
        return {
            "phone": phone,
            "status": "demo",
            "source": "local_demo",
        }

    await client.send_message(BOT_NAME, phone)
    await asyncio.sleep(2)

    message = (await client.get_messages(BOT_NAME, limit=1))[0]

    if message.buttons:
        try:
            await message.click(0)
        except Exception:
            pass

    await asyncio.sleep(2)
    message = (await client.get_messages(BOT_NAME, limit=1))[0]

    if message.file is None:
        return {
            "phone": phone,
            "status": "no_file",
            "source": "telegram",
        }

    Path(HTML_FOLDER).mkdir(parents=True, exist_ok=True)
    path = await message.download_media(
        file=os.path.join(HTML_FOLDER, f"{phone}.html")
    )

    with open(path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")

    text = "\n".join(line.strip() for line in soup.get_text("\n").splitlines() if line.strip())

    return {
        "phone": phone,
        "status": "received",
        "source": "telegram",
        "html_size": len(text),
    }
