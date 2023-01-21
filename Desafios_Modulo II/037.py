# Escreva um programa ue leia um número inteiro qualuer e peça para o usuário escolher qual será a base da conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Número: "))

opc = int(input("1 - Binário \n2 - Octal\n3 - Hexadecimal "))
if opc == 1:
    print(bin(num)[2:])
elif opc == 2:
    print(oct(num)[2:])
elif opc == 3:
    print(hex(num)[2:])
else:
    print('Número incorreto')
