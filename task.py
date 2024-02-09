import sqlite3
import time
import datetime
import table
from db import conn
from db import cur

def add_task():
    task = input("Task: ")
    description = input(f"Description: ")
    add_to_table = input("Would you like to add this to a table? (y/n): ")
    if add_to_table == "y":
        tables = cur.execute("SELECT name FROM all_created_tables").fetchall()
        table_list = [row[0] for row in tables]
        choice = None
        while choice not in table_list:
            if choice == 'x':
                break
            choice = input(f"Which table would you like to add it to? {table_list} or enter 'x': ")
        if choice in tables:
            cur.execute(f"INSERT INTO {choice} (task, description) VALUES (?, ?)", (task, description))
    cur.execute(f"INSERT INTO all_pending_tasks (task, description) VALUES (?, ?)", (task, description))
    cur.execute(f"INSERT INTO all_tasks (task) VALUES ('{task}')")
    conn.commit()

def delete_task():
    tasks = cur.execute("SELECT task FROM all_tasks").fetchall()
    task_list = [row[0] for row in tasks]
    delete_task_task = input(f"Task to delete {task_list}: ")
    all_tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    for table in all_tables:    
        table_name = table[0]
        print(table_name)
        try:
            cur.execute(f"DELETE FROM {table_name} WHERE task='{delete_task_task}'")
        except sqlite3.Error as e:
            pass
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


if __name__ == "__main__":
    #table.create_table()
    #table.create_table()
    table.create_table()
    #add_task()
    #add_task()
    #add_task()
    #delete_task()
    #complete_task()
    #table.delete_table()
    #edit_task()
    table.edit_table()
    print("all tasks")
    for row in cur.execute("SELECT task FROM all_tasks ORDER BY task"):
        print(row[0])
    print("all pending tasks")
    for row in cur.execute("SELECT task, description FROM all_pending_tasks ORDER BY task"):
        print(f"{row[0]}, {row[1]}")
    print("all completed tasks")
    for row in cur.execute("SELECT task, description FROM all_completed_tasks ORDER BY task"):
        print(f"{row[0]}, {row[1]}")
    print("all tables")
    for row in cur.execute("SELECT name FROM all_created_tables ORDER BY name"):
        print(row[0])