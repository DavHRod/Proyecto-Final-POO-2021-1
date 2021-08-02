import sqlite3
from sqlite3 import Error

class sql:
    def __init__(self):
        self.__con = self.__sql_connection()
        self.__cursor=self.__con.cursor()
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

    def cargar_tabla(self, tabla, columna = "*"):
        self.__cursor.execute(f"SELECT {columna} FROM {tabla}")
        tupla = self.__cursor.fetchall()
        return tupla
    
    def guardar_tabla(self, tabla, carga):
        try:
            self.__cursor.execute(f"INSERT INTO {tabla} VALUES {carga}")
        except:
            if tabla == "Afiliados":
                carga_update = (carga[1], carga[2], carga[3], carga[4], carga[5], carga[6], carga[7], carga[8], carga[9], carga[10], carga[11], carga[12] )
                self.__cursor.execute(f"UPDATE Afiliados SET ID_Plan = ? , Nombre = ?, Apellido = ? , Direccion = ? , Telefono = ? , Correo = ? , Ciudad_De_Residencia = ? , Fecha_De_Nacimiento = ? , Edad = ? , Fecha_De_Afiliacion = ?,Fecha_De_Desafiliacion = ? , Vacunado = ? WHERE Numero_De_Identificacion = {carga[0]}",carga_update)
            elif tabla == "Planes":
                carga_update = (carga[1], carga[2], carga[3])
                self.__cursor.execute(f"UPDATE Planes SET Edad_Min = ?, Edad_Max = ?, Fecha_inicio = ? WHERE ID = {carga[0]}",carga_update)
            elif tabla == "Lotes":
                carga_update = (carga[1], carga[2], carga[3], carga[4], carga[5], carga[6], carga[7], carga[8], carga[9], carga[10], carga[11] )
                self.__cursor.execute(f"UPDATE Lotes SET Fabricante = ? , Tipo_De_Vacuna = ?, Cantidad_Recibida = ? , Cantidad_Asignada = ? , Cantidad_Usada = ? , Dosis_Necesarias = ? , Temperatura_De_Almacenamiento = ? , Efectividad_Identificada = ? , Tiempo_De_Proteccion = ? , Fecha_De_Vencimiento = ?,Imagen = ? WHERE Codigo_De_Lote = {carga[0]}",carga_update)
            elif tabla == "Citas":
                return True
        self.__con.commit()

    def __sql_table(self):
        #Creación de la tabla Afiliados
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS 
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
            Edad text,
            Fecha_De_Afiliacion text,
            Fecha_De_Desafiliacion text,
            Vacunado text)''')

        #Creación de la tabla Lotes
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS 
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
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS 
        Planes(
            ID integer PRIMARY KEY, 
            Edad_Min integer, 
            Edad_Max integer,
            Fecha_Inicio text)''')

        #Creación de la tabla Citas
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS
        Citas(
            Numero_De_Cita integer PRIMARY KEY,
            ID_Plan integer,
            Numero_De_Identificacion integer,
            Ciudad_De_Vacunacion text,
            Codigo_De_Lote integer,
            Fecha_De_Cita text,
            Hora_De_Cita integer)''')

    def close(self):
        self.__con.close()