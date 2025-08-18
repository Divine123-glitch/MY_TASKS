# Personal Task Manager

# Dictionary to store tasks with task ID as key and tuple of (task_name, priority) as value
tasks = {}
# Set to keep track of used task IDs to avoid duplicates
used_ids = set()
# List to store task categories
categories = ["Work", "Personal", "Study"]

def display_menu():
    # Using escape sequences for formatting
    print("\n\033[1m=== Personal Task Manager ===\033[0m")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. View tasks by category")
    print("6. Exit")
    print("\033[1m==========================\033[0m")

def add_task():
    # Input statements for task details
    task_name = input("Enter task name: ")
    while True:
        priority = input("Enter priority (High/Medium/Low): ").title()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Invalid priority! Please enter High, Medium, or Low.")
    
    while True:
        category = input("Enter category (Work/Personal/Study): ").title()
        if category in categories:
            break
        print("Invalid category! Available categories:", categories)
    
    # Generate unique task ID
    task_id = 1
    while task_id in used_ids:
        task_id += 1
    used_ids.add(task_id)
    
    # Store task as a tuple in the dictionary
    tasks[task_id] = (task_name, priority, category)
    print(f"\033[32mTask '{task_name}' added with ID {task_id}!\033[0m")

def view_tasks():
    if not tasks:
        print("\033[31mNo tasks available!\033[0m")
        return
    print("\n\033[1mAll Tasks:\033[0m")
    for task_id, task_info in tasks.items():
        print(f"ID: {task_id}, Name: {task_info[0]}, Priority: {task_info[1]}, Category: {task_info[2]}")

def update_task():
    task_id = int(input("Enter task ID to update: "))
    if task_id not in tasks:
        print("\033[31mTask ID not found!\033[0m")
        return
    
    # Update task name
    new_name = input("Enter new task name (press Enter to keep '{tasks[task_id][0]}'): ")
    new_priority = input("Enter new priority (High/Medium/Low, press Enter to keep '{tasks[task_id][1]}'): ").title()
    new_category = input("Enter new category (Work/Personal/Study, press Enter to keep '{tasks[task_id][2]}'): ").title()
    
    # Keep existing values if input is empty
    task_name = new_name if new_name else tasks[task_id][0]
    priority = new_priority if new_priority in ["High", "Medium", "Low"] else tasks[task_id][1]
    category = new_category if new_category in categories else tasks[task_id][2]
    
    tasks[task_id] = (task_name, priority, category)
    print(f"\033[32mTask ID {task_id} updated!\033[0m")

def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        task_name = tasks[task_id][0]
        del tasks[task_id]
        used_ids.remove(task_id)
        print(f"\033[32mTask '{task_name}' deleted!\033[0m")
    else:
        print("\033[31mTask ID not found!\033[0m")

def view_by_category():
    category = input("Enter category to view (Work/Personal/Study): ").capitalize()
    if category not in categories:
        print("\033[31mInvalid category!\033[0m")
        return
    
    print(f"\n\033[1mTasks in {category}:\033[0m")
    found = False
    for task_id, task_info in tasks.items():
        if task_info[2] == category:
            print(f"ID: {task_id}, Name: {task_info[0]}, Priority: {task_info[1]}")
            found = True
    if not found:
        print("\033[31mNo tasks in this category!\033[0m")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        view_by_category()
    elif choice == "6":
        print("\033[1mThank you for using Task Manager!\033[0m")
        break
    else:
        print("\033[31mInvalid choice! Please enter a number between 1 and 6.\033[0m")