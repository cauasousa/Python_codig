# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar trÊs contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
# spleet  situação-> 90, 40, 10
# 20, 10 , -1 ou 1 
# 5, -5, 0-> vai consiederar passo 1 em 1
from time import sleep


def contador(i, f, p):
    fim = f
    if i > f:
        if p == 0:
            p = -1
        if p > 0:
            p = -p
        f = f - 1
    if i<f:
        if p == 0:
            p = 1
        elif p<0:
            p = -p
        f = f + 1
    print(f'Contando de {i} até {fim} -> ', end='', flush=True)

    for c in range(i, f, p):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('----Personalizar----')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('PASSO: ')))