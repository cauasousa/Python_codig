#Crie um programa que faça o computador jogar Jokenpô com você
while True:
    from random import randint
    print('1 - Pedra \n2 - Papel \n3 - Tesoura ')
    num = int(input(''))
    comp = randint(1, 3)
    if comp == num:
        print(f'Empate\n{comp}')
    elif comp == 1 and num == 3:
        print(f'Perdeu\n{comp}')
    elif comp == 2 and num == 1:
        print(f'Perdeu \n{comp}')
    elif comp == 3 and num == 2:
        print(f'Perdeu \n{comp}')
    else:
        print(f'Ganhou \n{comp}')
    