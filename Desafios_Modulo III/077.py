# crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
palavra = 'Caua', 'Joana', 'Maria', 'Beatriz', 'Janiel', 'Ana', 'Testando'
print('---'*20)
for c in palavra:
    print(f'-> A Palavra {c} contém a vogal: ', end ='')
    i = 0
    while i < len(c):
        if c[i] in 'AEIOUaeiou':
            print(f'-{c[i]}', end='')
        i+=1
    print('.')
print('')
print('---'*20)
