# DEsenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# mostre:
#  média de idade do grupo
#  Qual é o nome do homem mais velho
#  quantas mulheres têm menos de 20 anos
import datetime
average_age_team = 0
she_20 = 0
maior = 0

for c in range(4):
    nome = input("Say your name: ").strip()
    idade = int(input('Say Age: '))
    sexo = input('Sexo: ').strip()

    if sexo.upper() == 'FEMENINO' and idade < 20:
        she_20+=1
    if ((sexo.lower() in 'masculino') and (idade > maior)):
        name_old = nome
        maior = idade
    average_age_team+=idade
print(f'Average of Teams {average_age_team/4} \nHomem mais velho {name_old}\nExistem {she_20} mulhures com idade menor que 20')