#pip install fastapi uvicorn passlib[bcrypt] pyjwt

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
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from pydantic import BaseModel
import sqlite3
import jwt






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
    conn.row_factory= sqlite3.Row
    conn.execute("PRAGMA foreign_keys= ON")
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

# Model for User
class User(BaseModel):
    username: str
    password: str
# Model for Task
class Task(BaseModel):
    task: str
    completed: bool

#=====================
# Pass Hashing
#=====================
def hash_pwd(pwd: str)-> str:
    return pwd_context.hash(pwd)

def verify_pwd(current_pwd: str, hashed_pwd)-> bool:
    return pwd_context.verify(current_pwd, hashed_pwd)

#=====================
# Token Generate
#=====================
# token formato da dict= (data[user] + exp) + firma + algorithm
def create_token(data: dict) -> str: # encode crea token da dict un str
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRED_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def decode_token(token: str) -> dict: # decode token da str a dict
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token scaduto")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token non valido")
    



