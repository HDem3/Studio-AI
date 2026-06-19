#pip install fastapi uvicorn passlib[bcrypt] 

# Utenti
# register
# login
# 🔑 Sicurezza
# password hashata
# JWT token
# 📋 Task
# crea task (solo loggati)
# vedi task SOLO tuoi
# elimina task SOLO tuoi

from fastapi import FastAPI, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from pydantic import BaseModel
import sqlite3






#======================
# Config
#======================
app= FastAPI()
pwd_context= CryptContext(schemes=["bcrypt"], bcrypt__rounds=11, deprecated="auto")

JWT_SECRET= "your_jwt_secret_key"
JWT_ALGORITHM= "HS256"
JWT_EXPIRED_MINUTES= 30

#=====================
# BD Functions
#=====================
DB_NAME= "users.db"
def get_db():
    conn= sqlite3.connect(DB_NAME)
    conn.row_factory= sqlite3
    conn.execute("PRAGMA foreign_key= ON")
    return conn

def init_db():
    conn= get_db()
    cur= conn.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS user(
                userID INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL)"""
    )
    cur.execute(
        """CREATE TABLE IF NOT EXISTS task(
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0,
                userID INTEGER NOT NULL,
                FOREIGN KEY (userID) REFERENCES user(userID) ON DELETE CASCADE)"""
    )# prima creare colonna poi collegare FK 
    conn.commit()
    cur.close()
    conn.close()

init_db()





