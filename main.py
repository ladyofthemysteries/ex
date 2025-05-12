from fastapi import FastAPI
app = FastAPI()

@app.get('/saudacao')
def saudacao():
    return {"mensagem": "Bom dia!"}

@app.get('/tudobem')
def tudobem():
    return {"mensagem": "oi, tudo bem?"}
