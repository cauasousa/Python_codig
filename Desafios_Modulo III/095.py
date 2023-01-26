# Aprimore o desafio 093 para que ele funcione com vários jogadores,
#  incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
data = dict()
cont = 0
banco = list()
num = 0

while True:

    data.clear()
    

    data['Nome'] = input('Nome: ')
    num = int(input('Quantas partidas jogou? '))

    lsita = []
    lsita.clear()
    for i in range(1, num+1):
        lsita.append(int(input(f"Quantos gol na partida {i}? ")))
    data['GOLs'] = lsita[:]
    banco.append(data.copy())

    ############################################
    op = ' '
    while op not in 'SN':
        op = str(input('ADD?(S/N) ')).strip().upper()
    if op in 'N':
        break
    print('-='*20)


print('-='*20)
print('-='*20)

print(f'{"COD ":<5}{"NOME":<15}{" GOLS":<15}{" APROVEITAMENTO":<15}')

for x, v in enumerate(banco):
    print(f'{x:<5}|', end='')

    for da in v.values():
        print(f'{str(da):<15}{"|"}', end='')
    print(f'{sum(v["GOLs"]):<15}')

print('-='*20)

###########################################################################################
while True:
    busca = int(input('Mostrar dados de qual jogador?(Digitar COD)\n999 - Finaliza '))
    if busca == 999:
        break
    if busca >= len(banco):
        print('Incorreto!')
        continue
    else:
        print(f'=-=-=-=-=DADOS DO JOGADOR {banco[busca]["Nome"]}=-=-=-=-')
        print(f'{"COD ":<5}{"NOME":<15}{" GOLS":<15}{" APROVEITAMENTO":<15}')
        print(f'{busca:<5}', end='')
        for da in banco[busca].values():
            print(f'{str(da):<15}{"|"}', end='')
        print(f'{sum(banco[busca]["GOLs"]):<15}')
        print('-='*20)
###########################################################################################
