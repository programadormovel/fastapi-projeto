from pydantic import BaseModel, PrivateAttr

class Pessoa(BaseModel):
    "Classe modelo para criação do objeto Pessoa."
    
    __nome: str = PrivateAttr()
    __email: str = PrivateAttr()
    __mensagem: str = PrivateAttr()
    
    def __init__(self, nome: str, email: str, mensagem: str) -> None:
        super().__init__()
        self.__nome = nome
        self.__email = email
        self.__mensagem = mensagem

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def email(self):
        a = []
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
        
    @property
    def mensagem(self):
        return self.__mensagem
    
    @mensagem.setter
    def mensagem(self, mensagem):
        self.__mensagem = mensagem