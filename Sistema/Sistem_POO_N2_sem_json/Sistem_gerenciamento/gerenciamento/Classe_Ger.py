from abc import abstractmethod
from Sistem_gerenciamento.interface.face import Abst_Nivel_3_sist, Abst_Nivel_2_sist, Abst_Nivel_l_sist
from random import randint

class Gerenciamento_N1(Abst_Nivel_l_sist):
    
    def __init__(self, data_base, cod) -> None:
        self._data_base = data_base
        self._gerador_cod = cod

    def _validar_cod(self, lista, cod):
        if not lista: return False
        if(lista[0] == cod) : return True
        return self._validar_cod(lista[1:], cod)

    def add(self, cadast_new):
        cod_aleatorio = 0

        while True:
            cod_aleatorio = randint(101, 200)
            if self._validar_cod(self._gerador_cod, cod_aleatorio) == False: 
                self._gerador_cod.append(cod_aleatorio)
                break
        
        self._data_base[cod_aleatorio] = cadast_new
        print('\t\t\033[1;34;40mSeu Código é\033[m\033[1;32;40m', cod_aleatorio, '\033[m')
    
    def quant_min(self):
        if(len(self._gerador_cod) > 0):
            return True
        return False


class Gerenciamento_N2(Gerenciamento_N1, Abst_Nivel_2_sist):
    
    def __init__(self, data_b, cod) -> None:
        super().__init__(data_b, cod)

    def __find(self, cod):       
        objs = self._data_base.get(cod)

        if(objs == None):
            print("\t\t\033[1;31m Não Cadastrado!\033[m")
        else:
            return objs
        
        return None
    
    @abstractmethod
    def editar():
        pass

############################
       
class Gerenciamento_N3(Gerenciamento_N2, Abst_Nivel_3_sist):

    def __init__(self, bve, cod, quant):
        super().__init__(bve, cod)
        # self._data_base = dict()
        self._quant = quant

    def add(self, new_inst, cod):

        if self._validar_cod(self._gerador_cod, cod) == True:
            
            print("\t\t\033[1;32mJá Possui Cadastro!!\033[m")
            return
        self._gerador_cod.append(cod)
        self._data_base[cod] = new_inst
        self._quant+=1
        print('\t\t\033[1;34;40mCadastrado!!\033[m')

    def find(self, cod):
        return self._Gerenciamento_N2__find(cod)
    
    @abstractmethod
    def editar():
        pass

    def deletar(self, cod):
        
        try:
            del self._data_base[cod]
            self._gerador_cod.remove(cod)
            self._quant-=1
        except KeyError:
            print("\t\t\033[1;31mUSUA NOT FIND\033[m")
        else:
            print("\t\t\033[1;31mDeletado\033[m")

    @property
    def quant(self):
        return self._quant