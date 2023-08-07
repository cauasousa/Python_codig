#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# aproveite e crie também uma função leiafloat() com a mesma funcionalidade
def leiaint(tst):
    print(tst, end='')
    while True:
        try:
            rec = int(input())
        except KeyboardInterrupt:
            print('Usuário não digitou')
        except:
            print('Erro, Digite Novamente!')
            print(tst, end='')
        else:
            print(f'Número digitado foi {rec}')
            break
        
    
def leiafloat(tst):
    print(tst, end='')
    while True:
        try:
            rec = float(input())
        except KeyboardInterrupt:
            print(f'Número digitado foi 0')
        except:
            print('Erro, Digite Novamente!')
            print(tst, end='')
        else:
            print(f'Número digitado foi {rec}')
            break



leiaint('Digite um número inteiro: ')
leiafloat('Digite um número float: ')