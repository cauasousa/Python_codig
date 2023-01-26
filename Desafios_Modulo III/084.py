#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em um lista. No final, 
# mostre:
#a)Quantas pessoas foram cadastradas
#B) um listagem com pessoas mais pesadas   -> 100
#C)uma listagem com as pessoas mais leves   -> 70
pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(input('Nome: ').strip())
    peso = int(input('Peso: ').strip())
    dados.append(peso)
    if maior < peso:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso

    pessoas.append(dados[:])
    dados.clear()

    op = ' '
    while op not in 'SN':
        op = input('Continue? (S/N) ').upper().strip()
    if op in 'N':
        break
print('=-'*20)
print(f'Foram Cadastradas {len(pessoas)} Pessoas')
print(f'As Pessoas mais pesadas Foram: ', end = '')

for peso in pessoas:
    if peso[1] == maior:
        print(f'{peso[0]}... ', end='')

print(f'\nAs Pessoas mais leves Foram: ', end = '')

for peso in pessoas:
    if peso[1] == menor:
        print(f'{peso[0]}... ', end='')