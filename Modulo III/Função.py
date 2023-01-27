
# #exercicio 

# def mostreLinha(msg, num):
#     print('-='*num)
#     print(msg)
#     print('-='*num)


# mostreLinha(num=20, msg = 'Cauã')
# mostreLinha('Caua', 30)

# def contador(*núm):
#     #cria um tupla, um pacote com vários numeros eu posso pegar
#     print(núm)


# contador(1, 2, 3)
# contador(8, 5, 10, 11, 2)


# def listam(lts):
#     pos = 0
#     while pos < len(lts):
#         print(lts[pos], end =' ')
#         pos+=1
#     print()
#     print('Dobro')
#     pos = 0
#     while pos < len(lts):
#         lts[pos]*=2
#         pos+=1
#     print(lts)


# lista = [1, 2, 3, 4, 5]
# listam(lista)
# print(lista)


# def soma(*valores):
#     s = 0
#     #valores vira um tupla
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} temos {s}')


# soma(1, 2, 3, 4)
# soma(1)
