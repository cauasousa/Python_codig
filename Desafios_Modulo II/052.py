# FAca um programa que leia um numero interio e diga se ele pe ou nao um numero primo
num = int(input('Qual numero deseja saber se é primo: '))
test = 0
for c in range(1, num+1):
    if num%c == 0:
        test+=1

if test == 2:
    print('é primo')
else:
    print('Não é primo')