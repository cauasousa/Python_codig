# Crie um programa que leia o nome e preço de vários produtos. 
# O programa deverá perguntar se o usário vai continuar. 
# No final, mostre: 
# Qual é o total gasto na compra
# Quantos produtos custam mais de 1000
# Qual é o nome do produto mais barato
barato = total = 0.0
i = 0
nome_barato = ''

while True: 
    print('---'*20)
    nome = input('Nome do Produto: ').strip()
    preço = float(input('Preço: '))
    total+=preço

    if preço > 1000:
        i+=1

    if preço < barato or barato == 0:
        barato = preço
        nome_barato = nome

    op = input('Adicionar Mais um Produto? [S/N] '). strip().upper()[0]
    if  op in 'N':
        print('---'*20)
        print(f'Total gasto: $${total} \n{i} Custaram mais de $$1000 \nO {nome_barato} foi o mais barato, custando {barato}')
        break
    elif op in 'S':
        print('Adicionando.....')
    else:
        print('Resposta Incorreta!\nEncerrando.....')
        break
