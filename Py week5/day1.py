import sqlite3

conn = sqlite3.connect("mydb.db")
cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS users("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT)"
)

cur.execute("INSERT INTO users(name) VALUES ('Alice')")
cur.execute("INSERT INTO users(name) VALUES ('Bob')")

conn.commit()
conn.close()
