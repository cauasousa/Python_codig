# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de umjogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome ='Desconhecido', gols = 0):
    if nome.strip() == '':
        ficha(gols=0)
        return
    print(f'O jogador {nome} marcou {gols}')
    


nome = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
ficha(nome, gol)