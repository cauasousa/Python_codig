# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente
#em uma lista, composta por duas interna
par = []
impar = []
value = [par, impar]

for c in range(0,7):
    num = int(input('Write a Value: '))
    if num%2 == 0:
        par.append(num)
        #value[0].append(num)
    else: 
        impar.append(num)
        #value[1].append(num)

par.sort()
impar.sort()
print(f'Valores Pares : {value[0]}')
print(f'Value Impares : {value[1]}')