#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
import httpx

base_currency = input('Digite a moeda de base: ').upper() #digite USD
currency = input('Digite a moeda desejada: ').upper()     #digite BRL

response = httpx.get(
    url = 'https://api.exchangerate.host/lates?base={base_currency}').json()

currency_data = response['rates']
print(f'l {base_currency} vale {currency_data.get(currency)} {currency}')

din = float(input('Quanto tem na carteira: '))
convertor = din / currency_data.get(currency)
print(f'Equivale a {convertor:.3f} dolares')
