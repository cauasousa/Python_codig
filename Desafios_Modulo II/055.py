# faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior e menor peso lidos
maior = 0
menor = 0

for c in range(5):
    peso = float(input("Peso: "))
    if(peso > maior):
        maior = peso
    if peso < menor or menor == 0:
        menor = peso
print(f"Menor Peso: {menor:.2f}\nMaior Peso {maior:.1f}")
