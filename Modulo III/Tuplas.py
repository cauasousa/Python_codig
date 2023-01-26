# Tuplas são imutáveis 
# Quando o programa ta parado, pode mexer na tupla. Porém se tiver em execução não pode mexer
# aceita outros tipos de dados dentro 


# ()  -> Parentese  --- TUPLAS
# []  -> Colchete   --- LISTA
# {}  -> Chave      --- DICIONÁRIO

lache = 'Suco', 'Pizza', 'ETC'
# # lache = ('Suco', 'Pizza', 'ETC')
a = 1, 2, 3, 4
b = (2, 6, 7, 8)
c = a + b
d = b + a
# print('--'*10)

# print(lache)
# print(lache[0:1])
# print(lache[1:])
# print(lache[1:3])
# print(lache[:1])
# print(lache[-2:])

# print('--'*10)

# print(lache[0])
# print(lache[1])
# print(lache[2])

# print('--'*10)

# print(lache[-1])
# print(lache[-2])
# print(lache[-3])

# for comida in lache:
#     print(f'Eu comi {comida}')
# print('Comi Demais!')

# for posição, comida in enumerate(lache):
#     print(f'Eu comi {comida}, posição {posição}')
# print('Comi Demais!')

# print(sorted(lache))   #vai organizar a tupla quando imprimir

# print(a)
# print(b)
# print(c)
# print(d)
# print(c.count(2))  # contar quantas vezes aparece o numero 2
# print(d.index(8))  # qual posição está o 8
# print(c.index(2,1))  # como existe dois, ele vai agora procurar apartir da posição 1, haja visto q a posição zero tem o elemento 1

# print(c)
# del(c)   # deletou a tupla, serve pra outras variáveis. a tupla não aceita deletear somente uma
# print(c) # se imprimir irá dá erro
