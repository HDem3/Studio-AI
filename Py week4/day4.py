# Modello dati
# Post endpoint

from fastapi import FastAPI
from pydantic import BaseModel

class Utente(BaseModel):
    nome: str
    eta: int


app = FastAPI()

@app.post("/utente")
def crea_utente(user : Utente):
    return { "msg":f"ciao {user.nome}" }

