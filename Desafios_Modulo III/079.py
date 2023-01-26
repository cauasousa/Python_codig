# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente
Lista = []
Lista.append(int(input('Digite Um Número: ')))

while True:

    op = ''
    while True:
        op = input('Add a New Value? (S/N) ').strip().upper()
        if op in 'SN':
            break

    if 'S' in op:
        add = int(input('Write a value: '))
        if Lista.count(add) == False:

            Lista.append(add)

        else:

            print('!!Exists Value!!')

    else:
        break
Lista.sort()
print(Lista)
