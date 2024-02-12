
import os
from tratamento_erros.pasta_validacao.validacao import Validacao
from tratamento_erros.class_erros.classes_erros import Quant_de_Num_Insuf
from tratamento_erros.class_erros.classes_erros import Digito_1_invalido
from tratamento_erros.class_erros.classes_erros import Digito_2_invalido

class Input_Validar:
    vl = Validacao()
    
    def input_cpf(self):
        
        while True:
            try:
                cpf = input('\t\t\033[1;34mCPF ( 099 - SAIR ):\033[m ').strip()
                vdd = cpf
                if '099' == cpf:
                    return None
                self.vl.cpf(cpf)
            except ValueError:
                os.system('cls')
                print('\t\t\033[1;31mCPF Inválido, informe com Números!')
                print('\t\tTry Again!\033[m')
                continue
            except Quant_de_Num_Insuf :
                os.system('cls')
                print('\t\t\033[1;31mInforme um CPF com 11 Números, por favor!')
                print('\t\tTry Again!\033[m')
                continue
            except Digito_1_invalido:
                os.system('cls')
                print('\t\t\033[1;31mCPF Inválido, Dígito 1 Incorreto')
                print('\t\tTry Again!\033[m')
                continue
            except Digito_2_invalido:
                os.system('cls')
                print('\t\t\033[1;31mCPF Inválido, Dígito 2 Incorreto')
                print('\t\tTry Again!\033[m')
                continue
            else:
                
                cpf = cpf.replace(' ', '')
                cpf = cpf.replace('-', '')
                cpf = cpf.replace('.', '')
                
                return cpf 

    def input_rg(self):
        return self.vl.is_numero_int(['\033[1;34mRG ( 099 - SAIR ): \033[m', '\033[1;34mRG Inválido, contém letra!\033[m'])
    
    def input_cnh(self):
        return self.vl.is_numero_int(['\033[1;34mCNH ( 099 - SAIR ): \033[m', '\033[1;31mCNH Inválido, contém letra!\033[m'])
    
    def input_ano(self):
        return self.vl.is_numero_int(['\033[1;34mANO ( 099 - SAIR ): \033[m', '\033[1;34mANO Inválido, contém letra!\033[m'])

    def input_km(self):
        return self.vl.is_numero_float(['\033[1;34mKM ( 099 - SAIR ): \033[m', '\033[1;34mKM Inválido. contém letra ou sinal incorreto!\033[m'])
    
    def input_distancia(self):
        return self.vl.is_numero_float(['\033[1;34mDistância ( 099 - SAIR ): \033[m', '\033[1;34mDistância Inválido. contém letra ou sinal incorreto!\033[m'])
    
    def input_Valor(self):
        return self.vl.is_numero_float(['\033[1;34mValor ( 099 - SAIR ):\033[m ', '\033[1;34mValor Inválido. contém letra ou sinal incorreto!\033[m'])

    def input_Custo(self):
        return self.vl.is_numero_float(['\033[1;34mCusto ( 099 - SAIR ):\033[m ', '\033[1;34mCusto Inválido. contém letra ou sinal incorreto!\033[m'])

    def input_Data(self):
        return self.vl.is_numero_int(['\033[1;34mData ( 099 - SAIR ):\033[m ', '\033[1;34mData Inválido. contém letra ou sinal incorreto!\033[m'])
        
    def input_quant(self):
        return int(self.vl.is_numero_quant(['\033[1;34mQuant ( 099 - SAIR ):\033[m ', '\033[1;34mQuant Inválido. contém letra ou sinal incorreto!\033[m']))
