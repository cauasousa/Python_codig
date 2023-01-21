# crie um programa que leia vários números inteiros pelo teclado. 
# o programa só vai parar quando o usário digitar o valor 999. que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
x = True
soma = 0

while x == True:
    num = int(input('Valor: '))
    if num == 999:
        x = False
    else:
        soma = soma + num
print(f'A Soma é {soma}')
