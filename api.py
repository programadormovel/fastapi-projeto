import uvicorn
import pymysql
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI

from conexao import Conexao

app = FastAPI()

class Pessoa(BaseModel):
    nome: str = ""
    sobrenome: str = ""

    def set_nome(self, nome):
        self.nome = nome
        
    def get_nome(self):
        return self.nome

pessoa_local = Pessoa()

@app.get("/pegar_nome_pessoa")
async def getNomePessoa(nome:str) -> dict:
    conexao = Conexao()
    cursor = conexao.conectar().cursor()
    sql = f"SELECT `id`, `nome` , `email`, `mensagem` FROM `miniprojeto`.`mensagens` WHERE `nome`=%s"
    cursor.execute(sql, ({nome}))
    result = cursor.fetchall()
    columns = ('id', 'nome', 'email', 'mensagem')
    print(result)
    print(type(result))
    dados= pd.DataFrame(result, columns=columns)
    print(dados)
    conexao.desconectar(cursor)
    return dados.to_dict()

#'SELECT `id`, `nome` , `email`, `mensagem` FROM `miniprojeto`.`mensagens` WHERE `nome`='Adriano''

@app.post("/inserir_pessoa")
async def setPessoa(pessoa: Pessoa) -> str:
    pessoa_local.set_nome(pessoa.nome)
    pessoa_local.set_email(pessoa.email)
    pessoa_local.set_mensagem(pessoa.mensagem)
    conexao = Conexao()
    cursor = await conexao.conectar().cursor()
    sql = "INSERT INTO `mensagens` (`nome`, `email`, `mensagem`) VALUES (%s, %s, %s)"
    await cursor.execute(sql, (pessoa_local.nome, pessoa_local.email, pessoa_local.mensagem))   
    conexao.desconectar()
    return "Pessoa " + pessoa_local.get_nome() + ' inserida com sucesso!'

if __name__ == "__main__":
    uvicorn.run(app, port=8087)