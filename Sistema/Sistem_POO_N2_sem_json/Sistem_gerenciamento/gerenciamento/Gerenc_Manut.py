import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR
from classes.Manutencao import Manutencao

class Gerenc_Manutencao(GR.Gerenciamento_N1):
    
    def __init__(self, data_b, cod) -> None:
        super().__init__(data_b, cod)
        
    def total_manut(self):
        total = 0.0
        
        for i in self._data_base.values():
            total += float(i.custo)
        
        if(total == 0):
            print("\t\t\033[1;31mNão Houve Cadastro de Manutenção\033[m")
        else:
            print("\t\t\033[1;34mTotal gasto com manutenção ", total, '\033[m')