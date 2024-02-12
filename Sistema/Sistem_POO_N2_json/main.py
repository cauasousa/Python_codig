from menu.G_menu import Menu

#      :)
# cpf1 =  091.585.720-07
# cpf2 = 718.669.910-35
# cpf3 = 094.937.290-01

way1 = "data_base\\motorista.json"
way2 = "data_base\\veiculo.json"
way3 = "data_base\\viagem.json"
way4 = "data_base\\manutencao.json"
way5 = "data_base\\abastecimento.json"

my_menu = Menu(way1, way2, way3, way4, way5)

cond = True
while cond != False:  
    cond = my_menu.Principal()