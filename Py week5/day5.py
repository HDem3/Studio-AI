from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# connect database
DB_NAME= "tasks.db"
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
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY 
            titolo TEXT NOT NULL,
            descrizione TEXT,
            completato BOOLEAN NOT NULL DEFAULT 0
            )
        '''
    )
    conn.commit()
    cur.close()
    conn.close()

db_init()

# Model for task
class Task(BaseModel):
    titolo: str
    descrizione: str = None
    completato: bool = False

# Create a new task
@app.post("/tasks")
def create_task(task: Task):
    conn= get_db()
    cur= conn.cursor()

    cur.execute(
        'INSERT INTO tasks (titolo, descrizione, completato)'
        'VALUES (?, ?, ?)',
        (task.titolo, task.descrizione, task.completato)
    )
    conn.commit()
    cur.close()
    conn.close()

