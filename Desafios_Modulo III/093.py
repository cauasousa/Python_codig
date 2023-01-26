# crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a qunatidade de gols feitos em cada partidas. No final,
#  tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato
data = dict()
cont = 0

data['Nome'] = input('Nome: ')
num = int(input('Quantas partidas jogou? '))

for i in range(1, num+1):
    data[i] = int(input(f"Quantos gol na partida {i}? "))
    cont += data[i]
data['Total'] = cont
print('-='*20)
print(data)
print('-='*20)
for key, value in data.items():

    if key == 'Nome':
        print(f'{key} - {value}')
        continue
    if key == 'Total':
        print(f'{key} - {value} Gols')
        continue
    print(f'Jogo {key} foram feitos {value} Gols')
