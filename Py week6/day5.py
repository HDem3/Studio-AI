from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import timedelta, datetime, timezone
from passlib.context import CryptContext
import sqlite3
import bcrypt
import jwt
#======================
# Configuration
#======================
JWT_SECRET = "your_jwt_secret_key"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = 30

app = FastAPI()
pwd_context= CryptContext(schemes=["bcrypt"], bcrypt__rounds=11, deprecated="auto")

#======================
# Database Functions
#======================
DB_NAME = "users.db"
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn= get_db()
    cur= conn.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY, 
                username TEXT NOT NULL UNIQUE,
                hashed_pwd TEXT NOT NULL)'''
        )
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                cmpleted BOOLEAN NOT NULL,
                user_id INTEGER NOT NULL)'''
    )
    conn.commit()

    cur.close()
    conn.close()

init_db()

#=======================
# Password hashing
#=======================
def pwd_hash(pwd: str) -> bytes:
    return pwd_context.hash(pwd)

def verify_pwd(current_pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(current_pwd, hashed_pwd)

# Model for user & task
class User(BaseModel):
    username: str
    password: str
class Task(BaseModel):
    title: str
    complete: int

#====================
# Token generation
#====================
def create_token(data: dict) -> str:
    to_encode= data.copy()
    expire= datetime.now(timezone.utc)+ timedelta(minutes= JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token= jwt.encode(to_encode, JWT_SECRET, algorithms= JWT_ALGORITHM)
    return token

def decode_token(token: str) -> dict:
    try:
        payload= jwt.decode(token, JWT_ALGORITHM, algorithms= [JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
#======================
# API Endpoint
#======================
@app.post("/signup")
def signup(user: User):
    