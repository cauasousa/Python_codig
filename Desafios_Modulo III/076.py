# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# no final, mostre uma listagem de preços, organizando os dados em forma tabular.
tabela = 'Arroz', 7.5, 'Carne', 15.8, 'Manteiga', 5.20, 'Feijão', 8.6
i = 0
while True: 
    print(f'Produto {tabela[i]:^10}', end=' ----------------- ')
    print(f' R$ {tabela[i+1]:<10}')
    i+=2
    if  i >= len(tabela):
        break