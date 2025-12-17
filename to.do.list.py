
tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        status = "Completed" if task["done"] else "Pending"
        print(f"{i + 1}. {task['title']} - {status}")

def add_task():
    title = input("\nEnter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully.")

def update_task():
    display_tasks()
    try:
        index = int(input("\nEnter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new task title: ")
            tasks[index]["title"] = new_title
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    display_tasks()
    try:
        index = int(input("\nEnter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            mark_completed()
        elif choice == "6":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()
