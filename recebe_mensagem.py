import boto3
from conexao import Conexao

class RecebeMensagem:
    
    def __init__(self):
        pass
    
    async def receber_mensagem(self):
        conexao = Conexao()
        try:
            cliente = conexao.conectar_aws_sqs()
            print(cliente)

            FilaUrl = "https://sqs.us-east-2.amazonaws.com/654654178434/FilaTeste"

            resposta = cliente.receive_message(
                QueueUrl=FilaUrl,
                AttributeNames=[
                    'SentTimestamp'
                ],
                MessageAttributeNames=[
                    'All'
                ],
                MaxNumberOfMessages=1,
                VisibilityTimeout=0,
                WaitTimeSeconds=0
            )

            mensagem = resposta['Messages'][0]
            return mensagem
        except:
            print('erro ao conectar na AWS')
            return None
        
    
    