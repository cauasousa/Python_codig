# Faça um programa que leia um npumero de  0 a 9999 e mostre na tela cada um dos dígitos separados
#  unidade dezena centena e milhar
num = 0
test = False
while test == False:
    num = int(input('Num: '))
    if(num < 9999 and num > 0):
        test = True
    else:
        print('Escreva novamente um numero entre 0 e 9999')
        
nome = str(num)
if num < 10:
    print('Uni: ', num)
if num < 100 and num >=10:
    print(f"uni: {nome[1]} \nDez: {nome[0]}")
if num < 1000 and num >=100:
    print(f"uni: {nome[2]} \nDez: {nome[1]}\nCent: {nome[0]}")
if num < 10000 and num >= 1000:
    print(f"uni: {nome[3]} \nDez: {nome[2]}\nCent: {nome[1]} \nMilh: {nome[0]}")

