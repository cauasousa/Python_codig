# crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO"
nome = str(input('Nome: ')).strip()
print(nome.upper().count('SANTO', 0, 5))