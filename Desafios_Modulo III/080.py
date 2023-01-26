#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção(sem usar o sort())
#No final, mostre a lista ordenada na tela
Lista = []
i = 0

while i < 5:
    value = int(input('Write a Value: '))
    if i == 0:
        Lista.append(value)
    else:
        a = -1
        for j in range(0, len(Lista)):
            if value < Lista[j]:
                Lista.insert(j, value)
                a = j
                break
            
        if a == -1:
            Lista.append(value)
    i+=1
    
print(Lista)