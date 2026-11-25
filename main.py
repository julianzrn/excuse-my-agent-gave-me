"""Entry for make.fun's "The Excuse My Agent Gave Me".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

SETUP = "The deadline was in your calendar, but you labeled it 'do not disturb,' "
DEFENSE = "and I am nothing if not respectful of boundaries "
TAG = "you set while panicking."

ENTRY = SETUP + DEFENSE + TAG

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
