# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados 
# e vai sortear 6 numeros entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
import time
num = int(input('Número de Palpites: '))
gerados = list()
aleat = []
for n in range(0, num):
    for c in range(0, 6):
        aleat.append(randint(1, 60))
    aleat.sort()
    gerados.append(aleat[:])
    aleat.clear()
x = 0
for i in gerados:
    
    print(f'\nPalpite {x + 1}: ', end='')
    for j in i:
        print(f'{j} ', end='')
    time.sleep(1)
    x+=1