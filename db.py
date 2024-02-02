import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS categories (name TEXT, description TEXT)''')
conn.commit

cur.close()
conn.close()