from classes.P_Veiculo import Veiculo

class Abastecimento:
    def __init__(self, veiculo:Veiculo, valor:float, data:str, quantidade:int):
        self.__valor = valor
        self.__data = data
        self.__veiculo = veiculo
        self.__quantidade = quantidade


    @property
    def valor(self):
        return self.__valor