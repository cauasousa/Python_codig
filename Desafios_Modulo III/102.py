#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
import math
def fatorial(a=0, b=False):
    """
    a = é o número que deseja saber o fatorial
    b para inidicar se precisa do calculo ou nao"""
    res = math.factorial(a)
    if b == False:
        print(res)
        return res
    else:
        
        for j in range(1, a+1):
            print(f'{j}', end =' ')
            if j+1 < a:
                print('x ', end='')
        print(f' = {res}')    


fatorial(5, True)
fatorial(5)