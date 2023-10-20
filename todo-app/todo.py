# todo.py

from datetime import datetime

# Function to read tasks from the tasks.txt file
def read_tasks():
    with open('tasks.txt', 'r') as file:
        return [line.strip().split('|') for line in file.readlines()]

# Function to write tasks to the tasks.txt file
def write_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write('|'.join(task) + '\n')

# Function to add a new task with a deadline
def add_task(task, deadline):
    tasks = read_tasks()
    tasks.append([task, deadline, ''])
    write_tasks(tasks)
    print(f"Task '{task}' with deadline '{deadline}' added successfully!")

# Function to list all tasks
def list_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "[DONE]" if task[2] else "[TODO]"
            print(f"{i}. {task[0]} (Deadline: {task[1]}) {status}")

# Function to mark a task as done
def mark_done(task_num):
    tasks = read_tasks()
    if 1 <= task_num <= len(tasks):
        if not tasks[task_num - 1][2]:
            tasks[task_num - 1][2] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_tasks(tasks)
            print(f"Task {task_num} marked as done.")
        else:
            print("Task already marked as done.")
    else:
        print("Invalid task number.")

# Main program loop
while True:
    print("\nTo-Do List:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        deadline = input("Enter the deadline (YYYY-MM-DD HH:MM:SS): ")
        add_task(task, deadline)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        task_num = int(input("Enter the task number to mark as done: "))
        mark_done(task_num)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
