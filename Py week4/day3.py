# Parametro URL
# Query param

from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def home():
#     return "Home page"
# 
# @app.get("/pathpara/{id}")
# def get_id(id: int):
#     return {"path para": id}
# 
# @app.get("/querypara/")
# def get_str(nome: str):
#     return {"in query": nome}

@app.get ("/calcolatrice/somma")
def somma(a: float, b: float):
    somma= a+b
    return {"risultato": somma} 
