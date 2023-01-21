# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado

preco_casa = float(input('Preço da casa: '))
salário = float(input('Salário: '))
anos = float(input('Em quantos anos irá pagar: '))
mes = anos * 12
if (preco_casa/mes) > salário * 0.3:
    print('Negado')
else:
    print("Confirmado")