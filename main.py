#Modulo contenedor de la clase "Afiliado"
from Afiliados import *
#from Lotes import *
#from Planes import *
#from Citas import *
from sql import *

class main:
    def __init__(self):
        sqlObj = sql()
        self.__con = sqlObj.get_con()
        
inicio = main()