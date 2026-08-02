import json
import os

FILE_NAME = "todos.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!\n")
        return
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. [{status}] {task['title']}")
    print()


def main():
    tasks = load_tasks()
    while True:
        print("1. Add Task  2. Show Tasks  3. Mark Done  4. Delete Task  5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print("Task added!\n")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Task number to mark done: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
                print("Marked as done!\n")

        elif choice == "4":
            show_tasks(tasks)
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                save_tasks(tasks)
                print(f"Deleted: {removed['title']}\n")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
