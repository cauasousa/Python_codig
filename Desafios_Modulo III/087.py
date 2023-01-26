# Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados
#B) A soma dos valores da terceira coluna
#C) O maior valor da segunda linha
matriz = []
ordem3 = []

for i in range(0, 3):
    for j in range(0, 3):
        ordem3.append(int(input(f'Adicionar Elemento Indice [{i}][{j}]: ')))
    matriz.append(ordem3[:])
    ordem3.clear()


soma_par = soma_coluna3 = maior_2_linha = cont = 0
for i in matriz:
    for j in range(0, 3):
        if i[j]%2==0:
            soma_par+=i[j]
        if j == 2:
            soma_coluna3+=i[j]
    
    if cont == 1: 
        maior_2_linha = max(i)
    cont+=1

for i in matriz:
    for j in range(0, 3):
        print(f'|{i[j]}|', end='')
    print('')

print(f'Soma dos Valores Pares é {soma_par}')
print(f'Soma da 3 coluna é {soma_coluna3}')
print(f'Maior da 2 linha é {maior_2_linha}')