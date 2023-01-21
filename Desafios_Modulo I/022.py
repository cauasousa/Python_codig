#Crie um programa que leia o nome completo de uma pessoa e mosre: 
# o nome com todas as letras maiúsculas 
# o nome com todas minúsculas 
# quantas letras ao todo(sem considerar espaços)
# quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo '))
print(nome.upper())
print(nome.lower())
divisao = nome.split()
print(len(''.join(divisao)))
print(len(divisao[0]))