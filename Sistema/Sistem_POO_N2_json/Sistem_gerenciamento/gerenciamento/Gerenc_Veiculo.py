import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR

class Gerenciamento_Veiculo(GR.Gerenciamento_N3):

    def __init__(self, way):
        super().__init__(way)

    def editar(self, opc:int, cod, novo):
        """
            EDITAR\n
            1 - Marca     || 4 - Chassi\n
            2 - Modelo    || 5 - Cor\n
            3 - Ano 
        """
        data = self.cnx.Data_base()
        if data == None: return

        dict_find = data.get(cod)

        if(dict_find == None):
            print("\t\t\033[1;31mUSUA NOT FIND\033[m")
            return 
        if (7 > opc) and (opc > 0):
            if(opc == 1):
                dict_find["marca"] = novo
            if(opc == 2):
                dict_find["modelo"] = novo
            if(opc == 3):
                dict_find["ano"] = novo
            if(opc == 4):
                dict_find["chassi"] = novo
            if(opc == 5):
                dict_find["cor"] = novo

            self.cnx.Update(dict_find, cod)

    def see_km_veic(self, placa):
        
        ref = self.find(placa)
        if None != ref:
            print("\t\t\033[1;34;40mThe Km is ", ref["km"],'\033[m')
        else:
            print("\t\t\033[1;31mNot Find Veiculo!\033[m")

    def maior_Km_veiculo(self):
        placa = list()
        Km_maior = 0

        data = self.cnx.Data_base()
        if data == None: return

        for i in data.values():
            if(i["km"] == Km_maior):
                placa.append(i["placa"])
            elif (i["km"] > Km_maior):
                Km_maior = i["km"]
                placa.clear()
                placa.append(i["placa"])

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