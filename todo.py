# todo.py
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return [] # Return empty list if file is empty, corrupt, or not found

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def print_welcome_message():
    """Prints a welcome message and instructions."""
    print("====================================")
    print("  Welcome to your CLI Todo List!")
    print("====================================")
    print("\nCommands:")
    print("  list           - Show all tasks")
    print("  add [task]     - Add a new task")
    print("  done [number]  - Mark a task as complete")
    print("  remove [number]- Remove a task")
    print("  exit           - Exit the program")
    print("------------------------------------")

def list_tasks(tasks):
    """Lists all tasks with their number and status."""
    print("\n--- Your Tasks ---")
    if not tasks:
        print("You have no tasks.")
    else:
        for i, task in enumerate(tasks):
            status = "[✓]" if task['done'] else "[ ]"
            print(f"{i + 1}. {status} {task['text']}")
    print("------------------")

def main():
    """The main function of the todo list app."""
    tasks = load_tasks()
    print_welcome_message()

    while True:
        command_input = input("> ").strip()

        if command_input == "list":
            list_tasks(tasks)

        elif command_input.startswith("add "):
            task_text = command_input[4:]
            if task_text:
                tasks.append({'text': task_text, 'done': False})
                save_tasks(tasks)
                print(f"Added: '{task_text}'")
            else:
                print("Please enter a task to add. (e.g., add Learn Python)")

        elif command_input.startswith("done "):
            try:
                task_number_str = command_input[5:]
                task_index = int(task_number_str) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]['done'] = True
                    save_tasks(tasks)
                    print(f"Completed: '{tasks[task_index]['text']}'")
                    list_tasks(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number. (e.g., done 2)")

        elif command_input.startswith("remove "):
            try:
                task_number_str = command_input[7:]
                task_index = int(task_number_str) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    save_tasks(tasks)
                    print(f"Removed: '{removed_task['text']}'")
                    list_tasks(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number. (e.g., remove 1)")

        elif command_input == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'list', 'add [task]', 'done [number]', 'remove [number]', or 'exit'.")

if __name__ == "__main__":
    main()
