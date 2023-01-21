# DEsenvolva uma programa que leia o primeiro termo e a razao de PA. No final, 
# mostre os 10 primeiros termos dessa progressão
prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(10):
    print(prim)
    prim+=razao
    