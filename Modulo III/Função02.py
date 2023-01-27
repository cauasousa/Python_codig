#Exercicio 101 até 106

def contador(i, f, p):
    #docstring
    """
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    global fim 
    fim = 22
    
    for c in range(i, f, p):
        print(c, end=' ', flush=True)
    print()

fim = 10
print(f'Antes do Global {fim}')
print(f'Depois do Global {fim}')
# interacive help
#-> help('Nome da biblioteca ou função')
#help()
#########################################################
# dosctrings
#->
#help(contador)
#########################################################
# Argumentos opcionais
#->def contador(i=0, f=0, p=0)
#########################################################
# Escopo e Varáveis
#->
#########################################################
# Retorno de resultados
#->