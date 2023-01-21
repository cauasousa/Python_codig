# melhore o desafio 61, pergutando para o usário se ele quer mostrar mais alguns termos. 
# o programa encerra quando ele disser que quer mostrar 0 termos.

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