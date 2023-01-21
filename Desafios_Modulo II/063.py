# Escreva um programa que leia um número n inteiro qualquer
#  e mostre na tela os n primeiros elementos de uma sequência de Fibonacci
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Quant da sequência de Fibonacci: '))
x = 0
prim = 1
seg = 0

while x < n:
    termo = prim + seg
    prim = seg
    seg = termo
    print(termo, end='b-> ')
    x += 1
print('FIM')
