#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
from datetime import date

def voto(ano = 0):
    atual = date.today().year
    res = atual - ano
    if res < 16:
        return f'Com {res} Anos, o Voto é Negado'
    elif 65 > res >= 18:
        return f'Com {res} Anos, o Voto é Obrigatório'
    else:
        return f'Com {res} Anos, o Voto é Opcional'
    
ano = int(input('Ano que você nasceu: '))
print(voto(ano))