# Faça um programa que tenha uma função notas() que pode receber várias notas
#  de alunos e v
# ai retornar um dicionário com as seguintes informações:
# - quantidade de notas - a maior nota - a menor nota - a média da turma - a situação(opcional)
# adicione também as docstrings da função.
import math
def notas(*nota, sit = False):
    """
    nota: irá conter as notas
    sit = é usado para saber a situação do aluno
    return: com retorno
    """
    quan = maior = menor = média = aux = 0
    op = -1
    # quan = len(nota)
    # maior = max(notas)
    # menor = min(nota)
    # média = sum(notas)/len(nota)
    for c in nota:
        if quan == 0:
            maior = c
            menor = c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        quan+=1
        média+=c
    média = média/quan

    dici = {'Total':quan, 'Maior':maior, 'Menor':menor, 'Média':média}

    if sit == True:
        if média >= 7:
            dici['Situação'] = 'Boa'
        if 7 > média > 5:
            dici['Situação'] = 'Razoável'
        if 5 > média >= 0:
            dici['Situação'] = 'Ruim'

    return dici


bloco = notas( 1, 12, 10)
print(bloco)
help(notas)