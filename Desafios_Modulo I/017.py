#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#calculo e mostre o comprimento da hipotenusa

import math

cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(hipotenusa)