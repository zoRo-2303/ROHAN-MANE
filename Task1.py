import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

def list_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks in the to-do list!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{idx}. [{status}] {task['task']}")

def update_task(index, new_task):
    """Update a task."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_task
        save_tasks(tasks)
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def mark_done(index):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def remove_task(index):
    """Remove a task."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' removed!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Remove Task")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task: ")
            update_task(index, new_task)
        elif choice == "4":
            list_tasks()
            index = int(input("Enter task number to mark as done: ")) - 1
            mark_done(index)
        elif choice == "5":
            list_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            remove_task(index)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
