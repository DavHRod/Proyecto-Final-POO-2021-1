import sqlite3
from sqlite3 import Error

class sql:
    def __init__(self):
        self.__con = self.__sql_connection()
        self.__sql_table()

    def get_con (self):
        self.__con = self.__sql_connection()
        return self.__con

    def __sql_connection(self):
        try:
            #Conexión con la base de datos
            con = sqlite3.connect('ProgramaDeVacunacion.db')
            return con
        except Error:
            print(Error)

    def __sql_table(self):
        cursorObj = self.__con.cursor()
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