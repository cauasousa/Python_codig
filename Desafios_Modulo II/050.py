# DEsevolva um programa que leia seis numeros interio e mostre a soma daqueles que forem pares.
#  se o valor digitado for impar, desconsidere-o
soma = 0
for c in range(6):
    s = int(input(f'Num {c}:'))

    if s%2==0:
        soma+=s
print(soma)