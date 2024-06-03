import joblib

from fastapi import FastAPI, responses

from pydantic import BaseModel

class previsaoCasaRequest(BaseModel):
    tamanho : int
    quartos : int
    n_vagas : int

class previsaoCasaResponse(BaseModel):
    preco_estimado: float

app = FastAPI()

modelo = joblib.load("modelo_casas.pkl")

@app.post("/prever/", response_model=previsaoCasaResponse)
def prever_preco(casa: previsaoCasaRequest):
    
    dados_entrada = [[casa.tamanho, casa.quartos, casa.n_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    return {
        "preco_estimado" :round(preco_estimado,2)
    }
    
