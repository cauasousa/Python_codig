# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
# depois disso, mostre a listagem de números gerados e também indique o menor 
# e o maior valor que estão na tupla
from random import randint
tupla = randint(0,20), randint(0,20), randint(0,20), randint(0,20), randint(0,20)
print(tupla)

maior = menor = 0

for c in tupla:
    if c > maior: 
        maior = c
    if c < menor or menor == 0:
        menor = c
print('---'*25)
print('***'*25)

print(f'Maior Número Gerado foi {maior}')
#print(f'Maior Número Gerado foi {max(tupla)}')

print(f'Menor Número Gerado foi {menor}')
#print(f'Menor Número Gerado foi {min(tupla)}')

print('---'*25)
print('***'*25)