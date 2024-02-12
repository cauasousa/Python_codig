import random
import emoji

print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.emojize("Olá, Mundo :kissing:", language='alias'))
#print(emoji.emojize("Olá, Mundo! :gritar:", use_aliases=True))

num = random.random()
print(f'Número entre 0 e 1: {num}')

num = random.randint(1,100)
print(f'Número entre 1 e 100: {num}')



