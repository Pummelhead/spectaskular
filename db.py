import sqlite3



conn = sqlite3.connect("database.db")
cur = conn.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS all_pending_tasks 
            (
            task TEXT,
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
            task TEXT,
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
conn.commit()
