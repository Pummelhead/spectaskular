from db import conn
from db import cur
import tkinter as tk
from datetime import datetime

def create_table():
    create_table_name = input("Table name: ")
    cur.execute(f'''CREATE TABLE IF NOT EXISTS '{create_table_name}' (
            task TEXT,
            description TEXT,
            priority INTEGER,
            display_time NULL,
            due_time NULL,
            display INTEGER,
            frequency_step NULL,
            frequency_step_type NULL
            )''')
    conn.commit()
    cur.execute(f"INSERT INTO all_created_tables (name) VALUES ('{create_table_name}')")
    conn.commit()

def delete_table():
    tables = cur.execute("SELECT name FROM all_created_tables").fetchall()
    table_list = [row[0] for row in tables]
    delete_table_name = input(f"Table to delete {table_list}: ")
    cur.execute(f"DROP TABLE IF EXISTS '{delete_table_name}'")
    cur.execute(f"DELETE FROM all_created_tables WHERE name='{delete_table_name}'")
    conn.commit()

def edit_table():
    tables = cur.execute("SELECT name FROM all_created_tables").fetchall()
    table_list = [row[0] for row in tables]
    edit_table_name = input(f"Table to edit {table_list}: ")
    new_table_name = input("New table name: ")
    cur.execute(f"ALTER TABLE '{edit_table_name}' RENAME TO '{new_table_name}'")
    cur.execute(f"UPDATE all_created_tables SET name = '{new_table_name}' WHERE name = '{edit_table_name}'")
    conn.commit()

def display_all_pending_tasks(tree):
    rows = cur.execute("SELECT * FROM all_pending_tasks").fetchall()
    cur_row = 1
    tree.tag_configure("odd")
    tree.tag_configure("even", background="#f0f0f0")
    for row in rows:
        if datetime(row[5]+2000,row[3],row[4]) <= datetime.now():
            tag = "even" if cur_row % 2 == 0 else "odd"
            tree.insert("", tk.END, values=(row[0], row[1], row[2], f"{row[6]:02d}/{row[7]:02d}/{row[8]:02d} - {row[9]}", row[11], row[12]), tags=(tag))
            cur_row += 1
    conn.commit()

def display_all_completed_tasks(tree):
    rows = cur.execute("SELECT * FROM all_completed_tasks").fetchall()
    cur_row = 1
    tree.tag_configure("odd")
    tree.tag_configure("even", background="#f0f0f0")
    for row in rows:
        tag = "even" if cur_row % 2 == 0 else "odd"
        tree.insert("", tk.END, values=(row[0], row[1], row[2], f"{row[6]:02d}/{row[7]:02d}/{row[8]:02d} - {row[9]}", row[11], row[12]), tags=(tag))
        cur_row += 1
    conn.commit()

def display_all_tasks(tree):
    rows = cur.execute("SELECT * FROM all_pending_tasks").fetchall()
    cur_row = 1
    tree.tag_configure("odd")
    tree.tag_configure("even", background="#f0f0f0")
    for row in rows:
        tag = "even" if cur_row % 2 == 0 else "odd"
        tree.insert("", tk.END, values=(row[0], row[1], row[2], f"{row[6]:02d}/{row[7]:02d}/{row[8]:02d} - {row[9]}", row[11], row[12]), tags=(tag))
        cur_row += 1
    rows = cur.execute("SELECT * FROM all_completed_tasks").fetchall()
    for row in rows:
        tag = "even" if cur_row % 2 == 0 else "odd"
        tree.insert("", tk.END, values=(row[0], row[1], row[2], f"{row[6]:02d}/{row[7]:02d}/{row[8]:02d} - {row[9]}", row[11], row[12]), tags=(tag))
        cur_row += 1
    conn.commit()