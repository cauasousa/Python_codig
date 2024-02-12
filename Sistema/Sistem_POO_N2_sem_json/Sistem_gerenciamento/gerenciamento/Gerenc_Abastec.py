import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR
from classes.P_Abastecimento import Abastecimento

class Gerenciamento_Abastecimento(GR.Gerenciamento_N1):

    def __init__(self, data_b, cod) -> None:
        super().__init__(data_b, cod)
        
    def total_abast(self):
        total = 0.0
        for i in self._data_base.values():
            total += float(i.valor)
        
        if(total == 0.0):
            print('\t\t\033[1;31mNão Houve Cadastro de Abastecimento\033[m')
        else:
            print("\t\t\033[1;34mTotal gasto com abastecimento ", total, '\033[m')