#crie um programa que vai ler vários números e colocar em uma lista.
#depois disso, crie duas listas extras que 
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas
#joga em uma lista e depois separa as lista em duas
Lista = []

while True:
    Lista.append(int(input('Write a Value: ')))

    op = ' '
    while op not in 'SN':
        op = input('Continue? (S/N) ').strip().upper()

    if op  in 'N':
        break

pares = []
impar = []

for c in Lista:
    if c%2 == 0:
        pares.append(c)
    else:
        impar.append(c)
        
print(f'Lista Completa: {Lista}')
print(f'Pares {pares}')
print(f'Ímpar {impar}')