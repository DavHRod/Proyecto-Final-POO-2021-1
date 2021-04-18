#Importacion de librerias a usar
import sqlite3
from sqlite3 import Error
from datetime import date
from datetime import datetime

#Variables a Usar
resp="" #Variable que almacena la respuesta del usuario "Menu()"

#Funcion de iniciacion de la base de datos
def sql_connection():
    try:
        con = sqlite3.connect('ProgamaDeVacunacion.db')
        return con
    except Error:
        print(Error)

#Funcion de creacion primary keys
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE Afiliados(Numero_de_identificacion integer PRIMARY KEY, Nombre text, Apellido text, Direccion text, Telefono integer, Correo text, Ciudad text,Fecha_de_nacimiento datetime,Fecha_de_afiliacion datetime,Fecha_de_desafiliacion datetime,Vacunado bool)")
"""
#Funcion Menu
def Menu():
    Cases={1:"Afiliar",2:"Consultar",3:"Desafiliar",4:"Salir"} #Diccionario de Casos
    #Mensajes de Inicio del Menu
    print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
    print("1.Afiliar un Paciente \n2.Consultar un Afiliado\n3.Desafiliar un Paciente\n4.Salir")
    #Recepcion de la respuesta del Usuario
    resp=int(input())
    #Casos de funcionamiento
"""
    

def afiliarPaciente():
    noIdentificacion=input("Ingrese el número de identificación del paciente: ")
    nombre=input("Ingrese el nombre del paciente: ")
    apellido=input("Ingrese el apellido del paciente: ")
    direccion=input("Ingrese la dirección de residensia del paciente: ")
    telefono=int(input("Ingrese un número de contacto: "))
    correo=input("Ingrese el correo electrónico del paciente: ")
    ciudad=input("Ingrese la ciudad en la que reside el paciente: ")
    year=int(input("Ingrese el año de nacimiento:"))
    month=int(input("Ingrese el mes de nacimiento: "))
    day=int(input("Ingrese el día de nacimiento: "))
    fechaNacimiento=datetime.date(year, month, day)
    datosPaciente=(noIdentificacion,nombre,apellido,direccion,telefono,correo,ciudad,fechaNacimiento,date.today(),None,False)
    cursorObj.execute("INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosPaciente)
    con.commit()
#def consultarAfiliado():

    
#def desafiliarPaciente():



#Conexion con la base de datos
con=sql_connection()

#Ejecucion de funciones
sql_table(con)
#Menu()
afiliarPaciente()


#Cerrar conexion
con.close()
"""
Acá dejamos los comandos sqlite3
Crear// Tabla cursorObj.execute("CREATE TABLE Nombre_De_Tabla(Campo1 Tipo_Dato Situacional(PRIMARY KEY), Campo2 Tipo_Dato, N_Campos Su_Tipo_Dato)")
Insert// cursorObj.execute("INSERT INTO Nombre_De_Tabla VALUES(Campo1, Campo2, N_Campos_Concordes_Al_#_Campos)")
Updates// cursorObj.execute('UPDATE Nombre_De_Tabla SET Campo_Modificar = Valor_Nuevo where Campo_de_Identificacion = PRIMARY KEY')

Recordar que existen comandos que no funcionan correctamente sin un SELECT
Select// cursorObj.execute('SELECT Campo1, Campo2, N_campos FROM Nombre_de_tabla')
Para seleccionar todo usar * en ves de campos

Deletes// cursorObj.execute('DELETE FROM Nombre_De_Tabla').rowcount
.rowcount, devuelve el numero de filas borradas

!!!!!Drop!!!!!// DROP TABLE Nombre_De_Tabla
"""