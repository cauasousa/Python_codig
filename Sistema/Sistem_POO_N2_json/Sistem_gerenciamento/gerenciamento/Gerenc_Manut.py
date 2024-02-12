import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR

class Gerenc_Manutencao(GR.Gerenciamento_N1):
    
    def __init__(self, way) -> None:
        super().__init__(way)
        
    def total_manut(self):
        total = 0.0
        data = self.cnx.Data_base()
        if data == None:
            return
        
        for i in data.values():
            total += float(i["custo"])
        
        if(total == 0):
            print("\t\t\033[1;31mNão Houve Cadastro de Manutenção\033[m")
        else:
            print("\t\t\033[1;34mTotal gasto com manutenção ", total, '\033[m')