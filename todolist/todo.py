import os

FILENAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.\n")
        return
    print("\n📝 Your To-Do List:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task}")
    print()

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append("[ ] " + task)
        save_tasks(tasks)
        print("✅ Task added.\n")
    else:
        print("⚠️ Empty task not added.\n")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            if tasks[num - 1].startswith("[x]"):
                print("✅ Task already marked complete.\n")
            else:
                tasks[num - 1] = tasks[num - 1].replace("[ ]", "[x]", 1)
                save_tasks(tasks)
                print("🎉 Task marked as complete!\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Enter a valid number.\n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: {removed}\n")
        else:
            print("❌ Invalid task number.\n")
    except ValueError:
        print("❌ Enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("========== TO-DO LIST ==========")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
