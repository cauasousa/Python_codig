# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um voletim contendo a média de cada um e permita que o usuário 
# possa mostrar as notas de cada aluno individuamente, perguntando
# [nome, [nota, nota2]], 
database = list()
dados = list()
notas = []
nome = []

while True:

    nome.append(input('Name: '))
    notas.append(int(input('Nota 1: ')))
    notas.append(int(input('Nota 2: ')))
    dados.append(nome[:])
    dados.append(notas[:])
    database.append(dados[:])
    notas.clear()
    dados.clear()
    nome.clear()

    op =' '
    while op not in 'SN':
        op = input('Continue? (S/N) ').strip().upper()
    if op in 'N':
        break
#print(database)
print(f'{"Num":<6}{"Aluno":<10}{"  Média":>8}')
for pos, i in enumerate(database):

    print(f'{pos:<4}  {i[0][0]:<10}   {(i[1][0] + i[1][1])/2:>6}')

while True:
    nome = input('Nome do Aluno Procurado: ')
    for i in database:
        if nome in i[0][0]:
            print(f'Nota 01: {i[1][0]} Nota 02: {i[1][1]}')
    op =' '
    while op not in 'SN':
        op = input('novamente? (S/N) ').strip().upper()
    if op in 'N':
        break