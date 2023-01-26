import os

#Listas
funcionarios = []

#Menus
def menuEditar():
  print('1 -- Editar Nome')
  print('2 -- Editar CPF')
  print('3 -- Editar Cargo')
  print('4 -- Editar Salario')
  print('5 -- Editar Telefones')
  print('0 -- SAIR')

def menuInicial():
  print('\n1 -- Cadastrar Funcionario')
def menuTotal():
  menuInicial()
  print('2 -- Pesquisar funcionario')
  print('3 -- Cadastrar novo telefone')
  print('4 -- Editar dados do funcionário')
  print('5 -- Deletar funcionário')
  print('0 -- SAIR')

#Funções
def encontrarFuncionario(cpfFuncionario):
  for i in funcionarios:
    if  i['CPF'] == cpfFuncionario:
      return i
def cadastrar():
  telefones = list()
  nome = input('\nNome do funcionario:\n')
  cpf = input('\nCFP:\n')
  cpfPesquisa = encontrarFuncionario(cpf)
  while cpfPesquisa in funcionarios:
    cpf = input('\nErro: CPF já cadastrado!\nAdicionar CFP válido:\n')
    cpfPesquisa = encontrarFuncionario(cpf)
  cargo = input('\nCargo:\n')
  salario = -1
  while salario < 0:
    salario = float(input('\nNão adicione um valor NEGATIVO!\nSalario (R$):\n'))
  while True:
    aux = input('\nDeseja adicionar um telefone? [S/N]: ')
    if aux == 'S':
      numeroTel = input('\nAdicionar telefone: ')
      telefones.append(numeroTel)
    elif aux == 'N':
      break
    else:
      print('\nOperação inválida!\nTente novamente.')
  return {'NOME': nome, 'CPF': cpf, 'CARGO': cargo, 'SALARIO': salario, 'TELEFONES': telefones}
def pesquisar(cpfFuncionario):
  for i in funcionarios:
    if cpfFuncionario == i['CPF']:
      print(i)
  


def addTelefone(cpfFuncionario):
  aux = encontrarFuncionario(cpfFuncionario)
  novoNumTel = input('Adicionar telefone: ')
  aux['TELEFONES'].append(novoNumTel)
  os.system('cls')
  print(f"\nNovo telefone addicionado a {aux['NOME']}")
def deletarFuncionario(cpfFuncionario):
  for i in funcionarios:
    if cpfFuncionario == i['CPF']:
      funcionarios.remove(i)
      print('Funcionário removido com sucesso!')
def editarCadastro(cpfFuncionario):
  for aux in funcionarios:
    if cpfFuncionario == aux['CPF']:
      while True:
        menuEditar()
        op = int(input('\nOpção: '))
        os.system('cls')
        if op == 1:
          aux['NOME'] = input("Novo Nome:\n")
        elif op == 2:
          cpf = input('Inserir CPF: ')
          cpfPesquisa = encontrarFuncionario(cpf)
          while cpfPesquisa in funcionarios:
            cpf = input('\nErro: CPF já cadastrado!\nAdicionar CFP válido:\n')
            cpfPesquisa = encontrarFuncionario(cpf)
          aux['CPF'] = cpf
        elif op == 3:
          aux['CARGO'] = input("Novo cargo:\n")
        elif op == 4:
          aux['SALARIO'] = float(input("\nNovo salário:\n"))
        elif op == 5:
          print("\n1 -- Adicionar Telefone\n2 -- Remover telefone")
          aux2 = int(input('Opção: '))
          if aux2 == 1:
            addTelefone(cpfFuncionario)
          elif aux2 == 2:
            removeTel = input('Número a remover:\n')
            if removeTel in aux['TELEFONES']:
              aux['TELEFONES'].remove(removeTel)
              os.system('cls')
              print('Telefone removido com sucesso!')
            else:
              print('ERRO: NÚMERO NÃO ENCONTRADO!')
        elif op == 0:
          print('\nCadastro atualizado!')
          break
        



#Executar
while True:
  if len(funcionarios) == 0:
    menuInicial();
    print('0 -- Sair')
    opMenuInicial = int(input('Opção: '))
    os.system('cls')
    if opMenuInicial == 1:
      newFuncionario = cadastrar()
      funcionarios.append(newFuncionario)
    elif opMenuInicial == 0:
      break
  else:
    menuTotal()
    opMenuTotal = int(input('\nOpção: '))
    os.system('cls')
    if opMenuTotal == 1:
      novoCadastro = cadastrar()
      funcionarios.append(novoCadastro)
    elif opMenuTotal == 2:
      aux = input('Inserir CPF do funcionário:\n')
      cpfPesquisa = encontrarFuncionario(aux)
      if cpfPesquisa in funcionarios:
        pesquisar(aux)
      else:
        print('Nada encontrado')
    elif opMenuTotal == 3:
      aux = input('Inserir CPF do funcionário:\n')
      cpfPesquisa = encontrarFuncionario(aux)
      if cpfPesquisa in funcionarios:
        addTelefone(aux)
    elif opMenuTotal == 4:
      aux = input('Inserir CPF do funcionário:\n')
      cpfPesquisa = encontrarFuncionario(aux)
      if cpfPesquisa in funcionarios:
        editarCadastro(aux)
    elif opMenuTotal == 5:
      aux = input('Inserir CPF do funcionário:\n')
      cpfPesquisa = encontrarFuncionario(aux)
      if cpfPesquisa in funcionarios:
        deletarFuncionario(aux)
    elif opMenuTotal == 0:
      break
    else:
      print('Operação inválida!')