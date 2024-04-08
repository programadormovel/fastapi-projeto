import pymysql

class Conexao():
    
    cursor = pymysql.cursors
    
    def __init__(self):
        self.host='localhost'
        self.port=3306
        self.user='root'
        self.password='123456'
        self.database='miniprojeto'

    def conectar(self):
        try:
           return pymysql.connect(host=self.host,  
                                    port=self.port, 
                                    user=self.user, 
                                    password=self.password, 
                                    database=self.database, 
                                    cursorclass=pymysql.cursors.DictCursor)
        except pymysql.ConnectionError:
            return False
        
    def desconectar(self, cursor):
        try:
            cursor.close()
        except pymysql.ConnectionError:
            return False
        

        

