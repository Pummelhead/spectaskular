import sqlite3



conn = sqlite3.connect("database.db")
cur = conn.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS all_pending_tasks 
            (
            task TEXT PRIMARY KEY,
            description TEXT,
            priority INTEGER,
            display_time NULL,
            due_time NULL,
            display INTEGER,
            frequency_step NULL,
            frequency_step_type NULL
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS all_completed_tasks 
            (
            task TEXT PRIMARY KEY,
            description TEXT,
            priority INTEGER,
            display_time NULL,
            due_time NULL,
            display INTEGER,
            frequency_step NULL,
            frequency_step_type NULL
            )''')
apt_count = cur.execute("SELECT COUNT(*) FROM all_pending_tasks").fetchone()[0]
cur.execute('''CREATE TABLE IF NOT EXISTS all_created_tables (name TEXT)''')
if apt_count == 0:
    cur.execute(f"INSERT OR IGNORE INTO all_pending_tasks (task, description, priority) VALUES (?, ?, ?)", ("Task Example", "Description Example", "High"))
conn.commit()
