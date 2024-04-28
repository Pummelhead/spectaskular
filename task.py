import sqlite3
import tkinter as tk
from db import conn
from db import cur

def add_task(task_entry,
             desc_entry,
             priority_var,
             display_var=False,
             display_month_entry=0,
             display_day_entry=0,
             display_year_entry=0,
             display_time_picker="",
             due_var=False,
             due_month_entry=0,
             due_day_entry=0,
             due_year_entry=0,
             due_time_picker="-",
             repeat_var=False,
             frequency_step_entry=0,
             frequency_type_var=""):
    try:
        cur.execute(f"INSERT INTO all_pending_tasks (task, description, priority) VALUES (?, ?, ?)",
                    (task_entry.get(),
                     desc_entry.get(),
                     priority_var.get(),
                     ))
    except sqlite3.Error as e:
        pass
    if display_var.get():
        try:
            cur.execute("UPDATE all_pending_tasks SET display_month = ?, display_day = ?, display_year = ?, display_time = ? WHERE task = ?", (display_month_entry.get(), display_day_entry.get(), display_year_entry.get(), f"{display_time_picker.hours():02d}:{display_time_picker.minutes():02d}", task_entry.get()))
        except sqlite3.Error as e:
            print(e)
    if due_var.get():
        try:
            cur.execute("UPDATE all_pending_tasks SET due_month = ?, due_day = ?, due_year = ?, due_time =? WHERE task = ?", (due_month_entry.get(), due_day_entry.get(), due_year_entry.get(), f"{due_time_picker.hours():02d}:{display_time_picker.minutes():02d}", task_entry.get()))
        except sqlite3.Error as e:
            print(e)
    if repeat_var.get():
        try:
            cur.execute("UPDATE all_pending_tasks SET frequency_step = ?, frequency_step_type = ? WHERE task = ?", (frequency_step_entry.get(), frequency_type_var.get(), task_entry.get()))
        except sqlite3.Error as e:
            print(e)
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
