from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Sua API está funcionando!"}

@app.post("/calcular")
def calcular(a: float, b: float, operacao: str):

    if operacao == "soma":
        resultado = a + b

    elif operacao == "subtracao":
        resultado = a - b

    elif operacao == "multiplicacao":
        resultado = a * b

    elif operacao == "divisao":
        if b == 0:
            return {"erro": "Divisão por zero!"}
        resultado = a / b

    else:
        return {"erro": "Operação inválida!"}

    return {
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": resultado
    }