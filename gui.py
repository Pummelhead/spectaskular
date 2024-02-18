import tkinter as tk
from tkinter import ttk

def create_task_widgets(root, add_task):
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

def display_table_widgets(root, display_data_func):
    tree = ttk.Treeview(root, columns=("Task", "Description", "Priority"))
    tree.heading("Task", text="Task")
    tree.heading("Description", text="Description")
    tree.heading("Priority", text="Priority")
    tree.grid(row=0, rowspan=1000, column=2, columnspan=2)
    display_data_func(tree)