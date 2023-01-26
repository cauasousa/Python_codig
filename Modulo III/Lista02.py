pessoa = list()
dados = list()

for c in range(0,2):
    dados.append(str(input('Add your name: ')))
    dados.append(int(input('Add Age: ')))
    pessoa.append(dados[:])
    dados.clear()

for c in pessoa:
    print(f"{c[0]} tem {c[1]} anos")
print('FIM')