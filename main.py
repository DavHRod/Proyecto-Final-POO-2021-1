#--------- Importaciones de librerias a usar -----------------------------------------------------------------
from User import * #Modulo contenedor de las clases para la ejecucion de la interfaz grafica
from sql import * #Modulo que maneja base de datos

class main: #Clase inicializadora del programa y la base de datos
    def __init__(self): #Método principal de la clase
        self.sqlObj = sql() #Creación de un objeto tipo sql
        self.__con = self.sqlObj.get_con() #Ejecución del método get_con para creación de las tablas
        app = QtWidgets.QApplication([]) #Creación de la app Qt
        application = principal_win() #Creación del objeto principal_win (ventana principal)
        application.show() #Muestra la ventana del menú principal
        self.sqlObj.close() #Ciere de la conexión con la base de datos
        sys.exit(app.exec()) #Sobrescritura del método del sistema (exit)
        
inicio = main()
