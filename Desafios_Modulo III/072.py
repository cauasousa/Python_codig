#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
# de zero até vinte.
#seu programa deverá ler um número pelo teclado(entre 0 a 20) e mostrá-lo por extenso
tupla = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dizesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
n = -1
while n not in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
    n = int(input('Digite um número entre 0 e 20: '))
print(f'O {n} por extenso é {tupla[n]}')
