"""CLI entry point for the Telegram + Excel automation pipeline."""

import asyncio

from config import (
    API_HASH,
    API_ID,
    DEMO_MODE,
    SESSION_NAME,
    validate_runtime_config,
)
from excel import process_excel


async def main() -> None:
    validate_runtime_config()

    if DEMO_MODE:
        print("DEMO_MODE=True — no Telegram connection will be made.")
        await process_excel(None)
        return

    from telethon import TelegramClient

    client = TelegramClient(SESSION_NAME, int(API_ID), API_HASH)
    print("Connecting to Telegram...")
    await client.start()
    print("Telegram connected.")

    try:
        await process_excel(client)
    finally:
        await client.disconnect()
        print("Connection closed.")


if __name__ == "__main__":
    asyncio.run(main())
