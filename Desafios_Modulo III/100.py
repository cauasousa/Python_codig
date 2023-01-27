# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(),
# a primeria função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
from random import randint
from time import sleep


def sorteia(lista):
    pos = 0
    print('Foram Sorteados ', end ='', flush=True)
    while pos < 5:
        num = randint(1, 10)
        print(num, end=' ', flush=True)
        lista.append(num)
        pos += 1
        sleep(0.5)
    print()
    return lista


def somaPar(tup):
    soma = 0
    for i in tup:
        if i%2 == 0:
            soma+=i
    print(f'A Soma dos Pares é : {soma}')


##############################
números = []
números = sorteia(números)
somaPar(números)