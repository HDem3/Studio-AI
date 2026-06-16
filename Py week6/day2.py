from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import bcrypt


#----------------------------- Database setup ----------------------------
# connect database
DB_NAME= "users.db"
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# create table if not exist
def db_init():
    conn= get_db()
    cur= conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY, 
            username TEXT NOT NULL UNIQUE,
            hashed_pwd TEXT NOT NULL
            )
        '''
    )
    conn.commit()
    cur.close()
    conn.close()

db_init()
#------------------------------------------------------------------------------

#----------------------------- Password hashing -------------------------------
def hash_password(password: str) -> bytes:
    salt= bcrypt.gensalt(11)
    return bcrypt.hashpw(password.encode(), salt)
#------------------------------------------------------------------------------

# Model for user
class User(BaseModel):
    username: str
    password: str


#----------------------------- API Endpoints ----------------------------
app= FastAPI()

# Create a new user
@app.post("/signup")
def signup(user: User):
    hashed_pwd= hash_password(user.password).decode()

    conn= get_db()
    cur= conn.cursor()

    cur.execute(
        'INSERT INTO users (username, hashed_pwd)'
        'VALUES (?, ?)',
        (user.username, hashed_pwd)
    )
    conn.commit()

    cur.close()
    conn.close()
    return {"message": f"User {user.username} created successfully."}
