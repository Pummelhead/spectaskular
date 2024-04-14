import sqlite3



conn = sqlite3.connect("database.db")
cur = conn.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS all_pending_tasks 
            (
            task TEXT PRIMARY KEY,
            description TEXT,
            priority INTEGER,
            display_time TEXT,
            due_time TEXT,
            completed BOOLEAN DEFAULT false,
            frequency_step INTEGER,
            frequency_step_type TEXT
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS all_completed_tasks 
            (
            task TEXT PRIMARY KEY,
            description TEXT,
            priority INTEGER,
            display_time TEXT,
            due_time TEXT,
            completed BOOLEAN,
            frequency_step INTEGER,
            frequency_step_type TEXT
            )''')
apt_count = cur.execute("SELECT COUNT(*) FROM all_pending_tasks").fetchone()[0]
if apt_count == 0:
    cur.execute(f"INSERT OR IGNORE INTO all_pending_tasks (task, description, priority) VALUES (?, ?, ?)", ("Task Example", "Description Example", "High"))
act_count = cur.execute("SELECT COUNT(*) FROM all_completed_tasks").fetchone()[0]
if act_count == 0:
    cur.execute(f"INSERT OR IGNORE INTO all_completed_tasks (task, description, priority) VALUES (?, ?, ?)", ("Task Example (Completed)", "Description Example", "High"))
cur.execute('''CREATE TABLE IF NOT EXISTS all_created_tables (name TEXT)''')
conn.commit()
