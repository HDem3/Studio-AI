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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Task(BaseModel):
    describ: str

app = FastAPI()
ltask = []
contatore = 1

@app.post("/creaTask")
def creaTask(task: Task):
    global contatore 
    new_task= {"id": contatore, "describ": task.describ}
    ltask.append(new_task)
    contatore+=1
    return {"msg": "task creata", ** new_task}


@app.get("/visualizza")
def getTask():
    risultato = {"totale_tasks": len(ltask)}
    for t in ltask:
        risultato[f"task {t['id']}"] = t["describ"]
    return risultato

@app.get("/visualizzaID/{task_id}")
def findTask(task_id: int):
    for task in ltask:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="task non trovata")

@app.delete("/eliminaTask/{task_id}")
def deleteTask(task_id: int):
    for task in ltask:
        if task["id"] == task_id:
            ltask.remove(task)
            return {"msg": "task eliminata"}
    raise HTTPException(status_code=404, detail="task non trovata")