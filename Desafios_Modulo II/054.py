#Crie um programa ue leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas já são maiores
# maioridade é 21 anos
maioridade = 0
de_menor = 0

from datetime import date
atual = date.today().year

for c in range(7):
    ano = int(input("Digite o ano de nascimento: "))
    if 2023 - atual >= 21:
        maioridade+=1
    else:
        de_menor+=1
print(f'Das {maioridade+de_menor}, {maioridade} são de maiores e {de_menor} são de menor')