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
    cur.execute(f"INSERT INTO all_pending_tasks (task, description, priority) VALUES (?, ?, ?)", (task, description, priority))
    print("task added")
    task_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    conn.commit()

def delete_task(task_to_delete):
    task = task_to_delete.get()
    print(type(task))
    try:
        cur.execute(f"DELETE FROM all_pending_tasks WHERE task='{task}'")
    except sqlite3.Error as e:
        print(e)
    print(task)
    print("Delete button pressed")
    conn.commit()

def complete_task():
    tasks = cur.execute("SELECT task FROM all_tasks").fetchall()
    task_list = [row[0] for row in tasks]
    complete_task_task = input(f"Task to complete {task_list}: ")
    task_move = cur.execute(f"SELECT * FROM all_pending_tasks WHERE task='{complete_task_task}'").fetchone()
    all_tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    for table in all_tables:    
        table_name = table[0]
        if table_name != "all_tasks":
            try:
                cur.execute(f"DELETE FROM {table_name} WHERE task='{complete_task_task}'")
            except sqlite3.Error as e:
                pass
    cur.execute(f"INSERT INTO all_completed_tasks (task, description) VALUES (?, ?)", (task_move[0], task_move[1]))
    conn.commit()

def edit_task():
    tasks = cur.execute("SELECT task FROM all_pending_tasks").fetchall()
    task_list = [row[0] for row in tasks]
    edit_task_task = input(f"Task to edit {task_list}: ")
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    edit_task_name = input("Would you like to edit the name of this task? (y/n): ")
    if edit_task_name == "y":
        new_task = input(f"Task: ")
        for table in tables:
            table_name = table[0]
            try:
                cur.execute(f"UPDATE '{table_name}' SET task = '{new_task}' WHERE task = '{edit_task_task}'")
            except sqlite3.Error as e:
                pass
    edit_task_description = input("Would you like to edit the description of this task? (y/n): ")
    if edit_task_description == "y":
        new_description = input(f"Description: ")
        for table in tables:
            table_name = table[0]
            try:
                cur.execute(f"UPDATE '{table_name}' SET description = '{new_description}' WHERE description = '{edit_task_description}'")
            except sqlite3.Error as e:
                pass
    conn.commit()
