from Afiliados import *
from Lotes import *
from Planes import *
from Citas import *
import sqlite3
from sqlite3 import Error

class main:
    def __init__(self):
        self.resp = None
    def principal(self,con):
        navi=menu()
        #Diccionario de casos del menu principal
        casosPrincipal={1:"Datos",2:"Lotes",3:"Plan",4:"Citas",5:"Salir"}
        #Bucle de comprobación
        while True:
            print("\nPorfavor escoja que tarea quiere realizar")
            #Comprobación del tipo de dato
            try:
                #Recepcion de la respuesta para el menu
                self.resp=int(input("1.Gestionar Datos\n2.Gestionar Lotes\n3.Gestionar Plan\n4.Gestionar Citas\n5.Salir\n"))
                #Ruptura del bucle de comprobación
                break
            except:
                #Mensaje de Error
                print("Debe ser un Numero")
        #Condicionales de uso del Menu Principal: verifica que la entrada se encuentre entre las opciones ofrecidas por el menú
        if self.resp > 0 and self.resp < 6:
            #Llamado de las funciones según opción elegida 
            if casosPrincipal[self.resp]=="Datos":
                navi.datos(con)
            elif casosPrincipal[self.resp]=="Lotes":
                navi.lotes(con)
            elif casosPrincipal[self.resp] == "Plan":
                navi.planes(con)
            elif casosPrincipal[self.resp] == "Citas":
                navi.citas(con)
            elif casosPrincipal[self.resp] == "Salir":
                con.close()
                exit()
        else:
            #Mensaje de Error
            print("Deber se una respuesta Valida")
            self.principal()

class menu(main):
    def __init__(self):
        super().__init__()
    #Funcion Menu para gestion de datos de los pacientes
    def datos(self,con):
        afil=afiliado()
        #Diccionario de casos del menu datos
        casosDatos={1:"Afiliar",2:"Consultar",3:"Desafiliar",4:"Vacunar",5:"Volver",6:"Salir"} #Diccionario de Casos
        #Mensajes de Inicio del Menu
        while True:
            #Comprobacion del tipo de dato
            try:
                #Recepción de la respuesta del usuario
                self.resp = int(input("\nPorfavor escoja que tarea quiere realizar\n1.Afiliar un Paciente \n2.Consultar un Afiliado\n3.Desafiliar un Paciente\n4.Vacunar\n5.Volver\n6.Salir\n"))
                #Ruptura del bucle de comprobación
                break
            except:
                #Mensaje de Error
                print("Debe ser un Numero")
        #Condicionales de uso del Menu de Gestión de Datos: verifica que la entrada se encuentre entre las opciones ofrecidas por el menú
        if self.resp > 0 and self.resp < 7:
            #Condicionales de uso del Menu Para Gestion De Datos: Llamado de las funciones según opción elegida 
            if casosDatos[self.resp] == "Afiliar":
                afil.afiliar(con)
                self.datos(con)
            elif casosDatos[self.resp] == "Consultar":
                afil.consultar(con)
                self.datos(con)
            elif casosDatos[self.resp] == "Desafiliar":
                afil.desafiliar(con)
                self.datos(con)
            elif casosDatos[self.resp] == "Vacunar":
                afil.vacunar(con)
                self.datos(con)
            elif casosDatos[self.resp]=="Volver":
                self.principal(con)
            elif casosDatos[self.resp] == "Salir":
                con.close()
                exit()
        else:
            #Mensaje de Error
            print("\nDebe ser una opcion valida")
            self.datos(con)

    #Funcion menu de gestion de lotes de vacunas
    def lotes(self, con):
        lotesN = lote()
        #Diccionario de casos del menu Lotes
        casosLotes={1:"Crear",2:"Consultar", 3:"Regresar",4:"Salir"}
        #Bucle de comprobación de entrada
        while True:
            #Comprobación para el tipo de dato
            try:
                #Recepción de la respuesta
                self.resp=int(input("\nPorfavor escoja que tarea quiere realizar\n1.Crear Lote\n2.Consultar Lote\n3.Regresar\n4.Salir\n"))
                #Ruptura del bucle de comprobación
                break
            except:
                #Mensaje de Error
                print("Debe ser un Numero")
        #Condicional para mantener la respuesta dentro del rango del menú
        if self.resp > 0 and self.resp < 5:
            #Condicionales de uso del Menu Para Gestion De Lotes: Llamado de las funciones según opción elegida 
            if casosLotes[self.resp] == "Crear":
                lotesN.crear(con)
                self.lotes(con)
            elif casosLotes[self.resp] == "Consultar":
                lotesN.consultar(con)
                self.lotes(con)
            elif casosLotes[self.resp] == "Regresar":
                self.principal(con)
            elif casosLotes[self.resp] == "Salir":
                con.close()
                exit()
        else:
            #Mensaje de error en caso de no estar en el intervalo
            print("Deber se una respuesta Valida")
            self.lotes(con)
    #Funcion menu para gestion de planes de vacunacion
    def planes(self,con):
        planN = plan()
        #Diccionario de casos del menu Planes
        casosPlan={1:"Crear",2:"Consultar", 3:"Regresar",4:"Salir"}
        #Bucle de comprobación de entrada
        while True:
            #Comprobación para el tipo de dato
            try:
                #Recepción de la respuesta
                self.resp=int(input("\nPorfavor escoja que tarea quiere realizar\n1.Crear Plan\n2.Consultar Plan por ID\n3.Regresar\n4.Salir\n"))
                #Ruptura del bucle de comprobación
                break
            except:
                #Mensaje de Error
                print("Debe ser un Numero")
        #Condicional para mantener la respuesta dentro del rango del menú
        if self.resp > 0 and self.resp < 5:
            #Condicionales de uso del Menu Para Gestion De Planes: Llamado de las funciones según opción elegida 
            if casosPlan[self.resp] == "Crear":
                planN.crear(con)
                self.planes(con)
            elif casosPlan[self.resp] == "Consultar":
                planN.consultar(con)
                self.planes(con)
            elif casosPlan[self.resp] == "Regresar":
                self.principal(con)
            elif casosPlan[self.resp] == "Salir":
                con.close()
                exit()
        else:
            #Mensaje de error en caso de no estar en el intervalo
            print("Deber se una respuesta Valida")
            self.planes(con)
    #Funcion menu para gestion de citas de vacunacion
    def citas(self, con):
        citasN = citas()
        #Diccionario de casos del menu Citas
        casosCitas={1:"Calcular Citas",2:"Consulta Individual",3:"Consulta General",4:"Regresar",5:"Salir"} 
        #Bucle de comprobacion de entrada
        while True:
            #Comprobación para el tipo de dato
            try:
                #Recepción de la respuesta
                self.resp=int(input("\nPorfavor escoja que tarea quiere realizar\n1.Calcular Citas\n2.Consulta Individual\n3.Consulta General\n4.Regresar\n5.Salir\n")) 
                #Ruptura del bucle de comprobación
                break
            except:
                #Mensaje de Error
                print("Debe ser un Numero")
        #Condicional para mantener la respuesta dentro del rango del menú
        if self.resp > 0 and self.resp < 6:
            #Condicionales de uso del Menu Para Gestion De Citas: Llamado de las funciones según opción elegida 
            if casosCitas[self.resp] == "Calcular Citas":
                citasN.calcular(con)
                self.citas(con)
            elif casosCitas[self.resp] == "Consulta Individual":
                citasN.consultaIndividual(con)
                self.citas(con)
            elif casosCitas[self.resp] == "Consulta General":
                citasN.consultaGeneral(con)
                self.citas(con)
            elif casosCitas[self.resp] == "Regresar":
                self.principal(con)
            elif casosCitas[self.resp] == "Salir":
                con.close()
                exit()
        else:
            #Mensaje de error en caso de no estar en el intervalo
            print("Deber se una respuesta Valida")
            self.citas(con)

def sql_connection():
    try:
        #Conexión con la base de datos
        con = sqlite3.connect('ProgramaDeVacunacion.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    #Creación de la tabla Afiliados
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS 
    Afiliados(
        Numero_De_Identificacion integer PRIMARY KEY, 
        ID_Plan integer FOREING KEY,
        Nombre text, 
        Apellido text, 
        Direccion text, 
        Telefono integer, 
        Correo text, 
        Ciudad_De_Residencia text,
        Fecha_De_Nacimiento text,
        Fecha_De_Afiliacion text,
        Fecha_De_Desafiliacion text,
        Vacunado text)''')

    #Creación de la tabla Lotes
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS 
    Lotes(
        Codigo_De_Lote integer PRIMARY KEY,
        Fabricante text, 
        Tipo_De_Vacuna text, 
        Cantidad_Recibida integer,
        Cantidad_Asignada integer, 
        Cantidad_Usada integer,
        Dosis_Necesarias integer, 
        Temperatura_De_Almacenamiento integer,
        Efectividad_Identificada integer,
        Tiempo_De_Proteccion integer,
        Fecha_De_Vencimiento text,
        Imagen text)''')

    #Creación de la tabla Planes
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS 
    Planes(
        ID integer PRIMARY KEY, 
        Edad_Min integer, 
        Edad_Max integer,
        Fecha_Inicio text,
        Fecha_Fin text)''')

    #Creación de la tabla Citas
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS
    Citas(
        Numero_De_Cita integer PRIMARY KEY,
        ID_Plan integer,
        Numero_De_Identificacion integer,
        Ciudad_De_Vacunacion text,
        Codigo_De_Lote integer,
        Fecha_De_Cita text,
        Hora_De_Cita integer)''')
        
con=sql_connection()
sql_table(con)
iniciar = main()
iniciar.principal(con)