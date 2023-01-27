# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
# escreva('Olá, Mundo!)   -> a linha acompanha a frase
# -> -----------
# -> Olá, Mundo!
# -> -----------
def printf(num):
    for n in range(num):
        print('-', end='')
    print()

    
def escreva(txt):
    printf(len(txt))
    print(txt)
    printf(len(txt))


########Princ
tex = input('Escreva o Text: ')
escreva(tex)