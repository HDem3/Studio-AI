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
    descrizione: str | None = None 
    completato: bool = False

class TaskUpdate(BaseModel):
    titolo: str | None = None
    descrizione: str | None = None 
    completato: bool | None = None

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

# Get all tasks
@app.get("/tasks")
def get_tasks():
    conn= get_db()
    cur= conn.cursor()
    
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    conn.commit()

    cur.close()
    conn.close()
    return [dict(task) for task in tasks]

# Delete a task by id
@app.delete("/tasks/{id}")
def delete_task(id: int):
    conn= get_db()
    cur= conn.cursor()
    
    cur.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    
    cur.close()
    conn.close()
    return {"status": "ok", "message": f"Task {task_id} eliminato"} 

# Update a task by id
@app.put("/tasks/{id}")
def update_task(id: int, task: TaskUpdate):
    conn= get_db()
    cur= conn.cursor()

    cur.execute('SELECT * FROM tasks WHERE id = ?', (id,))
    existing_task = cur.fetchone()

    if existing_task is None:
        cur.close()
        conn.close()
        return {"error": "Task not found"}
    
    # se il task non è None assegna il nuovo task altrimenti mantieni il vecchio task
    new_titolo = task.titolo if task.titolo is not None else existing_task["titolo"] 
    new_descrizione = task.descrizione if task.descrizione is not None else existing_task["descrizione"]
    new_completato = task.completato if task.completato is not None else existing_task["completato"]

    cur.execute(
        'UPDATE tasks SET titolo = ?, descrizione = ?, completato = ? WHERE id = ?',
        (new_titolo, new_descrizione, new_completato, id)
    )

    conn.commit()
    cur.close()
    conn.close()
    return {"status": "ok", "message": f"Task {id} aggiornato"}
