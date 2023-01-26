# Crie um programa que leia um nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário
# se por acaso a CTPS for diferente da ZERO.
# o dicionario receberá também o ano de contratação e o salário. Calcule e acrescente, elém da idade, com quantos anos e
#  pessoas vai se aposentar
# ctps - carteira de trabalho(0 nao tem) = se for zero nao pergunta nao de contr e nem salario
# 35 ano de contribuição
from datetime import datetime

data = {'Nome': input('Nome: ')}
ano = int(input('Ano de Nascimento: '))
data['Idade'] = (datetime.now().year - ano)

data['Ctps'] = int(input('Carteira de Trabalho: (0 Não adicionar ctps) '))

if data['Ctps'] != 0:
    data['Ano de Contratação'] = int(input('Ano de Contratação: '))
    data['Salario'] = float(input('Salário: '))
    data['Aposenta'] = data['Idade'] + \
        (data['Ano de Contratação'] + 35) - datetime.now().year

print('-='*20)
for key, value in data.items():
    if key in 'Ctps' and value == 0:
        print('\t - Sem Carteira de Trabalho')
        continue
    print(f'\t - {key} : {value}')
