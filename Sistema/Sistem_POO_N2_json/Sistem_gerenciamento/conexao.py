import json

# Conexão com os arq
class Conexao:
    def __init__(self, way):
        self.way = way

    def Data_base(self):
        try:
            with open(self.way, "r") as arq:
                return json.load(arq)
        except FileNotFoundError:
            print("Data not found")
        except IOError:
            print("Reading Error")
        
        return None
        
    def Update(self, new_dict, cod):
        try:
            data = self.Data_base()
            data[cod] = new_dict

            with open(self.way, "w") as arq:
                json.dump(data, arq, indent=4)

        except Exception:
            print('Error in Update')
            return False
        else:
            return True
    
    def Delete(self, cod):

        try:
            data = self.Data_base()
            del data[cod]
            with open(self.way, "w") as arq:
                json.dump(data, arq, indent=4)

        except KeyError:
            print("\t\t\033[1;31mUSUA NOT FIND\033[m")
        except Exception:
            # AttributeError : data -> null
            print("\t\t\033[1;31mError\033[m")
        else:
            print("\t\t\033[1;31mDeletado\033[m")