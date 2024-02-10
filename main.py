import tkinter as tk
from gui import creat_widgets
from task import add_task
from db import cur

root = tk.Tk()

root.geometry("1920x1080")
root.title("Spectaskular")

creat_widgets(root, add_task)

print("all pending tasks")
for row in cur.execute("SELECT task, description, priority FROM all_pending_tasks ORDER BY task"):
    print(f"{row[0]}, {row[1]}, {row[2]}")

root.mainloop()

def main():
    return