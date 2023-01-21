# Faça um programa que mostre a tabuada de vários números, um de cada vez.
# para cada valor digitado pelo usário.
# o programa será interrompido quando o número solicitado for negativo

while True:
    n = int(input('Qual tabuda? '))
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1
    if input('Informar mais uma valor? (S/N) ').strip().upper()[0] in 'N':
        print('Finalizando Programa!')
        break
    else:
        print('--' * 20)
