# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o coneúdo da estrutura na tela
data = dict()
datasheet = dict()
lista = []
while True:

    data['Nome'] = str(input('Nome:'))
    data['Média'] = float(input('Média: '))
    if data['Média'] >= 7:
        data['Situação'] = 'Aprovado'
    elif (data['Média'] >= 5) and (data['Média'] < 7):
        data['Situação'] = 'Recuperação'
    else:
        data['Situação'] = 'Reprovado'
    lista.append(data.copy())

    op = ' '
    while op not in 'SN':
        op = str(input('Add? (S/N)')).upper().strip()
    if op in 'N':
        break
for e in lista:
    print(f'{"Aluno:":<4} {e["Nome"]:>4} {"  Média":>4} {e["Média"]:<6} {"Situação:":>4} {e["Situação"]:<8} ')
    #print(f'{"Aluno:" "{e["Nome"]:>4}"} {"Média":>4} {e["Média"]:>6} Situação: {e["Situação"]:<8} ')

