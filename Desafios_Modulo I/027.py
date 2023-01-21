#faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e último nome separadamente
nome = str(input('Nome: ')).strip()
prim = nome.find(' ')
ult = nome.rfind(' ')

print(f"Prime: {nome[:prim]} \nSeg: {nome[ult:]}")
