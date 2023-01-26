# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantos vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) quais foram os numeros pares

n1 = int(input('Digite o 1 Número: '))
n2 = int(input('Digite o 2 Número: '))
n3 = int(input('Digite o 3 Número: '))
n4 = int(input('Digite o 4 Número: '))

Tupla = n1, n2, n3, n4
print('---'*25)
print('***'*25)
print(f"O valor 9 Apareceu {Tupla.count(9)} Vezes")

posição = -1
for pos, time in enumerate(Tupla):
    if time == 3:
        posição = pos
        break
if posição == -1:
    print('A Posição do valor 3 não existe')
else:
    print(f'A Posição do valor 3 é {posição+1}')
print('Os valor Encontrados Pares: ', end='')

for c in Tupla:
    if c%2 == 0:
        print(f' {c} ', end='')

print(' ')
print('---'*25)
print('***'*25)