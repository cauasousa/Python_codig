from random import randint
aposta = set()
ap = set()

números = 0
## MEGA-SENA
num = 0
while num < 5:
    while números < 6:
        aposta.add(randint(1, 60))
        números += 1
    print(aposta)
    números = 0
    aposta.clear()
    num += 1


