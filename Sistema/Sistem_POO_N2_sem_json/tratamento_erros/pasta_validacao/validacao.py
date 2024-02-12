from tratamento_erros.class_erros.classes_erros import Quant_de_Num_Insuf
from tratamento_erros.class_erros.classes_erros import Digito_1_invalido
from tratamento_erros.class_erros.classes_erros import Digito_2_invalido
from tratamento_erros.class_erros.classes_erros import Num_Negativo
import os

class Validacao:
    
    def cpf(self, cpf):
            try:
                
                if(cpf.count(' ') > 0 or cpf.count('-') > 0 or cpf.count('.')>0):
                    cpf = cpf.replace(' ', '')
                    cpf = cpf.replace('-', '')
                    cpf = cpf.replace('.', '')

                int(cpf)

                if(len(cpf) != 11):
                    raise Quant_de_Num_Insuf
                
            except ValueError:
                raise ValueError
            
            except Quant_de_Num_Insuf:
                raise Quant_de_Num_Insuf
            else:

                aux = 0
                verifcador_1 = 0
                verificador_2 = 0
            
                for i in range(10, 1, -1):
                    verifcador_1 = verifcador_1 + int(cpf[aux]) * i
                    aux += 1

                aux = 0
                for i in range(11, 1, -1):
                    verificador_2 = verificador_2 + int(cpf[aux]) * i
                    aux += 1

                resto_1 = verifcador_1%11
                resto_2 = verificador_2%11

                if(resto_1 == 0 or resto_1 == 1 ):
                    
                    if(int(cpf[9]) != 0 ):
                        raise Digito_1_invalido
                else:
                    if(11-resto_1 != int(cpf[9])):
                        raise Digito_1_invalido
                
                if(resto_2 == 0 or resto_2 == 1 ):
                    
                    if(int(cpf[10]) != 0 ):
                        raise Digito_2_invalido
                else:
                    if(11-resto_2 != int(cpf[10])):
                        raise Digito_2_invalido

    def is_numero_int(self, frase):

        while True:
            try:
                print('\t\t',frase[0], end=' ')
                num = input().strip()
                if '099' == num:
                    return None
                num = num.replace(' ', '')
                num = num.replace('-', '')
                num = num.replace('.', '')
                num = num.replace('/', '')
                int(num)
            except ValueError:
                os.system('cls')
                print('\t\t', frase[1])
                print('\t\t\033[1;34mTry Again!\033[m')
                continue
            else:
                return num

    def is_numero_quant(self, frase):

        while True:
            try:
                print('\t\t',frase[0], end=' ')
                num = input().strip()
                if '099' == num:
                    return None
                num = num.replace(' ', '')
                
                int(num)
            except ValueError:
                os.system('cls')
                print('\t\t', frase[1])
                print('\t\t\033[1;34mTry Again!\033[m')
                continue
            else:
                return num
    def is_numero_float(self, frase):

        while True:
            try:
                print('\t\t', frase[0], end=' ')
                num = input().strip()
                if '099' == num:
                    return None
                num = num.replace(' ', '')
                float(num)
                if(float(num) < 0):
                    raise Num_Negativo
                
            except ValueError:
                os.system('cls')
                print('\t\t', frase[1])
                print('\t\tTry Again!')
                continue
            except Num_Negativo:
                os.system('cls')
                print('\t\t\033[1;31mValor Informado Negativo! Informe um Valor Maior ou Igual a Zero, Por Favor!')
                print('\t\tTry Again!\033[m')
                continue
            else:
                return float(num)
            