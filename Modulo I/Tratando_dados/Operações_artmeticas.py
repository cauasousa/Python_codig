# // divisão inteira
# ** potência
# % resto da divisão
##############################
# ordem de precedencia
# 1 - ()
# 2 - **
# 3 - * / % //
# 4 - + -

a = int(input("Prim: "))
b = int(input('Segundo: '))
print('Adicao ')
print(f'Soma de {a} + {b} é {a+b:.2f}', end = ' >>>>>>> ')
print(' - ' * b)

a = int(input("Prim: "))
b = int(input('Segundo: '))
print('Subtracao ')
print(a - b)
print(' - ' * b)

a = int(input("Prim: "))
b = int(input('Segundo: '))
print('Multi ')
print(a * b)
print(' - ' * b)

a = int(input("Prim: "))
b = int(input('Segundo: '))
print('Divisao ')
print(f'Divisao de {a} / {b} é {a/b:.2f}', end = '')
print(' - ' * b)

a = int(input("Prim: "))
b = int(input('Segundo: '))
print('potencia ')
print(a ** b)
#pow(a,b)
print(' - ' * b)

a = int(input("Prim: "))
b = int(input('Segundo: '))
print('Divisao inteira ')
print(a // b)
print(' - ' * b)

a = int(input("Prim: "))
b = int(input('Segundo: '))
print('Resto da divisao ')
print(a % b)
print(' - ' * b)
