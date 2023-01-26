# crie um programa que vai ler vários números e colocar em uma lista.
# depois disso, mostre:
# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma descrescente.
# C) Se o valor 5 foi digitado se está ou não na lista

Lista = []
while True:
    Lista.append(int(input('Write a Value: ')))

    op = ''
    while ('S' not in op) and ('N' not in op):
        op = input('Add a value? (S/N) ').strip().upper()

    if 'N' in op:
        break
print(f'\n-------------\n{len(Lista)} Write Were Value')
Lista.sort(reverse=True)
print(f'Descending Order: {Lista}')

if Lista.count(5) > 0:
    print(f'Value 5 Was Found {Lista.count(5)} Times ')
else:
    print('Not Find 5')
