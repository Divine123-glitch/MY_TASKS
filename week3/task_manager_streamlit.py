import streamlit as st

# Initialize session state for persistent data (dictionary)
if "tasks" not in st.session_state:
    st.session_state.tasks = {}  # Dictionary for tasks: {task_id: (name, priority, category)}
if "used_ids" not in st.session_state:
    st.session_state.used_ids = set()  # Set for unique task IDs
if "categories" not in st.session_state:
    st.session_state.categories = ["Work", "Personal", "Study"]  # List of categories
if "current_action" not in st.session_state:
    st.session_state.current_action = "menu"  # Variable to track current action

# Main title with Markdown (substitute for escape sequence formatting)
st.markdown("<h1 style='color: blue;'>=== Personal Task Manager ===</h1>", unsafe_allow_html=True)

# Menu options using buttons
st.write("Select an action:")
if st.button("1. Add a new task"):
    st.session_state.current_action = "add"
if st.button("2. View all tasks"):
    st.session_state.current_action = "view"
if st.button("3. Update a task"):
    st.session_state.current_action = "update"
if st.button("4. Delete a task"):
    st.session_state.current_action = "delete"
if st.button("5. View tasks by category"):
    st.session_state.current_action = "view_category"
if st.button("6. Exit"):
    st.session_state.current_action = "exit"

# Handle actions based on current_action
if st.session_state.current_action == "add":
    st.markdown("<h3 style='color: green;'>Add New Task</h3>", unsafe_allow_html=True)
    task_name = st.text_input("Enter task name:", key="add_name")
    priority = st.text_input("Enter priority (High/Medium/Low):", key="add_priority").capitalize()
    category = st.text_input("Enter category (Work/Personal/Study):", key="add_category").capitalize()
    
    if st.button("Submit Task"):
        # Validate inputs
        if priority not in ["High", "Medium", "Low"]:
            st.markdown("<p style='color: red;'>Invalid priority! Please enter High, Medium, or Low.</p>", unsafe_allow_html=True)
        elif category not in st.session_state.categories:
            st.markdown("<p style='color: red;'>Invalid category! Available categories: {}</p>".format(st.session_state.categories), unsafe_allow_html=True)
        elif task_name == "":
            st.markdown("<p style='color: red;'>Task name cannot be empty!</p>", unsafe_allow_html=True)
        else:
            # Generate unique task ID using while loop
            task_id = 1
            while task_id in st.session_state.used_ids:
                task_id += 1
            st.session_state.used_ids.add(task_id)
            st.session_state.tasks[task_id] = (task_name, priority, category)  # Store as tuple
            st.markdown(f"<p style='color: green;'>Task '{task_name}' added with ID {task_id}!</p>", unsafe_allow_html=True)
            st.session_state.current_action = "menu"

elif st.session_state.current_action == "view":
    if not st.session_state.tasks:
        st.markdown("<p style='color: red;'>No tasks available!</p>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: blue;'>All Tasks:</h3>", unsafe_allow_html=True)
        for task_id, task_info in st.session_state.tasks.items():
            st.write(f"ID: {task_id}, Name: {task_info[0]}, Priority: {task_info[1]}, Category: {task_info[2]}")
    if st.button("Back to Menu"):
        st.session_state.current_action = "menu"

elif st.session_state.current_action == "update":
    task_id = st.text_input("Enter task ID to update:", key="update_id")
    if task_id:
        task_id = int(task_id) if task_id.isdigit() else 0
        if task_id not in st.session_state.tasks:
            st.markdown("<p style='color: red;'>Task ID not found!</p>", unsafe_allow_html=True)
        else:
            current_task = st.session_state.tasks[task_id]
            new_name = st.text_input(f"Enter new task name (press Enter to keep '{current_task[0]}'):", key="update_name")
            new_priority = st.text_input(f"Enter new priority (High/Medium/Low, press Enter to keep '{current_task[1]}'):", key="update_priority").capitalize()
            new_category = st.text_input(f"Enter new category (Work/Personal/Study, press Enter to keep '{current_task[2]}'):", key="update_category").capitalize()
            
            if st.button("Submit Update"):
                task_name = new_name if new_name else current_task[0]
                priority = new_priority if new_priority in ["High", "Medium", "Low"] else current_task[1]
                category = new_category if new_category in st.session_state.categories else current_task[2]
                st.session_state.tasks[task_id] = (task_name, priority, category)
                st.markdown(f"<p style='color: green;'>Task ID {task_id} updated!</p>", unsafe_allow_html=True)
                st.session_state.current_action = "menu"

elif st.session_state.current_action == "delete":
    task_id = st.text_input("Enter task ID to delete:", key="delete_id")
    if task_id:
        task_id = int(task_id) if task_id.isdigit() else 0
        if task_id in st.session_state.tasks:
            task_name = st.session_state.tasks[task_id][0]
            del st.session_state.tasks[task_id]
            st.session_state.used_ids.remove(task_id)
            st.markdown(f"<p style='color: green;'>Task '{task_name}' deleted!</p>", unsafe_allow_html=True)
            st.session_state.current_action = "menu"
        else:
            st.markdown("<p style='color: red;'>Task ID not found!</p>", unsafe_allow_html=True)
    if st.button("Back to Menu"):
        st.session_state.current_action = "menu"

elif st.session_state.current_action == "view_category":
    category = st.text_input("Enter category to view (Work/Personal/Study):", key="view_cat").capitalize()
    if category:
        if category not in st.session_state.categories:
            st.markdown("<p style='color: red;'>Invalid category!</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h3 style='color: blue;'>Tasks in {category}:</h3>", unsafe_allow_html=True)
            found = False
            for task_id, task_info in st.session_state.tasks.items():
                if task_info[2] == category:
                    st.write(f"ID: {task_id}, Name: {task_info[0]}, Priority: {task_info[1]}")
                    found = True
            if not found:
                st.markdown("<p style='color: red;'>No tasks in this category!</p>", unsafe_allow_html=True)
    if st.button("Back to Menu"):
        st.session_state.current_action = "menu"

elif st.session_state.current_action == "exit":
    st.markdown("<h3 style='color: blue;'>Thank you for using Task Manager!</h3>", unsafe_allow_html=True)
