# Password Manager base

# Funzioni:
# Salvare password
# Leggere password
# Ricercare account

# Usa:
# file
# funzioni
# dizionari
# try/except

import json
import os

def salva(dati):
    with open("password.json", "w") as f:
        json.dump(dati, f, indent=4)

def leggi():
    try:
        with open("password.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Errore, file non trovato")
        return {3}
def newPass():
    dati= leggi()
    
    acc= input("Account: ").strip() #serve a prendere input senza spazi
    pw= input("Password: ").strip()

    dati[acc]= pw
    
    salva(dati)
    print("Password salvata!")
    
def cerca(acc):
    if acc in leggi():
        print(f"Account: {acc}, Password: {leggi()[acc]}")
    else:
        print("Account non trovato")

class OutRange(Exception):
    def __init__(self,min,max):
        super().__init__(f"Errore, il numero dev'essere tra {min} e {max}")

def controllo(a, min , max):
    if a<min or a>max:
        raise OutRange(min,max)

print("Password Manager")
print("1) Salva Password")
print("2) Leggi Password")
print("3) Cerca account")


errore= False
while(not errore):
    try:
        scelta= int(input("scelta: "))
        controllo(scelta,1,3)
    except ValueError:
        print("Errore, scelta non valida")
    except OutRange as e:
        print(e)
    else: 
        errore= True

if scelta==1:
    newPass()
elif scelta==2:
    for acc, pw in leggi().items():
        print(f"Account: {acc} | Password: {pw}")
        print("-" * 30)
elif scelta==3:
    cerca(input("Account da cercare: ").strip())