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
    ris= a+b
    return {"risultato": ris} 

@app.get ("/calcolatrice/sottrazione")
def sottrazione(a: float, b: float):
    ris= a-b
    return {"risultato": ris}

@app.get ("/calcolatrice/moltiplicazione")
def moltiplicazione(a: float, b: float):
    ris= a*b
    return {"risultato": ris}

@app.get ("/calcolatrice/divsione")
def divsione(a: float, b: float):
    if b==0: return "Non divisibile per 0"
    else: 
        ris= a/b
        return {"risultato": ris}


