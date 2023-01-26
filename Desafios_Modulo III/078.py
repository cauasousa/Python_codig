# Faça um programa que leia 5 valores númericos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

Lista = []
for c in range(0, 5):
    Lista.append(int(input('Digite Um Número: ')))

print(Lista)
print(f"Maior Foi {max(Lista)} nas Posições ", end=' ')

for pos, c in enumerate(Lista):
    if max(Lista) == c:
        print(f'{pos + 1}', end='...')

print(f"\nMenor Foi {min(Lista)} nas Posições ", end='')
for pos, c in enumerate(Lista):
    if min(Lista) == c:
        print(f'{pos + 1}', end='...')
