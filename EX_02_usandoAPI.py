from fastapi import FastAPI

import random

app = FastAPI()

@app.get("/gerar_numero_aleatorio")
def gerar_numero_aleatorio():
    num = random.randint(1, 10)
    return {"data": num} # num

@app.get('/outro_recurso')
def pegar_recurso():
    return "hello world"
