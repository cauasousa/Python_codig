#crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#no final, mostre a matriz na tela, com o formatação correta
matriz = []
ordem3 = []

for i in range(0, 3):
    for j in range(0, 3):
        ordem3.append(int(input(f'Adicionar Elemento Indice [{i}][{j}]: ')))
    matriz.append(ordem3[:])
    ordem3.clear()

for i in matriz:
    for j in range(0, 3):
        print(f'|{i[j]}|', end='')
    print('')