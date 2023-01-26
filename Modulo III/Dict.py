# ## dicionario = {}
# ## dicionario = dict()
# dicionario = dict()
# dicionario = {'Nome':'Caua'}

#exercicio 90 - 95
# #     Chave 'Nome'     ->> dicionario.keys()
# #     Value 'Caua'     ->> dicionario.values()
# #     Iten ->  Chave e Value  ->> dicionario.items()


# # apartir de dicionario, o indice agora será a CHAVE.
# for chave, value in dicionario.items():
#     print(f'O {chave} é {value}')

# #o dicionário cria chaves automaticamente
# dicionario['Idade'] = 19
# dicionario['Sexo'] = 'M'

# del dicionario['Nome']  # apagando o elemento Nome do dict
#################################################################
###################Dicionário dentro de Lista####################
brasil = list()
estado = dict()

for c in range(0,3):
    estado['Estado'] = str(input('Qual Estado? '))
    estado['Sigla'] = str(input('Sigla? '))
    brasil.append(estado.copy())
#print(brasil)
# for item in brasil:
#     print(f'{item["Estado"]} - {item["Sigla"]}')
print('-='*20)
for e in brasil:
    for value in e.values():
        print(value, end=' - ')
    print()    
    
# for e in brasil:
#     for key, value in e.items():
#         print(f'{key} - {value}')


########### Organizar ############
# from operator import itemgetter
# ranki = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# #print(ranki)
# for i, j in enumerate(ranki):
#     print(f'{i+1} Lugar {j[0]} com {j[1]}')
#     #sleep(1)



# from operator import itemgetter
# ranki = sorted(jogo.items(),  key=lambda item: item[1], reverse=True)
# #print(ranki)
# for i, j in enumerate(ranki):
#     print(f'{i+1} Lugar {j[0]} com {j[1]}')
#     #sleep(1)
