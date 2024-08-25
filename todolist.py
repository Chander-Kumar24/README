import json
tasks = []

def add_task():
    """I want to add new task here"""
    description = input("Enter the task description: ").strip()
    due_date = input("Enter the due date (YYYY-MM-DD): ").strip()

    if not description or not due_date:
        print("Both description and due date are required.")
        return

    task = {
        'description': description,
        'due_date': due_date
    }
    tasks.append(task)
    print(f"Task '{description}' added successfully.")

def remove_task():
    """Remove a task """
    description = input("Enter the description of the task to remove: ").strip()
    
    global tasks
    tasks = [task for task in tasks if task['description'] != description]

    print(f"Task '{description}' removed successfully.")

def view_all_tasks():
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print()

def save_to_file(filename):
    """Save tasks to a file."""
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to {filename}.")

def load_from_file(filename):
    """Load tasks from a file."""
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
        print(f"Tasks loaded from {filename}.")
    except FileNotFoundError:
        print(f"No file found with the name {filename}.")
    except json.JSONDecodeError:
        print("Error reading the file. It might be corrupted.")

def main():
    """Main function to run the To-Do List Application."""
    filename = 'tasks.json'

    load_from_file(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View All Tasks")
        print("4. Save to File")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_all_tasks()
        elif choice == '4':
            save_to_file(filename)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
