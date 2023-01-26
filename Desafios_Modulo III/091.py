# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#  No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
import random
from time import sleep

jogo = dict()
ranki = list()

jogo['Jogador 1'] = random.randint(1, 6)
jogo['Jogador 2'] = random.randint(1, 6)
jogo['Jogador 3'] = random.randint(1, 6)
jogo['Jogador 4'] = random.randint(1, 6)

for key, valu in jogo.items():
    print(f'O {key} Tirou {valu}')
    sleep(1)

from operator import itemgetter
ranki = sorted(jogo.items(),  key=lambda item: item[1], reverse=True)
#print(ranki)
print('--- Ranking ---')
for i, j in enumerate(ranki):
    print(f'{i+1} Lugar {j[0]} com {j[1]}')
    sleep(1)
