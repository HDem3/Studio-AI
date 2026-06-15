import sqlite3

conn= sqlite3.connect("studenti.db")
cur= conn.cursor()

class OutRange(Exception): # non uso print perche se no melo stampa anche se non voglio
    def __init__(self,min,max):
        super().__init__(f"Errore, il numero dev'essere tra {min} e {max}")
    
def controllo(a, min , max):
    if a<min or a>max:
        raise OutRange(min,max)
    
def inserisci(n: str,c: str,v: int):
    cur.execute(
        "INSERT INTO studenti(nome, cognome, voto) "
        "VALUES(?,?,?)",(n,c,v)
    )
    conn.commit()

def modifica(id: int, n: str,c: str,v: int):
    cur.execute(
        "UPDATE studenti SET nome=?, cognome=?, voto=? " 
        "WHERE id=?",(n,c,v,id)
    )
    conn.commit()

def elimina(id: int):
    cur.execute(
        "DELETE FROM studenti WHERE id=?",(id,)
    )
    conn.commit()



esci= True

cur.execute(
    "CREATE TABLE IF NOT EXISTS studenti("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "nome TEXT, "
    "cognome TEXT, "
    "voto INTEGER)"
)
conn.commit()


while (esci):
    print("STUDENTI DB")
    print("1)Inserisci studente")
    print("2)Modifica studente")
    print("3)Elimina studente")
    print("4)Esci")
    try:
        scelta= int(input("Scegli un'opzione: "))
        controllo(scelta,1,4)

    except ValueError:
        print("Scelta non valida")
    except OutRange as e:
        print(e)
        print()
    else:
        
        if scelta== 1:
            inserisci('HDEM','HUANG',20)
        elif scelta== 2:
            modifica(3,'HDEM','HUANG',28)
        elif scelta== 3:
            elimina(1)
        elif scelta== 4:
            cur.close()
            conn.close()
            esci= False

