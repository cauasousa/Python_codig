from time import sleep
def printf(num):
    for n in range(num):
        print('-', end='', flush=True)
    print(flush=True)

def escreva(txt):
    printf(len(txt))
    print(txt, flush=True)
    printf(len(txt))
    sleep(0.7)