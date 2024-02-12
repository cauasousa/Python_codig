import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR

class Gerenciamento_Abastecimento(GR.Gerenciamento_N1):

    def __init__(self,way) -> None:
        super().__init__(way)

    def total_abast(self):
        total = 0.0
        data = self.cnx.Data_base()
        if data == None: 
            return

        for i in data.values():
            total += float(i["valor"])
        
        if(total == 0.0):
            print('\t\t\033[1;31mNão Houve Cadastro de Abastecimento\033[m')
        else:
            print("\t\t\033[1;34mTotal gasto com abastecimento ", total, '\033[m')