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

@app.post("/signup")
def signup(user: Utente):
    return {
        "msg": f"Benvenuto {user.nome}!",
        "email": user.email,
        "eta": user.eta
    }
