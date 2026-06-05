import sqlite3

conn = sqlite3.connect("todolist.db")
cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS todolist("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "task TEXT)"
)

cur.execute("INSERT INTO todolist(task) VALUES ('andare parco')")
cur.execute("INSERT INTO todolist(task) VALUES ('palestra')")

conn.commit()
conn.close()
