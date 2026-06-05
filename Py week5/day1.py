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

conn= sqlite3.connect("studenti.db")
cur= conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS studenti("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "nome TEXT,"
    "cognome TEXT,"
    "voto INTEGER)"
)

cur.execute("INSERT INTO studenti(nome,cognome,voto) "
            "VALUES('Dem','H','18')")

cur.execute("INSERT INTO studenti(nome,cognome,voto) "
            "VALUES('Fabio','M','28')")

conn.commit()
conn.close()

