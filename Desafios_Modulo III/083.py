#Crie um programa onde o usário digie uma expressão qualquer que use parênteses.
#  Seu aplicativo deverá analisar se a expressão passada está 
# com os parênteses abertos e fechados na ordem correta

## ((a+b) * c)
## ((a+b)*c))  ->errado
## ((a+b)*(a*c)-2   ->errado

Lista = []
cont = 0

while True:
    Lista.append(input('Expressão: ').strip())

    test = Lista[cont]
    if test.count('(') == test.count(')'):
        print('Valid')
    else:
        print('Not Valid')

    op = ' '
    while op not in 'SN':
        op = input('Add ? (S/N) ').strip().upper()
    if 'N' in op: 
        break
    cont+=1