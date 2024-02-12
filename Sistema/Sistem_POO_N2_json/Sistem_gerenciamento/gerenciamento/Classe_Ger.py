from abc import abstractmethod
from Sistem_gerenciamento.interface.face import Abst_Nivel_3_sist, Abst_Nivel_2_sist, Abst_Nivel_l_sist
from random import randint
from Sistem_gerenciamento.conexao import Conexao

class Gerenciamento_N1(Abst_Nivel_l_sist):
    
    def __init__(self, way):
        self.cnx = Conexao(way)

    def _validar_cod(self, cod):
        data = self.cnx.Data_base()
        if None == data:
            return False
        
        for i in data.keys():
            if i == cod:
                return True
        
        return False

    def add(self, cadast_new):
        cod_aleatorio = 0

        while True:
            cod_aleatorio = randint(101, 200)
            if self._validar_cod(cod_aleatorio) == False: 
                break
        
        if self.cnx.Update(cadast_new, cod_aleatorio):
            print('\t\t\033[1;34m Seu Código é\033[m\033[1;32m', cod_aleatorio, '\033[m')
    
    def __quant(self) -> int:
        data = self.cnx.Data_base()
        if data == None : return 0

        cont = 0
        for i in data:
            cont+=1
        return cont
    
    def quant_min(self):
        if(self.__quant() > 0):
            return True
        return False


class Gerenciamento_N2(Gerenciamento_N1, Abst_Nivel_2_sist):

    def __init__(self, way):
        super().__init__(way)

    def __find(self, cod):
        data = self.cnx.Data_base() 
        if(data == None): return None
        
        dict_data = data.get(cod)
        
        if(dict_data == None):
            return None
        else:
            return dict_data
            
    @abstractmethod
    def editar():
        pass

############################
       
class Gerenciamento_N3(Gerenciamento_N2, Abst_Nivel_3_sist):

    def __init__(self, way):
        super().__init__(way)

    def add(self, new_data, cod):

        if self._validar_cod(cod):
            print("\t\t\033[1;32mJá Possui Cadastro!!\033[m")
            return
        
        if self.cnx.Update(new_data, cod):
            print('\t\t\033[1;34;40mCadastrado!!\033[m')

    def find(self, cod):
        return self._Gerenciamento_N2__find(cod)
    
    @abstractmethod
    def editar():
        pass

    def deletar(self, cod):
        self.cnx.Delete(cod)

    @property
    def quant(self):
        return self._Gerenciamento_N1__quant()