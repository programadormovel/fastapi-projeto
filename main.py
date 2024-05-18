import uvicorn
from pessoa import Pessoa
from fastapi import FastAPI
from pessoa_controller import PessoaController
from mangum import Mangum
import time

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def principal() -> None:
    while True:
        verifica_se_existe_mensagem()

@app.get("/pegar_nome_pessoa")
async def getNomePessoa(nome:str) -> dict:
    return await PessoaController.getNomePessoa(nome)

@app.post("/inserir_pessoa")
async def setPessoa(pessoa: Pessoa) -> str:
    return await PessoaController.setPessoa(pessoa)

def verifica_se_existe_mensagem():
    print('buscando mensagens...')

def recebePessoa(pessoa: Pessoa) -> str:
    return PessoaController.setPessoa(pessoa)

if __name__ == "__main__":
    print('rodando')
    uvicorn.run("main:app", port=8087, workers=2, reload=True)
    principal()
    
    
        

