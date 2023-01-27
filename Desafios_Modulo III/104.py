# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaint(tst):
    print(tst, end='')
    while True:
        rec = input()
        if False == rec.isnumeric():
            print('Erro, Digite Novamente!')
            print(tst, end='')
        else:
            break
    return rec
    

num = leiaint('Leia um Número: ')
print(f'Número digitado {num}')