from db import conn
from db import cur
import tkinter as tk
from datetime import datetime

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