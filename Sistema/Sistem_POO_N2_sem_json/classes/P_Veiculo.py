
class Veiculo:
    
    def __init__(self, marca, modelo, ano, placa, chassi, cor, Km) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__placa = placa
        self.__chassi = chassi
        self.__cor = cor
        self.__km = Km
        
        

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, new):
        self.__marca = new
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, new):
        self.__modelo = new
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, new):
        self.__ano = new

    @property
    def placa(self):
        return self.__placa

    @property
    def chassi(self):
        return self.__chassi
    
    @chassi.setter
    def chassi(self, new):
        self.__chassi = new
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, new):
        self.__cor = new
    
    @property
    def km(self):
        return self.__km
    
    @km.setter
    def km(self, new):
        self.__km = new
    
    @property
    def veiculo_data(self):
        return self.__veiculo_data
    
    @veiculo_data.setter
    def veiculo_data(self, new):
        self.__veiculo_data = new