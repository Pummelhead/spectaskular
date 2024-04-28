import sqlite3
from datetime import datetime



conn = sqlite3.connect("database.db")
cur = conn.cursor()



cur.execute(f'''CREATE TABLE IF NOT EXISTS all_pending_tasks 
            (
            task TEXT PRIMARY KEY,
            description TEXT,
            priority INTEGER,
            display_month INTEGER DEFAULT {datetime.now().month},
            display_day INTEGER DEFAULT {datetime.now().day},
            display_year INTEGER DEFAULT {int(datetime.now().strftime("%y"))},
            display_time TEXT,
            due_month INTEGER DEFAULT 0,
            due_day INTEGER DEFAULT 0,
            due_year INTEGER DEFAULT 0,
            due_time TEXT DEFAULT "-:-",
            completed BOOLEAN DEFAULT false,
            frequency_step INTEGER,
            frequency_step_type TEXT
            )''')
cur.execute(f'''CREATE TABLE IF NOT EXISTS all_completed_tasks 
            (
            task TEXT PRIMARY KEY,
            description TEXT,
            priority INTEGER,
            display_month INTEGER DEFAULT {datetime.now().month},
            display_day INTEGER DEFAULT {datetime.now().day},
            display_year INTEGER DEFAULT {int(datetime.now().strftime("%y"))},
            display_time TEXT,
            due_month INTEGER DEFAULT 0 DEFAULT 0,
            due_day INTEGER DEFAULT 0,
            due_year INTEGER DEFAULT 0,
            due_time TEXT DEFAULT "-:-",
            completed BOOLEAN,
            frequency_step INTEGER,
            frequency_step_type TEXT
            )''')
apt_count = cur.execute("SELECT COUNT(*) FROM all_pending_tasks").fetchone()[0]
if apt_count == 0:
    cur.execute(f"INSERT OR IGNORE INTO all_pending_tasks (task, description, priority) VALUES (?, ?, ?)", ("Task Example", "Description Example", "5"))
act_count = cur.execute("SELECT COUNT(*) FROM all_completed_tasks").fetchone()[0]
if act_count == 0:
    cur.execute(f"INSERT OR IGNORE INTO all_completed_tasks (task, description, priority) VALUES (?, ?, ?)", ("Task Example (Completed)", "Description Example", "5"))
cur.execute('''CREATE TABLE IF NOT EXISTS all_created_tables (name TEXT)''')
conn.commit()
