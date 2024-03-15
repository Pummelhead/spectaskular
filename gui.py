import tkinter as tk
from tkinter import ttk
from db import cur

def create_task_widgets(root, add_task, delete_task):
    tk.Label(root, text="Task: ").grid(row=0, column=0)
    task_entry = tk.Entry(root)
    task_entry.grid(row=0, column=1)

    tk.Label(root, text="Description:").grid(row=1, column=0)
    desc_entry = tk.Entry(root)
    desc_entry.grid(row=1, column=1)

    tk.Label(root, text="Priority:").grid(row=2, column=0)
    priority_var = tk.StringVar(root)
    priority_var.set("High")
    priority_dropdown = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
    priority_dropdown.grid(row=2, column=1)

    add_button = tk.Button(root, text="Add Task", command=lambda: add_task(task_entry, desc_entry, priority_var))
    add_button.grid(row=3, column=0, columnspan=2)

    all_tasks = cur.execute("SELECT task FROM all_pending_tasks").fetchall()
    task_to_delete = tk.StringVar(root)
    task_to_delete.set("Select a task")
    delete_dropdown = tk.OptionMenu(root, task_to_delete, *all_tasks)
    delete_dropdown.grid(row=4, column=0)
    
    delete_button = tk.Button(root, text="Delete Task", command=lambda: delete_task(task_to_delete))
    delete_button.grid(row=4, column=1)

def display_table_widgets(root, display_data_func):
    tree = ttk.Treeview(root, columns=("Description", "Priority"))
    tree.heading("#0", text="Task")
    tree.heading("Description", text="Description")
    tree.heading("Priority", text="Priority")
    tree["displaycolumns"] = ("Description", "Priority")
    tree.grid(row=0, rowspan=1000, column=2, columnspan=2)
    display_data_func(tree)