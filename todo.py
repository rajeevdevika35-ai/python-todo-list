# TO-DO LIST PROJECT
# DecodeLabs Internship Project 1

tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("📌 No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    # Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("📌 No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"✅ '{removed}' deleted successfully!")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

    # Exit
    elif choice == "4":
        print("\nThank you for using the To-Do List!")
        break

    # Invalid Choice
    else:
        print("❌ Invalid choice! Please enter a number between 1 and 4.")