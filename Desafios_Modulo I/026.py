# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes a letra "A"
# Em que posilçao ela aparece a primeira vez
# em que posição ela aparece a última vez
nome = str(input('Nome: '))
print(f"Letra 'A' aparece {nome.count('A')}")
print(f"Posição: {nome.find('A')}")
print(f"Última posição: {nome.rfind('A')}")