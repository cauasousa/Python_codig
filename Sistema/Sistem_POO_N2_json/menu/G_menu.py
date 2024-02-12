from Sistem_gerenciamento.gerenciamento.Gerenc_Motor import Gerenciamento_Motorista as Gmot
from Sistem_gerenciamento.gerenciamento.Gerenc_Veiculo import Gerenciamento_Veiculo as Gveic
from Sistem_gerenciamento.gerenciamento.Gerenc_Viagem import Gerenciamento_Viagem as Gviag
from Sistem_gerenciamento.gerenciamento.Gerenc_Abastec import Gerenciamento_Abastecimento as Gab
from Sistem_gerenciamento.gerenciamento.Gerenc_Manut import Gerenc_Manutencao as Gman
from tratamento_erros.pasta_validacao.Input_Trat import Input_Validar
import os


class Menu:
    def __init__(self, way1, way2, way3, way4, way5):
        self.__R_motori = Gmot(way1)
        self.__R_veicul = Gveic(way2)
        self.__R_viagem = Gviag(way3)
        self.__R_manut = Gman(way4)
        self.__R_abast = Gab(way5)
        self.vd = Input_Validar()

    def __Relatorio(self):
        print('\n\t\033[1;31m   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('\t   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')

        quant_moto = self.__R_motori.quant
        quant_veic = self.__R_veicul.quant
        if(quant_moto != 0):
            print('\t\t\033[1;34mQuantidade de Motorista: ', quant_moto, '\033[m')
        else:
            print('\t\t\033[1;31mNão tem Motorista Cadastrado\033[m')
        if(quant_veic != 0):
            print('\t\t\033[1;34mQuantidade de Veiculo: ', quant_veic, '\033[m')
        else:
            print("\t\t\033[1;31mNão tem Veículo Cadastrado\033[m")

        self.__R_viagem.Motorista_realizou_vigens()
        self.__R_viagem.motorista_maior_Km()
        self.__R_veicul.maior_Km_veiculo()
        self.__R_abast.total_abast()
        self.__R_manut.total_manut()
        print('\t\033[1;31m   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('\t\033[1;31m   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    
    def __Registrar_Abastecimento(self):
        valor = self.vd.input_Valor()
        if valor == None: return

        data = self.vd.input_Data()
        if data == None : return

        quant = self.vd.input_quant()
        if quant == None: return

        placa = input("\t\t\033[1;34m Placa do Veiculo:\033[m ")    
        veiculo = self.__R_veicul.find(placa)

        if None == veiculo :
            print("\t\t\033[1;31m Não Cadastrado!\033[m")
            return
        
        abastecimento = {
            "valor":valor, 
            "data":data, 
            "quant":quant,
            "veiculo" : placa
        }
        self.__R_abast.add(abastecimento)

    def __Registrar_manutencao(self):
        custo = self.vd.input_Custo()
        if custo == None: return

        tipo = input('\t\t\033[1;34m Type: \033[m')

        date = self.vd.input_Data()
        if(date == None): return

        placa = input("\t\t\033[1;34m Placa do Veiculo:\033[m ")   
        veiculo = self.__R_veicul.find(placa)

        if None == veiculo :
            print("\t\t\033[1;31m Não Cadastrado!\033[m")
            return
        
        manutencao = {
            "custo": custo, 
            "tipo":tipo, 
            "data":date, 
            "veiculo":placa
        }

        self.__R_manut.add(manutencao)

    def __Gerenciamento_Viagem(self):
        print('\t\t\033[1;34;40ma. Cadastrar Viagem\033[m')
        print('\t\t\033[1;34;40mb. Editar Viagem\033[m')
        
        opc = input("\t\t\033[1;34m>>>>>>\033[m ")

        if('a' in opc and self.__R_motori.quant_min() and self.__R_veicul.quant_min()):
            destino = input("\t\t\033[1;34m Destino: \033[m")
            origem = input("\t\t\033[1;34m Origem: ")
            distancia = self.vd.input_distancia()
            if distancia == None: return

            cpf = input('\t\t\033[1;34m CPF do Motorista:\033[m ') 
            cpf = cpf.replace(' ', '')
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')
            motorista = self.__R_motori.find(cpf)

            if None == motorista :
                print('\t\tCPF Inválido!')
                return

            placa = input("\t\t\033[1;34m Placa do Veiculo:\033[m ")    
            veiculo = self.__R_veicul.find(placa)

            if None == veiculo :
                return
            else:
                veiculo["km"]+=distancia
                self.__R_veicul.cnx.Update(veiculo, placa)
                
            viagem = {
                "origem":origem, 
                "destino":destino, 
                "distancia":distancia, 
                "motorista":cpf, 
                "veiculo":placa
            }
            self.__R_viagem.add(viagem)
        
        elif('b' in opc and self.__R_viagem.quant_min()):

            cod = input("\t\t\033[1;34mCódigo da Viagem: ")
            ref = self.__R_viagem._Gerenciamento_N2__find(cod)
            
            if None != ref:
                print("\t\t\033[1;34mWrite for Edit:\n\t\t 1 - Origem\n\t\t 2 - Destino\n\t\t 3 - Distancia\n\t\t 4 - Motorista\n\t\t 5 - Veiculo")
                try:
                    opc = int(input('\t\t>>>>> \033[m'))
                except ValueError:
                    print('\t\t\033[1;31mIncorreto!\033[m')
                    return
                else:
                    if((6 > opc) and (opc > 0)):
                        
                        if opc == 3: #alterar distancia

                            alteracao = self.vd.input_distancia()

                            ### atualizar os dados do veiculo
                            aux = alteracao - ref["distancia"]
                            veiculo = self.__R_veicul.find(ref["veiculo"])


                            if(veiculo != None):
                                veiculo["km"] += aux
                                self.__R_veicul.cnx.Update(veiculo, veiculo['placa'])

                        elif opc == 4: # alterar motorista

                            cpf = input('\t\t\033[1;34m CPF do Motorista:\033[m ')
                            cpf = cpf.replace(' ', '')
                            cpf = cpf.replace('-', '')
                            cpf = cpf.replace('.', '')
                            motorista = self.__R_motori.find(cpf)
                            if motorista == None: return

                            alteracao = cpf

                        elif opc == 5: #Alterar o veiculo

                            placa = input('\t\t\033[1;34m Placa do Veiculo: \033[m')

                            veiculo_new = self.__R_veicul.find(placa)
                            if veiculo_new == None: 
                                print('\t\t\033[1;31m Não Encontrado\033[m')
                                return

                            ##atualizar veiculo novo e velho
                            veic_old = self.__R_veicul.find(ref["veiculo"])
                            if veic_old != None:
                                veic_old["km"] -= ref["distancia"]
                                self.__R_veicul.cnx.Update(veic_old, veic_old["placa"])

                                
                            veiculo_new["km"] += ref["distancia"]
                            self.__R_veicul.cnx.Update(veiculo_new, placa)
                            alteracao = placa

                        else:
                            alteracao = input("\t\t\033[1;34mWrite new change: \033[m")
                        
                        self.__R_viagem.editar(cod, alteracao, opc)
                    else:
                        print('\t\tTry Again')
            else:
                print("\t\t\033[1;31mNão Encontrado!\033[m")
        
        else:
            print("\t\t\033[1;34mTry Again\033[m")

    def __Gerenciamento_Veiculo(self):
        print('\n\t\t\033[1;34;40ma. Cadastrar Veículo\033[m')
        print('\t\t\033[1;34;40mb. Pesquisar Veículo\033[m')
        print('\t\t\033[1;34;40mc. Editar Veículo\033[m')
        print('\t\t\033[1;34;40md. Deletar Veículo\033[m')
        print('\t\t\033[1;34;40me. Ver quilometragem de Veículo\033[m')

        
        opc = input("\t\t>>>>>> ")
        
        if('a' in opc):
            marca = input("\t\t\033[1;34m Marca: ")
            modelo = input("\t\t Modelo: ")

            ano = self.vd.input_ano()
            if ano == None: return 

            placa = input("\t\t\033[1;34m Placa: ")

            chassi = input("\t\t chassis: ")
            cor = input("\t\t COR: \033[m")

            km = self.vd.input_km()
            if km == None: return 

            veiculo = {
                "marca":marca, 
                "modelo":modelo, 
                "ano":ano, 
                "placa":placa, 
                "chassi":chassi, 
                "cor":cor, 
                "km":km
            }
            self.__R_veicul.add(veiculo, placa)

        elif('b' in opc and self.__R_veicul.quant_min()):
            placa = input("\t\t\033[1;34m Placa do veiculo:\033[m ")
            ref = self.__R_veicul.find(placa)

            if None != ref:
                print('\n\t\033[1;31m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
                print("\t\t\t\033[1;34mMarca: ", ref["marca"], '\033[m')
                print("\t\t\t\033[1;34mModelo: ", ref["modelo"], '\033[m')
                print("\t\t\t\033[1;34mAno: ", ref["ano"], '\033[m')
                print("\t\t\t\033[1;34mPlaca: ", ref["placa"], '\033[m')
                print("\t\t\t\033[1;34mChassi: ", ref["chassi"], '\033[m')
                print("\t\t\t\033[1;34mCor: ", ref["cor"], '\033[m')
                print("\t\t\t\033[1;34mKm: ", ref["km"], '\033[m')
                print('\t\033[1;31m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m\n')
            else:
                print('\t\t\033[1;31mNão Encontrado\033[m')

        elif('c' in opc and self.__R_veicul.quant_min()):
            placa = input("\t\t\033[1;34m Placa do veiculo:\033[m ")
            ref = self.__R_veicul.find(placa)

            if None != ref:

                print("\t\t\033[1;34mDeseja Editar Qual ?\033[m")
                print("\t\t\033[1;34mWrite for Edit:\n\t\t 1 - Marca\n\t\t 2 - Modelo\n\t\t 3 - Ano\n\t\t 4 - Chassi\n\t\t 5 - Cor\033[m\n\t\t")
                try:
                    opc = int(input('\t\t\033[1;34m>>>>>\033[m '))
                except ValueError:
                    print('\033[1;34mIncorreto!\033[m')
                    return
                else:
                    if((6 > opc) and (opc > 0)):
                        if opc == 3: 
                            alteracao = self.vd.input_ano()
                            if alteracao == None:
                                return
                        else:
                            alteracao = input("\t\t\033[1;34mWrite new change:\033[m ")

                        self.__R_veicul.editar(opc, placa, alteracao)
                    else:
                        print('\t\t\033[1;34mOpcion Incorret\033[m')
            else:
                print("\t\t\033[1;31m Não Cadastrado!\033[m")        
        elif('d' in opc and self.__R_veicul.quant_min()):
            placa = input("\t\t\033[1;34m Placa do veiculo:\033[m ")
            self.__R_veicul.deletar(placa)

        elif('e' in opc and self.__R_veicul.quant_min()):
            placa = input("\t\t\033[1;34m Placa do veiculo:\033[m ")
            self.__R_veicul.see_km_veic(placa)
        
        else:
            print("\t\t\033[1;34mWrite again\033[m")

    def __Gerenciamento_Motorista(self):
        
        print('\n\t\t\033[1;34;40ma. Cadastrar Novo Motorista\033[m')
        print('\t\t\033[1;34;40mb. Pesquisar Motorista\033[m')
        print('\t\t\033[1;34;40mc. Editar Motorista\033[m')
        print('\t\t\033[1;34;40md. Deletar Motorista\033[m')
        
        opc = input("\t\t\033[1;34m>>>>>>\033[m")
        
        if('a' in opc):
            name = input("\t\t\033[1;34mNome:\033[m ")
            cpf = self.vd.input_cpf()
            
            if cpf == None: return

            rg = self.vd.input_rg()
            if rg == None: return

            cnh = self.vd.input_cnh()
            if cnh == None: return 

            motorista = {
                "nome":name, 
                "cpf":cpf, 
                "rg":rg, 
                "cnh":cnh
            }
            self.__R_motori.add(motorista, cpf)

        elif('b' in opc and self.__R_motori.quant_min()):
            cpf = input('\t\t\033[1;34m CPF do Motorista:\033[m ')
            cpf = cpf.replace(' ', '')
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')

            ref = self.__R_motori.find(cpf)
            if None != ref:
                print('\n\t\033[1;31m      =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
                print("\t\t\t\033[1;34mNome: ", ref["nome"])
                print("\t\t\t\033[1;34mCPF: ", ref["cpf"])
                print("\t\t\t\033[1;34mRG: ", ref["rg"])
                print("\t\t\t\033[1;34mCNH: ", ref["cnh"], '\033[m')
                print('\t\033[1;31m        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\033[m')

        elif('c' in opc and self.__R_motori.quant_min()):
            cpf = input('\t\t\033[1;34m CPF do Motorista:\033[m ')
            cpf = cpf.replace(' ', '')
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')
            ref = self.__R_motori.find(cpf)
            if None != ref:
                print("\t\t\033[1;34mWrite for Edit:\n\t\t 1 - Name\n\t\t 2 - RG\n\t\t 3 - CNH\033[m")
                
                try:
                    opc = int(input('\t\t\033[1;34m>>>>>\033[m '))
                except ValueError:
                    print('\t\t\033[1;31mIncorreto!\033[m')
                    return
                else:
                    if((4 > opc) and (opc > 0)):
                        if opc == 1:
                            alteracao = input("\t\t\033[1;34mWrite new Name:\033[m ")
                        elif opc == 2: 
                            alteracao = self.vd.input_rg()
                        elif opc == 3:
                            alteracao = self.vd.input_cnh()
                        
                        if alteracao == None: return

                        self.__R_motori.editar(opc, cpf, alteracao)
                    else:
                        print("\t\t\033[1;31mOpção Inválida\033[m")
            else:
                print("\t\t\033[1;31mCPF Inválido\033[m")
                
        elif('d' in opc and self.__R_motori.quant_min()):
            cpf = input('\t\t\033[1;34m CPF do Motorista:\033[m ')
            cpf = cpf.replace(' ', '')
            cpf = cpf.replace('-', '')
            cpf = cpf.replace('.', '')
            self.__R_motori.deletar(cpf)

        else:
            print("\t\t\033[1;31mTry Again\033[m")

    def Principal(self):

        print('\n\t\t\033[1;31m         MENU\033[m')
        print('\t\t\033[1;34;40m1. Gerenciamento de Motoristas\033[m')
        print('\t\t\033[1;34;40m2. Gerenciamento de Veículos\033[m')
        print('\t\t\033[1;34;40m3. Gerenciamento de  Viagem\033[m')
        print('\t\t\033[1;34;40m4. Registrar Abastecimento\033[m')
        print('\t\t\033[1;34;40m5. Registrar Manutenção\033[m')
        print('\t\t\033[1;34;40m6. Relatório\033[m')
        
        try:
            opc = int(input('\t\t\033[1;34m>>>>>\033[m'))

        except ValueError:
            print("\t\t\033[1;34mWrite again\033[m")
            return True
        
        else:

            if opc == 0:
                return False
            elif(opc == 1):
                #os.system('cls')
                self.__Gerenciamento_Motorista()
            elif(opc == 2):
                #os.system('cls')
                self.__Gerenciamento_Veiculo()
            elif(opc == 3 and self.__R_motori.quant_min() and self.__R_veicul.quant_min()):
                #os.system('cls')
                self.__Gerenciamento_Viagem()
            elif(opc == 4 and self.__R_veicul.quant_min()):
                #os.system('cls')
                self.__Registrar_Abastecimento()   
            elif(opc == 5 and self.__R_veicul.quant_min()):
                #os.system('cls')
                self.__Registrar_manutencao()
            elif(opc == 6):
                #os.system('cls')
                self.__Relatorio()  
            else:
                #os.system('cls')
                print("\t\t\033[1;31mWrite again\033[m")
            
            return True
