try:
    n = int(input('Número: '))
    b = int(input('Número: '))
    r = n / b
## except: 
## except (ValueError, TypeError):   -> erro de valor ou tipo faça isso
## except ZeroDivisionError:        -> não é possivel dividir numero por zero
## execept keyboardinterrupt:
except Exception as erro:
    #se falhar
    print(f'Errooo!!!{erro.__class__}')
else:
    #deu certo
    print(f'O resultado foi {r}')
finally:
    #certou/falha
    print('Volte sempre!')