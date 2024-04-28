# Task 1 To-Do List

tasks = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("\nEnter your choice : ")

    if choice == '1':
        task = input("\nEnter task : ")
        tasks.append(task)
        print(f"\nTask '{task}' added successfully.")
    elif choice == '2':
        if not tasks:
            print("\nNo tasks to remove.")
        else:
            task = input("\nEnter task to remove : ")
            if task in tasks:
                tasks.remove(task)
                print(f"\nTask '{task}' removed successfully.")
            else:
                print(f"\nTask '{task}' not found.")
    elif choice == '3':
        if not tasks:
            print("\nNo tasks.")
        else:
            print("\nTasks : ")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == '4':
        break
    else:
        print("\nInvalid choice. Please try again.")