# crie um programa que leia uma frase e diga se ela é um políndromo, desconsiderando os espaços
# ex-> após a sopa // a sacada da casa // a torre da derrota /// lendo de trás pra frente, ela tem o mesmo significado 
frase = str(input('Digite a frase: ')).strip()

frase = frase.upper()
lista = frase.split()
frase = ''.join(lista)

cont = 0
x = 0

for c in range(len(frase), 0, -1):
    if frase[x] == frase[c-1]:
        cont+=1
    x+=1
if cont == len(frase):
    print('-> Está frase é Políndromo')
else:
    print("-> Está frase não é Políndromo")

