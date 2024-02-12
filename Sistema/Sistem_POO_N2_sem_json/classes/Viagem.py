from classes.P_Veiculo import Veiculo
from classes.PMotorista import Motorista


class Viagem:    
    def __init__(self, origem:str, destino:str,  distancia:float , motorista : Motorista, veiculo : Veiculo):
        self.__destino = destino
        self.__origem = origem
        self.__distancia = distancia
        self.__motorista = motorista
        self.__veiculo = veiculo


    @property
    def destino(self):
        return self.__destino
    
    @destino.setter
    def destino(self, new):
        self.__destino = new
    
    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, new):
        self.__origem = new

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, new):
        self.__distancia = new

    @property
    def motorista(self):
        return self.__motorista

    @property
    def veiculo(self):
        return self.__veiculo