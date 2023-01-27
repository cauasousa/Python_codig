#Faça um mini-sistema que utilize o interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. quando o usuário digitar a palavra 'FIM', o programa se encerra.
#obs:use cores
from time import sleep

def printf(num):
    for n in range(num):
        print('-', end='')
    print()

def escreva(txt):
    printf(len(txt))
    print(txt)
    printf(len(txt))
    sleep(0.7)

while True:
    escreva('SISTEMA DE AJUDA PYTHON')
    fun = input('Função ou Biblioteca > ')
    
    if 'FIM' in fun:
        escreva('ATÉ LOGO')
        break
    escreva(f'ACESSANDO MANUAL DO {fun}')
    print(help(len))