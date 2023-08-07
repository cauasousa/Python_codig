#crie um pequeno sistema modularizado que permite cadastrar pessoas
#  pelo seu nome e idade em um arquivo de texto simples.
#o sistema só vai ter 2 opções: cadastrar um nova pessoa 
# e listar todas pessoas cadasradas.
import biblioteca

while True:
    op = biblioteca.menu('        MENU PRINCIPAL', ' - Cadastrar', ' - Lista das Pessoas', ' - Sair do Programa')
    if op == 3:
        break

    arq = 'lista_nome'
    if not biblioteca.ArquivoExiste(arq):
        biblioteca.criarArquivo(arq)
    biblioteca.exe_menu(op, arq)
