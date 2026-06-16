#SALVA I DATI DAL SERVER AL DATABASE SQLITE3
    
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

#------------------------
#-----SETUP DATABASE-----
#------------------------

DB_NAME = 'rubrica.db'

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# CREA TABELLA SE NON ESISTE
def db_init():
    conn= get_db()
    cur= conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS rubrica
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefono TEXT NOT NULL)
        '''
    )

#------------------------
#-----MODELLI DATI-------
#------------------------

class User(BaseModel):
    nome: str
    email: str
    telefono: int

#------------------------
#-----API ENDPOINTS------
#------------------------

# POST/user -> crea utente
@app.post("/user")
def create_user(user: User):
    conn= get_db()
    cur= conn.cursor()

    cur.execute(
        '''
        INSERT INTO rubrica (nome, email, telefono)
        VALUES (?, ?, ?)
        ''', 
        (user.nome, user.email, user.telefono)
    )
    conn.commit()
    
    cur.close()
    conn.close()
    return {"message": "User created successfully"}

# GET/users -> lista utenti
@app.get("/users")
def list_users():
    conn= get_db()
    cur= conn.cursor()

    cur.execute('SELECT * FROM rubrica')
    rows = cur.fetchall()
    
    cur.close()
    conn.close() 
    return [dict(row) for row in rows]

# DELETE/user/{id} -> elimina utente
@app.delete("/user/{id}")
def delete_user(id: int):
    conn= get_db()
    cur= conn.cursor()

    cur.execute('DELETE FROM rubrica WHERE id = ?', (id,))
    conn.commit()

    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Utente non trovato")
    
    cur.close()
    conn.close() 
    return {"status": "ok", "message": f"Utente {id} eliminato"}