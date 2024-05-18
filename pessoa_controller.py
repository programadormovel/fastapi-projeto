import pandas as pd
from pessoa import Pessoa
from conexao import Conexao

class PessoaController:

    async def getNomePessoa(nome:str) -> dict:
        conexao = Conexao().conectar()
        cursor = conexao.cursor()
        print(nome)
        sql = f"SELECT `id`, `nome` , `email`, `mensagem` FROM `miniprojeto`.`mensagens` WHERE `nome`='{nome}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        columns = ('id', 'nome', 'email', 'mensagem')
        print(result)
        print(type(result))
        dados= pd.DataFrame(result, columns=columns)
        print(dados)
        print(dados.info())
        cursor.close()
        Conexao().desconectar(cursor)
        return dados.to_dict()

    async def setPessoa(pessoa: Pessoa) -> dict:
        pessoa_local = Pessoa(pessoa.nome, pessoa.email, pessoa.mensagem)
        
        conexao = Conexao().conectar()
        cursor = conexao.cursor()
        sql = f"INSERT INTO `miniprojeto`.`mensagens` (`nome`, `email`, `mensagem`) VALUES ('{pessoa_local.nome}', '{pessoa_local.email}', '{pessoa_local.mensagem}')"
        try:
            res = cursor.execute(sql) 
            if res <= 0:
                return {"message":"Dados não inseridos!"}
        except:
            return {"message":"Falha na gravação da pessoa"}
        finally:
            cursor.close()
            conexao.commit()
            Conexao().desconectar(cursor)
        
        return {"message":"Pessoa " + pessoa_local.nome + ' inserida com sucesso!'}