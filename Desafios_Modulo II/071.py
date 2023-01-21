# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usário qual será o valor a ser sacado(número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues
# obs: considere que caixa possui cédulas de 50, 20 , 10 e 1

nota_20 = nota_10 = nota_1 = nota_50 = 0

print('--'*20)
valor = int(input('Valor a ser sacado: '))
print('--'*20)

while True:

    nota_50 = valor // 50
    resto = valor % 50
    nota_20 = resto // 20
    resto = resto % 20
    nota_10 = resto // 10
    resto = resto % 10
    nota_1 = resto // 1
    print(f'{nota_50} Cédulas de R$50 \n{nota_20} Cédulas de R$20 \n{nota_10} Cédulas de R$10 \n{nota_1} Cédulas de R$1')
    op = input('Deseja Sacar Outro Valor? [S/N] ').upper().strip()

    while True:
        if op in 'S':
            print('--'*20)
            valor = int(input('Valor a ser sacado: '))
            print('--'*20)
            break
        elif op in 'N':
            print('Encerrando!')
            break
        else:
            op = input('Deseja Sacar Outro Valor? [S/N] ').upper().strip() 
    if op == 'N':
        break
                    

        
        