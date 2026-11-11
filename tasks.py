"""Task logic and file storage for the Task Manager."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "tasks.json"


def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if unavailable."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)