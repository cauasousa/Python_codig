#Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artifícios,
#  indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)