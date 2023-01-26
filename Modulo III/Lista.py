#Lista
#insert(1, 'Novo') -> inserir em NOVO na posição 1 e o q antes tava 1, agora vai para posição 2
#append() --> adicionar no FINAL
####################3
#del lache[3]
#lanche.pop(3)  #->Normalmente usado para remover no Final, sem usar o index remover o ultimo
#lanhce.remove('Pizza')  -> se não tiver, irá dá erro. preciso de um if 

# lanche.sort()   #->organiza
# lanche.sort(reverse=True)  #-> Ordem reversa

# valores = list()
# lanche = ['Suco', 'Mortadela', 55]

# valores.append(5)
# print(valores)
# print('Adicionando....')
# valores.insert(0, 9)
# print(valores)
# print('Adicionando....')
# valores.insert(1, 10)
# print(valores)
# #################################################
# print('Deletando index 1...')
# del valores[1]
# # valores.pop(1)  #->valores.pop() #->remove o último
# # if 10 in valores:
# #     valores.remove(10)
# # else:
# #     print('Não tem o valor 10')
# print(valores)
# ###########################################

# print('Organizando....')
# valores.sort()
# print(valores)

# ##########
# print('Junção de Duas Listas.....')
# lista = valores + lanche
# print(lista)
# #lista.sort() #->ERRO
# #print(lista)

a = [5,2,6,1]
b = a
print(f'Lista A:{a}\nLista B:{b}')
print('Modificando o 6 na lista A//Obs: a lista funciona com a mesma lógica(do Ponteiro) da lista de C++')
a[2]=8
print(f'Lista A:{a}\nLista B:{b}  ->Modificou a B também')
print("\n-------Cópia------\nAgora Copiando a Lista A....")
copia = a[:]  # Copiando a lista
print('Modificando o 8 na lista A')
a[2]=7
print(f'Lista A:{a}\nLista B:{copia}  ->Não Modificou a B também')
