# Faça um programa que tenha um função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior
from time import sleep

def maior(*valores):
    print('-='*25)

    print('Analisando.', end='', flush=True)
    sleep(1)
    print('.', end='', flush=True)
    sleep(1)
    print('.')
    
    maior = 0
    print('Valores Informados: ', end='')
    for i in valores:
        print(i, end=' ')
        if i>maior:
            maior = i
    print()
    print(f'O Maior Valor Informado foi {maior}')
    print('-='*25)


maior(1, 2, 3, 4)
maior(7, 8, 10, 22, 55, 1)
maior()