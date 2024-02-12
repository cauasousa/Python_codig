class Motorista:
    def __init__(self, nome, cpf, rg, cnh) -> None:
        self.__nome = nome 
        self.__cpf = cpf
        self.__rg = rg
        self.__cnh = cnh

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, new):
        self.__nome = new
    
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def rg(self):
        return self.__rg
    
    @rg.setter
    def rg(self, new):
        self.__rg = new
    
    @property
    def cnh(self):
        return self.__cnh
    
    @cnh.setter
    def cnh(self, new):
        self.__cnh = new