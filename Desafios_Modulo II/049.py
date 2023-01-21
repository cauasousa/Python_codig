#refaça o desafio 9 mostrando a tabuada de umnumero que usário escolhe
n = int(input('Qual tabuada desejada: '))
for c in range(0, 11):
    print(n, 'x', c, '=', n*c)