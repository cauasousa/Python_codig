from menu.G_menu import Menu
from tratamento_erros.class_erros.Input_Trat import Input_Validar
from classes.PMotorista import Motorista
from classes.P_Veiculo import Veiculo
from classes.Viagem import Viagem
from classes.P_Abastecimento import Abastecimento
from classes.Manutencao import Manutencao

cond = True


#      :)

#cod = 150
#cod = 169
#cod = 182
mot1 = Motorista("François", 11111, "223212", "34221")
mot2 = Motorista("Ana", 22222, "223212", "34221")
mot3 = Motorista("Maria", 33333, "223212", "34221")
mot = [
        { 
            11111 :mot1,
            22222 :mot2,
            33333:mot3
        },
        
        [11111, 22222, 33333]
    ]
vei1 = Veiculo("Fiat", "UNO", "2003", "BCC009", "36563652", "Branco", 500.0)
vei2 = Veiculo("Fiat", "Toro", "2003", "BCC006", "36563652", "Branco", 500)
vei3 = Veiculo("Fiat", "Argo", "2003", "BCC007", "36563652", "Branco", 500)

veic = [
        {
            "BCC009": vei1,
            "BCC006": vei2,
            "BCC008": vei3
        },

        ["BCC009", "BCC006", "BCC008"]
    ]
via1 = Viagem( "Caxias", "Bacabal", 200.0, mot1, vei1)
via2 = Viagem("Caxias", "Bacabal", 200.0, mot1, vei1)

viagens=[
        {
            1 : via1,
            2 : via2
        },

        [1, 2]
    ]

man1 = Manutencao( 1000.0, "preventiva","02-02-2023", vei1)
man2 = Manutencao( 1000.0,"preventiva", "02-02-2023", vei1)

manutencoes =[
        {
            1:man1,
            2: man2
        },

        [1, 2]
    ]
abt1 = Abastecimento(vei1, 400.0, "4-2-2023", 150)
abt2 = Abastecimento(vei1, 400.0, "4-2-2023", 150)
abt3 = Abastecimento(vei1, 400.0, "4-2-2023", 150)


abastecimentos=[
    {
        1:abt1,
        2:abt2,
        3:abt3
    }, 

    [1, 2, 3]
]

my_menu = Menu(abastecimentos, manutencoes, mot, veic, viagens)


while cond != False:  
    cond = my_menu.Principal()
