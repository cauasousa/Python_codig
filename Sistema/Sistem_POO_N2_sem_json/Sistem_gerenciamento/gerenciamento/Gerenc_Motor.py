import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR

from classes.PMotorista import Motorista

class Gerenciamento_Motorista(GR.Gerenciamento_N3):

    def __init__(self, data_b, cod, quant):
        super().__init__( data_b, cod, quant)
        

    def editar(self, opc:int, motorista:Motorista, novo):
        """
        OPC:\n
            1 - nome\n
            2 - RG\n
            3 - CNH
        """
        if(motorista == None):
            print("\033[1;31mUSUA NOT FIND, \033[m")
            return 
        if(opc == 1):
            motorista.nome = novo
        if(opc == 2):
            motorista.rg = novo
        if(opc == 3):
            motorista.cnh = novo
            