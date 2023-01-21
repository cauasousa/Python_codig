#  Crie um programa que leia dois valores e mostre um nenu na tela:
# [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa
#seu programa deverá realizar a operação solicitada em cada caso
op = int(0)
operação = 0.0

while op != 5 :
    op = 0
    num = float(input('Primeiro Número: '))
    num_2 = float(input('Seg. Número: '))
    
    while (op != 4) and (op != 5):
        print('''
        Menu
        [1] somar
        [2] multiplicar 
        [3] maior
        [4] novos números 
        [5] sair do programa''')
        op = int(input('Qual opção: '))
        if (1 <= op <= 3):
            if op == 1:
                operação = num + num_2
            if op == 2:
                operação = num * num_2
            if op == 3:
                if num > num_2:
                    operação = num
                else:
                    operação = num_2
            print(f'Resultado dessa Operação {operação}')
        else:
            print('Finalizando essa operação')
print('Finalizando o Programa!')
        
        
