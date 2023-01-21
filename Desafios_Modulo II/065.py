# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# o programa deve perguntar  ao usuário se ele quer ou não continuar a digitar valores

x = True
menor = maior = cont = soma = 0

while x == True:
    op = str(input('Deseja adicionar valor? S/N ')).strip().upper()
    if op == 'S':
        num = int(input('Digite o valor: '))

        soma = soma + num
        cont+=1

        if num > maior:
            maior = num
        if num < menor or menor == 0:
            menor = num
    else:
        print(f'A média dos {cont} é {soma/cont} \nMenor termo: {menor} \nMaior termo: {maior}')
        x = False