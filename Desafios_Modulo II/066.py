# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados 
# e qual foi a soma entre eles(desconsiderando o flag)
# quantos valores teve
soma = i = 0

while True:
    print('--' * 20)
    num_1 = int(input('Número: '))
    if num_1 == 999:
        print('--' * 20)
        print(f'Foram digitados {i} números\nSendo a soma {soma}')
        break
    i+=1
    soma+=num_1
