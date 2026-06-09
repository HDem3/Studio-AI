import sqlite3

conn= sqlite3.connect("studenti.db")
cur= conn.cursor()



print("STUDENTI DB")
print("1)Inserisci studente")
print("2)Modifica studente")
print("3)Elimina studente")
scelta= int(input("Scegli un'opzione: "))
