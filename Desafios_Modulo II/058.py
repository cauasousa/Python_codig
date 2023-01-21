# Melhore o jogo do Desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer 
#
import random 
i = 1
while random.randint(0, 10) != int(input('Adivinhe: ')):
    print("Tente novamente ")
    i+=1
print('Acertou')
print(f'Foram necessários {i} tentativas')
