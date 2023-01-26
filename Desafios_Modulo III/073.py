# crie um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato brasileiro de Futebol,
#  na ordem de colocação. Depois mostre: 
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados dda tabela 
# C) Uma lista com os times em ordem alfabética
# D) em que posição na tabela está o time da Chapecoense
tupla = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Cotitiba', 'Cuiabá', 'Ceará', 'Atletico-Go', 'Avaí', 'Juventude'
print('---'*25)
print('***'*25)

print(f'Os cincos primeiro colocados: {tupla[0:5]}')
print('***'*25)

print(f'Os últimos 4 colocados da tabela: {tupla[-4:]}')
print('***'*25)

print(f'Lista Organizada: {sorted(tupla)}')
print('***'*25)

posição = 0
for pos, time in enumerate(tupla):
    if time == 'Chapecoense':
        posição = pos
        break
print(f'Chapecoense se Encontra na Posição {posição}')
print('***'*25)
print('---'*25)