#Modulo contenedor de la clase "Afiliado"
from Afiliados import *
#Modulo contenedor de las clases para la ejecucion de la interfaz grafica
from User import *
#from Lotes import *
#from Planes import *
#from Citas import *
from sql import *

class main:
    def __init__(self):
        sqlObj = sql()
        self.__con = sqlObj.get_con()
        app = QtWidgets.QApplication([])
        application = principal_win()
        application.show()
        sys.exit(app.exec())
        
inicio = main()
