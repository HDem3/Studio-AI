from fastapi import FastAPI
from pydantic import BaseModel
import bcrypt
import sqlite3

#----------------------------- Database Functions ----------------------------
DB_NAME= "users.db"
# connect database
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
#-------------------------------------------------------------------------



# ----------------------------- Password hashing ------------------------------- 
def hash_password(password: str) -> bytes:
    salt= bcrypt.gensalt(11)
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password: str, hashed_pwd: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_pwd.encode())

# Model for user
class User(BaseModel):
    username: str
    password: str

#----------------------------- API Endpoints ----------------------------
app= FastAPI()
# Login endpoint
@app.post("/login")
def login(user: User):
    conn= get_db()
    cur= conn.cursor()

    cur.execute(
        'SELECT * FROM users WHERE username = ?',
        (user.username,)
    )
    db_user= cur.fetchone()

    cur.close()
    conn.close()

    if db_user and verify_password(user.password, db_user["hashed_pwd"]):
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}