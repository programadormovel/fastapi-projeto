import uvicorn
from pessoa import Pessoa
from fastapi import FastAPI
from pessoa_controller import PessoaController

app = FastAPI()

@app.get("/pegar_nome_pessoa")
async def getNomePessoa(nome:str) -> dict:
    return await PessoaController.getNomePessoa(nome)

@app.post("/inserir_pessoa")
def setPessoa(pessoa: Pessoa) -> str:
    return PessoaController.setPessoa(pessoa)

if __name__ == "__main__":
    uvicorn.run(app, port=8087)
