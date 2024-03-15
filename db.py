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
cur.execute('''CREATE TABLE IF NOT EXISTS all_tasks (task TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS all_created_tables (name TEXT)''')
cur.execute(f"INSERT OR IGNORE INTO all_pending_tasks (task, description, priority) VALUES (?, ?, ?)", ("Task", "description", "priority"))
cur.execute(f"INSERT OR IGNORE INTO all_tasks (task) VALUES ('task')")
conn.commit()
