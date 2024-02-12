from classes.P_Veiculo import Veiculo
import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR


class Gerenciamento_Veiculo(GR.Gerenciamento_N3):

    def __init__(self, bve, cod, quant):
        super().__init__(bve, cod, quant)


    def editar(self, opc:int, Objeto_Find : Veiculo, novo):
        """
            EDITAR\n
            1 - Marca     || 4 - Chassi\n
            2 - Modelo    || 5 - Cor\n
            3 - Ano 
        """
        if(Objeto_Find == None):
            print("\t\t\033[1;31mUSUA NOT FIND\033[m")
            return 
        if (7 > opc) and (opc > 0):
            if(opc == 1):
                Objeto_Find.marca = novo
            if(opc == 2):
                Objeto_Find.modelo = novo
            if(opc == 3):
                Objeto_Find.ano = novo
            if(opc == 4):
                Objeto_Find.chassi = novo
            if(opc == 5):
                Objeto_Find.cor = novo

    def see_km_veic(self, placa):
        ref = self.find(placa)
        if None != ref:
            print("\t\t\033[1;34;40mThe Km is ", ref.km,'\033[m')
        else:
            print("\t\t\033[1;31mNot Find Veiculo!\033[m")

    def maior_Km_veiculo(self):
        placa = list()
        Km_maior = 0
        
        for i in self._data_base.values():
            if(i.km == Km_maior):
                placa.append(i.placa)
            elif (i.km > Km_maior):
                Km_maior = i.km
                placa.clear()
                placa.append(i.placa)

        if len(placa) != 0:
            print('\t\t\033[1;34mO(s) Veiculo(s) da(s) Placa(s): ', end='')

            design = 0
            for i in placa:
                print(i, end=' ')
                design+=1
                if(len(placa) > design and len(placa) > 0):
                    print(',', end=' ')
                    

            print('Rodou ', Km_maior, 'KM', '\033[m')
        else:
            print('\t\t\033[1;31mNão Possui Viagem Cadastrada\033[m')