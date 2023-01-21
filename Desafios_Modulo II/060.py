# Faça um programa que leia um número qualquer e mostre o seu fatorial.



cont = int(input('Número: '))
n = cont - 1
f = cont

#from math import factorial
#print(factorial(cont))

while n > 0:
    f = f * n
    n-=1
print(f'Fatorial {cont} é {f}')