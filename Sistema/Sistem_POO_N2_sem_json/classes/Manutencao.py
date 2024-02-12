from classes.P_Veiculo import Veiculo

class Manutencao:
    def __init__(self, custo : float, tipo : str, data : str, veiculo : Veiculo):
        self.__custo = custo
        self.__tipo = tipo
        self.__data = data
        self.__veiculo = veiculo


    @property
    def custo(self):
        return self.__custo