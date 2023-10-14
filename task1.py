
tasks = []

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task():
    display_tasks()
    try:
        inp = int(input("Enter the task number to remove: "))
        index=inp-1
        if 0 <= index < len(tasks):
            remove = tasks.pop(index)
            print(f"Task '{remove}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a task number.")

def update_task():
    display_tasks()
    try:
        inp = int(input("Enter the task number to update: "))
        index=inp-1
        if 0 <= index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[index] = new_task
            print(f"Task updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a task number.")


while True:
    print("\nOptions:")
    print("1. Display tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Update a task")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        update_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Exiting....")
