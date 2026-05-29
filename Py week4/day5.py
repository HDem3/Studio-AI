# Task Manager API

# Funzioni:
# aggiungere task
# vedere task
# eliminare task
 
# Endpoints:
# GET /tasks
# POST /tasks
# DELETE /tasks


from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    describ: str

app = FastAPI()
ltask = []

@app.post("/creaTask")
def creaTask(task: Task):
    ltask.append(task)
    return {"msg": "task creata"}

@app.get("/visualizza")
def getTask():
    return {
        "Numero task" : len(ltask),
        **{
            f"task {i+1}": task
            for i, task in enumerate(ltask)
        } 
    }

@app.get("/visualizzaID/{task_id}")
def findTask(task_id: int):
    for task in ltask:
        if task.id == task_id:
            return task
    return {"errore": "task non trovata"}

@app.delete("/eliminaTask/{task_id}")
def deleteTask(task_id: int):
    for task in ltask:
        if task.id == task_id:
            ltask.remove(task)
            return {"msg": "task eliminata"}
    return {"errore": "task non trovata"}