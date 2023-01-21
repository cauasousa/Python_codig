# Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usário quer ou não continuar. No final, mostre: 
#Quantas pessoas tem mais de 18 anos
#Quantas homens foram cadastrados
#quantos mulheres em menos de 20 anos
i = j = x = 0

while True:
    print('---' * 20)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip(). upper()[0]
    
    if idade > 18:
        i+=1
    if sexo in 'M':
        j+=1
    if sexo in 'F' and idade < 20:
        x+=1 
    if input('COntinuar Adicionando? [S/N] ').strip().upper()[0] in 'N':
        print('---' * 20)
        print(f'Existem {i} pessoa com mais de 18 anos \n{j} Homem Foi Cadastrados \nExiste {x} mulher com menos de 20')
        break