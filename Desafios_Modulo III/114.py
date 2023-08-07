#crie um código em python que teste se o site Pudim está acessível 
# pelo computador usado
########################################################3
# try:
#     from selenium import webdriver
#     from selenium.webdriver.common.keys import Keys

#     navegador = webdriver.Chrome()
#     navegador.get("http://pudim.com.br/")

# except Exception as erro:
#     print(f'Erro de {erro.__cause__}')
# else:
#     print('Certo né')

###########################################################
# import urllib
# import urllib.request

# try:
#     site = urllib.request.urlopen('http://pudim.com.br/')
# except urllib.error.URLError:
#     print('O site Pudim não está acessível')
# else:
#     print('Está Acessível')
#     #print(site.read())