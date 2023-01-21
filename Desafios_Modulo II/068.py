# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador Perder.
#Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
i = 0 

while True:

    comp = randint(0, 10)
    escolha = input('Escolha Par ou Ímpar. [P/I] '). upper().strip()[0]
    num = int(input('Número: '))

    if (comp + num) % 2 == 0:

        if escolha ==  'P':
            print('Ganhou')
            i+=1
        else: 
            print('Perdeu, o computador escolheu ', comp, '\nGanhou ', i)
            break

    else:
        if escolha == 'I':
            print('Ganhou')
            i+=1
        else: 
            print('Perdeu, o computador escolheu ', comp, '\nGanhou ', i)
            break