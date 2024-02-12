import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR

class Gerenciamento_Motorista(GR.Gerenciamento_N3):

    def __init__(self, way):
        super().__init__(way)
        

    def editar(self, opc:int, cod, novo):
        """
        OPC:\n
            1 - nome\n
            2 - RG\n
            3 - CNH
        """
        data = self.cnx.Data_base()
        if data == None: return

        motorista = data.get(cod)
        if(motorista == None):
            print("\033[1;31mUSUA NOT FIND, \033[m")
            return 
        if(opc == 1):
            motorista["nome"] = novo
        if(opc == 2):
            motorista["rg"] = novo
        if(opc == 3):
            motorista["cnh"] = novo
            
        self.cnx.Update(motorista, cod)