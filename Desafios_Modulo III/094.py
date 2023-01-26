# crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionarios em uma lista. No final, mostre: 
# A) quantas pessoas foram cadastradas
# B) a média de idade do grupo
# C) uma lista com todas as mulheres
# d) uma lista com todas as pessoas com idade acima da média
data = dict()
datasheet = list()
soma = 0

while True:
    data['Nome'] = str(input('Nome: ')).strip()
    gen = ' '
    while gen not in  'FM':
        gen = str(input('Sexo: ')).strip().upper()
    data['Sexo'] = gen
    data['Idade'] = int(input('Idade: '))
    datasheet.append(data.copy())
    soma = soma + data['Idade']

    op = ' '
    while op not in 'SN':
        op = str(input('ADD?(S/N) ')).strip().upper()
    if op in 'N':
        break
print('-='*20)
print('-='*20)


print(f'Foram Cadastradas {len(datasheet)} Pessoas')
print('-='*20)

print(f'Média das Idades: {soma/len(datasheet)}')
print('-='*20)

print('Mulheres -> ', end='')
for i in datasheet:
    if i['Sexo'] == 'F':
        print(f'{i["Nome"]}', end =' ')
print()
print('-='*20)

print('Lista de Pessoas Acima da Média de Idade: ')
for i in datasheet:
    if i['Idade'] >= (soma/len(datasheet)):
        print(f'{i["Nome"]}', end =' ')
print()
print('-='*20)
print('-='*20)

