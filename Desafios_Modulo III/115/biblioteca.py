from time import sleep

def leiaint(tst =''):
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
            #print(f'Número digitado foi {rec}')
            return rec
    
def printf(num=32):
    for n in range(num):
        print('-', end='')
    print()


def escreva(txt):
    print(txt)
    sleep(0.7)


def menu(*txt):
    i=1
    printf()
    escreva(txt[0])
    printf()

    for c in txt[1:]:
        escreva(str(i)+c)
        i+=1
    printf()
    op = 0
    while True:
        op = leiaint('OPÇÃO: ')
        if len(txt) > op >= 1 :
            break
        else:
            print('Escreva um Número de Acordo com o Menu\nOPÇÃO: ')
    return op


def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError: 
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro no Arquivo!')
    else:
        print('Arquivo Criado')


def op1(nome):
    usua = str(input('Nome:  '))
    idade = leiaint('Idade:  ')
    try:
        a = open(nome, 'at')
    except:
        print('Erro no arquiv!')
    else:
        try:
            a.write(f'{usua} - {idade}\n')    
        except:
            print('Erro no Cadastro')
        else:
            print('Cadastrado!')

def op2(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro na abertura do Arquivo')
    else:
        print('\n-=-=-Lista-=-=-')
        for linha in a:
            dado = linha.split('-')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()

def exe_menu(op, nome):
    if op == 1:
        op1(nome)
        print()
    elif op == 2:
        op2(nome)
    elif op == 3:
        return
    else:
        print('Erro!')

