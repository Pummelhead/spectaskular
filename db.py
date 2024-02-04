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
            frequency_step_type NULL,
            complete INTEGERT
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
            frequency_step_type NULL,
            complete INTEGERT
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS all_created_tables (name TEXT)''')
conn.commit()

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
            frequency_step_type NULL,
            complete INTEGERT
            )''')
    conn.commit()
    cur.execute(f"INSERT INTO all_created_tables (name) VALUES ('{create_table_name}')")
    conn.commit()

def delete_table():
    delete_table_name = input("Table to delete: ")
    cur.execute(f"DROP TABLE IF EXISTS '{delete_table_name}'")
    cur.execute(f"DELETE FROM all_created_tables WHERE name='{delete_table_name}'")
    conn.commit()

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
    conn.commit()

if __name__ == "__main__":
    create_table()
    create_table()
    create_table()
    add_task()
    add_task()
    add_task()
    delete_table()
    for row in cur.execute("SELECT name FROM all_created_tables ORDER BY name"):
        print(row)

cur.close()
conn.close()