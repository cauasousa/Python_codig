# Refaça o desafio 51. lendo o primeiro termo e a razão de um PA.
# mostrando os 10 primeiros termos da progressão usando a estrutura while
prim = float(input('Primeiro Termo: '))
razão = float(input('Razão: '))
n = 1
pa = 0
cond = 10

while n <= cond:
    pa = prim + (n - 1)*razão
    print(f'{n} termo: {pa}')
    n+=1
    if n > cond:
        cond = cond + int(input('Mostrar quantos elementos mais? '))
print('FIM')