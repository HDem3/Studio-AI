import sqlite3

conn= sqlite3.connect("rubrica.db")
cur= conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS "
    "rubrica(ID INTEGER PRIMARY KEY AUTOINCREMENT, "
    "nome TEXT, "
    "email TEXT, "
    "telefono INTEGER)"
)
cur.execute(
    "INSERT INTO rubrica(nome, email, telefono) "
    "VALUES(?,?,?)",("HDEM","hdem@example.com",1234567890)
)
conn.commit()


cur.close()
conn.close()
