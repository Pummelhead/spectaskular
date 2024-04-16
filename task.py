import sqlite3
import time
import datetime
import tkinter as tk
from db import conn
from db import cur

def add_task(task_entry, desc_entry, priority_var):
    task = task_entry.get()
    description = desc_entry.get()
    priority = priority_var.get()
    try:
        cur.execute(f"INSERT INTO all_pending_tasks (task, description, priority) VALUES (?, ?, ?)", (task, description, priority))
    except sqlite3.Error as e:
        pass
    task_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    conn.commit()

def delete_task(tree):
    selected = tree.selection()
    task = tree.item(selected)['values'][0]
    try:
        cur.execute(f"DELETE FROM all_pending_tasks WHERE task='{task}'")
        cur.execute(f"DELETE FROM all_completed_tasks WHERE task='{task}'")
    except sqlite3.Error as e:
        pass
    conn.commit()

def complete_task(tree):
    selected = tree.selection()
    task = tree.item(selected)['values'][0]
    try:
        cur.execute(f"INSERT INTO all_completed_tasks SELECT * FROM all_pending_tasks WHERE task='{task}'")
        cur.execute(f"UPDATE all_completed_tasks SET completed = 'true' WHERE task='{task}'")
        cur.execute(f"DELETE FROM all_pending_tasks WHERE task='{task}'")
    except sqlite3.Error as e:
        pass
    conn.commit()

def uncomplete_task(tree):
    selected = tree.selection()
    task = tree.item(selected)['values'][0]
    try:
        cur.execute(f"INSERT INTO all_pending_tasks SELECT * FROM all_completed_tasks WHERE task='{task}'")
        cur.execute(f"UPDATE all_pending_tasks SET completed = 'false' WHERE task='{task}'")
        cur.execute(f"DELETE FROM all_completed_tasks WHERE task='{task}'")
    except sqlite3.Error as e:
        pass
    conn.commit()

def edit_entry(task_entry, desc_entry, priority_var, tree):
    selected = tree.selection()
    if selected:
        existing_task = tree.item(selected)['values'][0]
        new_task = task_entry.get()
        new_description = desc_entry.get()
        new_priority = priority_var.get()
        try:
            cur.execute(f"UPDATE 'all_pending_tasks' SET task = '{new_task}' WHERE task = '{existing_task}'")
        except sqlite3.Error as e:
            pass
        try:
            cur.execute(f"UPDATE 'all_pending_tasks' SET description = '{new_description}' WHERE task = '{new_task}'")
        except sqlite3.Error as e:
            pass
        try:
            cur.execute(f"UPDATE 'all_pending_tasks' SET priority = '{new_priority}' WHERE task = '{new_task}'")
        except sqlite3.Error as e:
            pass
        task_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
    conn.commit()
