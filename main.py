import tkinter as tk
from gui import create_task_widgets, display_table_widgets
from table import display_all_pending_tasks
from task import add_task, delete_task
from db import cur

root = tk.Tk()

root.geometry("1920x1080")
root.title("Spectaskular")

create_task_widgets(root, add_task, delete_task)
display_table_widgets(root, display_all_pending_tasks)

root.mainloop()

def main():
    return