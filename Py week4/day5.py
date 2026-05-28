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
from pydantic import BaseModel, EmailStr # formatto email

class Task(BaseModel):
    id: int
    describ: str

app = FastAPI()

ltask=[]

@app.post("/creaTask")
def creaTask(task : Task):
    ltask.append(task)
    return {"msg": "task creata"}

@app.get("/visualizza")
def getTask(task: Task):
    return task

@app.get("/visualizzaID")
def getTaskID(task: Task, toGet: Task[id]):
    for toGet in task.item():
        return task[toGet]

@app.delete("/visualizzaID")
def deleteTaskID(task: Task, toDelete: Task[id]):
    for toDelete in task.item():
        return task[toDelete]
