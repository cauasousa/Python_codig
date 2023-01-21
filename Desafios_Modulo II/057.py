#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

while 'F' != input('Qual seu Sexo? M/F ').upper().strip()[0] != 'M':
    print(" Digite Novamente ")

# while input('Qual seu Sexo? M/F ').upper().strip()[0] not in 'MF':
#     print(" Condição ")

