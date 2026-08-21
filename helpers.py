"""Small text-processing helpers used by the ETL pipeline."""


def clean_text(text: str) -> str:
    """Remove selected UI symbols and surrounding whitespace."""
    if text is None:
        return ""

    return (
        str(text)
        .replace("👤", "")
        .replace("📱", "")
        .replace("🍼", "")
        .replace("🏠", "")
        .replace("📧", "")
        .replace("🔗", "")
        .strip()
    )


def get_value(lines: list[str], key: str) -> str | None:
    """Return the first line immediately following a given label."""
    for index, line in enumerate(lines):
        if clean_text(line) == key and index + 1 < len(lines):
            return clean_text(lines[index + 1])
    return None
