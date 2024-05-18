import pymysql
import boto3

class Conexao():
    
    cursor = pymysql.cursors
    
    def __init__(self):
        self.host='sql10.freesqldatabase.com'
        self.port=3306
        self.user='sql10698414'
        self.password='qhuJPDhLAa'
        self.database='sql10698414'

    def conectar(self):
        try:
           conexao = pymysql.connect(host=self.host,  
                                    port=self.port, 
                                    user=self.user, 
                                    password=self.password, 
                                    database=self.database, 
                                    cursorclass=pymysql.cursors.DictCursor)
           return conexao
        except:
            return False
        
    def desconectar(self, cursor):
        try:
            cursor.close()
        except:
            return False
        
    def conectar_aws_sqs(self):
        return boto3.client('sqs', region_name="us-east-2", 
                         aws_access_key_id="AKIAZQ3DOASBAGAEKDWJ",
                         aws_secret_access_key="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")

        

