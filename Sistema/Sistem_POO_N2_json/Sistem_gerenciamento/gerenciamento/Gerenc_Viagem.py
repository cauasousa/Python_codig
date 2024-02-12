import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR

class Gerenciamento_Viagem(GR.Gerenciamento_N2):
    def __init__(self, way):
        super().__init__(way)

    def editar(self, cod, alteracao, opc:int):
        """opc:
            1 - Origem\n 
            2 - Destino\n
            3 - Distancia\n
            4 - Motorista\n
            5 - Veiculo\n
        """
        data = self.cnx.Data_base()
        if data == None: return

        viagem = data.get(cod)

        if None != viagem:
            if(opc == 1):
                viagem["origem"] = alteracao
            elif(opc == 2):
                viagem["destino"] = alteracao
            elif(opc == 3):
                alteracao = float(alteracao)
                viagem["distancia"] = alteracao
            elif opc == 4:
                viagem["motorista"] = alteracao
            elif opc == 5:
                viagem["veiculo"] = alteracao

            self.cnx.Update(viagem, cod)

            print("\t\t\033[1;31mATUALIZADO !!\033[m")
        else:
            print("\t\t\033[1;31mNot Find\033[m")

    def motorista_maior_Km(self):
        name = {}        
        data = self.cnx.Data_base()
        if data == None: return

        for i in data.values():
            con = i["distancia"]
            if i["motorista"] in name:
                con = name[i["motorista"]] + con

            name.update({i["motorista"]: con})

        aux = 0
        moto = list()
        for i in name.items():
            if(aux == i[1]):
                moto.append(i[0])
            elif aux < i[1]:
                aux = i[1]
                moto.clear()
                moto.append(i[0])

        if(len(moto) == 0):
            print('\t\t\033[1;31mNão tem Motorista com maior KM\033[m')
        else:
            print('\t\t\033[1;34mMotorista(s) com maior(es) Km: ', end='')
            design = 0
            for i in moto:
                print(i, end=' ')
                design+=1
                if(len(moto) > design and len(moto) > 0):
                    print(',', end=' ')
            print('com', aux, 'KM', '\033[m')
    
    def Motorista_realizou_vigens(self):
        name = {}        
        data = self.cnx.Data_base()

        if data == None: return

        for i in data.values():
            con = 1
            if i["motorista"] in name:
                con = name[i["motorista"]] + con

            name.update({i["motorista"]: con})

        aux = 0
        moto = list()
        for i in name.items():
            if(aux == i[1]):
                moto.append(i[0])
            elif aux < i[1]:
                aux = i[1]
                moto.clear()
                moto.append(i[0])

        if(len(moto) == 0):
            print('\t\t\033[1;31mNão Houve Cadastro de Viagem\033[m')
        else:
            print('\t\t\033[1;34mMotorista(s) que mais realiza(ram) viagens: ', end='')
            design = 0
            for i in moto:
                print(i, end=' ')
                design+=1
                if(len(moto) > design and len(moto) > 0):
                    print(',', end=' ')
            print('com', aux, 'viagens', '\033[m')