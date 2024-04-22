import tkinter as tk
from tkinter import ttk
from tktimepicker import SpinTimePickerOld, constants
from table import display_all_pending_tasks, display_all_completed_tasks, display_all_tasks
from task import add_task, delete_task, edit_entry, complete_task, uncomplete_task
from functools import partial

window_geometry=None
tree=None
table_var = None

def create_window(geometry=None):
    global root
    root = tk.Tk()
    if geometry:
        root.geometry(geometry)
    root.title("Spectaskular")

    create_task_widgets(root)
    create_table_display_widgets(root)
    display_table_widgets(root)

    root.mainloop()

def save_geometry():
    global window_geometry
    window_geometry = f"{root.winfo_width()}x{root.winfo_height()}+{root.winfo_x()}+{root.winfo_y()}"

def reload_window():
    global window_geometry
    save_geometry()
    root.destroy()
    create_window(window_geometry)

def create_task_widgets(root, treeview=None):
    global tree

    #def display_toggle_radio():
    #    if display_var.get:
    #        display_var.set(False)
    #    else:
    #        display_var.set(True)
    #    print(f"display: {display_var.get()}")
#
    #def due_toggle_radio():
    #    if due_var.get:
    #        due_var.set(False)
    #    else:
    #        due_var.set(True)
    #    print(f"due: {due_var.get()}")

    tk.Label(root, text="Task: ").grid(row=0, column=0)
    task_entry = tk.Entry(root)
    task_entry.grid(row=0, column=1)

    tk.Label(root, text="Description:").grid(row=1, column=0)
    desc_entry = tk.Entry(root)
    desc_entry.grid(row=1, column=1)

    tk.Label(root, text="Priority:").grid(row=2, column=0)
    priority_var = tk.StringVar(root)
    priority_var.set("5")
    priority_dropdown = tk.OptionMenu(root, priority_var, "5", "4", "3", "2", "1")
    priority_dropdown.grid(row=2, column=1)
    
    display_var = tk.BooleanVar()
    display_var.set(False)
    print(f"display is: {display_var.get()}")
    tk.Checkbutton(root, text="Set Display Date/Time?", variable=display_var).grid(row=3, column=0, columnspan=2)
    
    tk.Label(root, text="Display Date:").grid(row=4, column=0)
    display_date_entry = tk.Entry(root)
    display_date_entry.insert(0, "MM/DD/YY")
    display_date_entry.grid(row=4, column=1)
    
    tk.Label(root, text="Display Time (24HR):").grid(row=5, column=0)
    display_time_picker = SpinTimePickerOld(root)
    display_time_picker.addAll(constants.HOURS24)
    display_time_picker.configureAll(width=5)
    display_time_picker.grid(row=5, column=1)

    due_var = tk.BooleanVar()
    due_var.set(False)
    print(f"due is: {due_var.get()}")
    tk.Checkbutton(root, text="Set Due Date/Time?", variable=due_var).grid(row=6, column=0, columnspan=2)
    
    tk.Label(root, text="Due Date:").grid(row=7, column=0)
    due_date_entry = tk.Entry(root)
    due_date_entry.insert(0, "MM/DD/YY")
    due_date_entry.grid(row=7, column=1)
    
    tk.Label(root, text="Due Time (24HR):").grid(row=8, column=0)
    due_time_picker = SpinTimePickerOld(root)
    due_time_picker.addAll(constants.HOURS24)
    due_time_picker.configureAll(width=5)
    due_time_picker.grid(row=8, column=1)

    add_button = tk.Button(root, text="Add Task",
                command=lambda: [add_task(task_entry,
                                          desc_entry,
                                          priority_var,
                                          display_var,
                                          display_date_entry,
                                          display_time_picker,
                                          due_var,
                                          due_date_entry,
                                          due_time_picker),
                                          display_table_widgets(root)])
    add_button.grid(row=9, column=0)
    edit_button = ttk.Button(root, text="Edit Task", 
                command=lambda: [edit_entry(task_entry, desc_entry, priority_var, tree),
                display_table_widgets(root)])
    edit_button.grid(row=9, column=1)

    complete_button = tk.Button(root, text="Complete Task", command=lambda: [complete_task(tree), display_table_widgets(root)])
    complete_button.grid(row=10, column=0)

    uncomplete_button = tk.Button(root, text="Uncomplete Task", command=lambda: [uncomplete_task(tree), display_table_widgets(root)])
    uncomplete_button.grid(row=10, column=1)

    tk.Label(root, text="Select a task: ").grid(row=11, column=0)
    delete_button = tk.Button(root, text="Delete Task", command=lambda: [delete_task(tree), display_table_widgets(root)])
    delete_button.grid(row=11, column=1)

    reload_button = tk.Button(root, text="Reload Window", command=lambda: reload_window())
    reload_button.grid(row=12, column=0, columnspan=2)

def create_table_display_widgets(root):
    global table_var
    table_var = tk.IntVar(value=1)
    tk.Radiobutton(root, text="Pending", variable=table_var, value=1, command=lambda: display_table_widgets(root)).grid(row=0, column=2)
    root.columnconfigure(2, minsize=200)
    tk.Radiobutton(root, text="Complete", variable=table_var, value=2, command=lambda: display_table_widgets(root)).grid(row=0, column=3)
    root.columnconfigure(3, minsize=200)
    tk.Radiobutton(root, text="All", variable=table_var, value=3, command=lambda: display_table_widgets(root)).grid(row=0, column=4)
    root.columnconfigure(4, minsize=200)
    

def display_table_widgets(root):
    global tree
    global table_var
    tree = ttk.Treeview(root, columns=("Task", "Description", "Priority", "Due Time", "Every", "Unit"))
    tree.heading("#0", text="")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.heading("Task", text="Task", command=lambda: sort_column(tree, "Task", False))
    tree.heading("Description", text="Description", command=lambda: sort_column(tree, "Description", False))
    tree.heading("Priority", text="Priority", command=lambda: sort_column(tree, "Priority", False))
    tree.heading("Due Time", text="Due Time", command=lambda: sort_column(tree, "Due Time", False))
    tree.heading("Every", text="Every", command=lambda: sort_column(tree, "Every", False))
    tree.heading("Unit", text="Unit", command=lambda: sort_column(tree, "Unit", False))
    tree["displaycolumns"] = ("Task", "Description", "Priority", "Due Time", "Every", "Unit")
    tree.grid(row=1, rowspan=1000, column=2, columnspan=3, sticky="nsew")
    table_selection = table_var.get()
    if table_selection == 1:
        display_all_pending_tasks(tree)
    elif table_selection == 2:
        display_all_completed_tasks(tree)
    elif table_selection == 3:
        display_all_tasks(tree)

def sort_column(tree, col, reverse=False):
    """Sort tree contents when a column header is clicked."""
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=reverse)
    for index, (val, child) in enumerate(data):
        tree.move(child, '', index)
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))


