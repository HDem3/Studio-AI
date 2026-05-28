# Modello dati
# Post endpoint

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr # formatto email

class Utente(BaseModel):
    nome: str
    email: EmailStr
    eta: int


app = FastAPI()

# @app.post("/utente")
# def crea_utente(user : Utente):
#     return { "msg":f"ciao {user.nome}" }
 

# Registrazione utenti API
# Dati:
# nome
# email
# età

lista=[]

@app.post("/signup")
def signup(user: Utente):
    lista.append(user)
    return {
        "msg": f"Benvenuto {user.nome}!",
        "email": user.email,
        "eta": user.eta
    }

@app.get("/utenti")
def get_utenti():
    return {
        "Numero Utenti" : len(lista),
        **{
            f"utente {i+1}": user
            for i, user in enumerate(lista)
        } 

    }   