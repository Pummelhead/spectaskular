from db import conn
from db import cur

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