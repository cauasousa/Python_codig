# Faça um programa que tenha um função chama área(), que recebea as dimensões de um terreno retangular(largura e comprimento) 
# e mostre a área do terreno
def área(com, lar):
    print('-='*40)
    print('-='*20)
    print(f'Largura de {lar} e Comprimento de {com} corresponde a Área de {lar*com}m²')
    print('-='*20)
    print('-='*40)


largura = float(input('Largura: '))
comprim = float(input('Comprimento: '))
área(largura, comprim)