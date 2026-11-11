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
        

def add_task(tasks, title):
    """Add a new task. Returns the created task, or None if the title is empty."""
    title = title.strip()
    if not title:
        return None
    new_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": new_id, "title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    return task


def delete_task(tasks, task_id):
    """Delete a task by id. Returns True if it existed."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def mark_done(tasks, task_id):
    """Mark a task as done. Returns True if it existed."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return True
    return False