"""Simple console Task Manager - entry point."""

import tasks

MENU = """
===== Task Manager =====
1. Add task
2. Show tasks
3. Delete task
4. Mark task as done
5. Exit
"""


def read_id(prompt):
    """Read an integer id from the user. Returns None if invalid."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Invalid number.")
        return None


def show_tasks(task_list):
    if not task_list:
        print("No tasks yet.")
        return
    print(f"\n{'ID':<4} {'Status':<8} Title")
    print("-" * 30)
    for t in task_list:
        status = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']:<4} {status:<8} {t['title']}")


def main():
    task_list = tasks.load_tasks()
    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Task title: ")
            if tasks.add_task(task_list, title):
                print("Task added.")
            else:
                print("Title cannot be empty.")
        elif choice == "2":
            show_tasks(task_list)
        elif choice == "3":
            task_id = read_id("Task id to delete: ")
            if task_id is not None:
                print("Task deleted." if tasks.delete_task(task_list, task_id)
                      else "Task not found.")
        elif choice == "4":
            task_id = read_id("Task id to mark as done: ")
            if task_id is not None:
                print("Task marked as done." if tasks.mark_done(task_list, task_id)
                      else "Task not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()