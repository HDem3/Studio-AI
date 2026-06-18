import jwt
import bcrypt
import sqlite3
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends, HTTPException, status

from pydantic import BaseModel
from passlib.context import CryptContext

#========================
# Configurations
#========================
app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"],bcrypt__rounds=11, deprecated="auto")


JWT_SECRET = "your_jwt_secret_key"
JWT_ALGORITHM = "HS256"
JWT_EXPIRE_MINUTES = 30


#========================
# Database Functions
#========================
DB_NAME= "users.db"
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


#========================
# Password hashing
#========================
def hash_password(password: str) -> bytes:
    salt= bcrypt.gensalt(11)
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password: str, hashed_pwd: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_pwd.encode())

# model for user
class User(BaseModel):
    username: str
    password: str

#========================
# JWT Token Generation
#========================
def create_token(data: dict)-> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token= jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def decode_token(token: str)->dict:
    try: 
        payload= jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
#========================
# API Endpoints
#========================
@app.post("/login")
def login(form_data:User):
    conn= get_db()
    cur= conn.cursor()

    cur.execute(
        'SELECT * FROM users WHERE username = ?',
        (form_data.username,)
    )
    db_user= cur.fetchone()

    cur.close()
    conn.close()

    if db_user and verify_password(form_data.password, db_user["hashed_pwd"]):
        token_data = {"sub": db_user["username"]}
        token = create_token(token_data)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    

    