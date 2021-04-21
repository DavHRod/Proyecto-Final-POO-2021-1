#Importacion de librerias a usar
import sqlite3
from sqlite3 import Error
from datetime import date
from datetime import datetime

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
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Afiliados(Numero_de_identificacion integer PRIMARY KEY, Nombre text, Apellido text, Direccion text, Telefono integer, Correo text, Ciudad text,Fecha_de_nacimiento datetime,Fecha_de_afiliacion datetime,Fecha_de_desafiliacion datetime,Vacunado bool)")

#Funcion Menu Principal Para Acceso A Funciones de Datos y Lotes
def menuPrincipal():
    #Diccionario de casos del menu principal
    casosPrincipal={1:"Datos",2:"Lotes",3:"Salir"}
    #Mensaje de inicio 
    print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
    #Recepcion de la respuesta para el menu
    resp=int(input("1.Gestionar Datos\n2.Gestionar Lotes\n3.Salir\n"))
    if casosPrincipal[resp]=="Datos":
        menuDatos()
    elif casosPrincipal[resp]=="Lotes":
        menuLotes()
    else:
        con.close()
        exit()

#Funcion Menu para gestion de datos de los pacientes
def menuDatos():
    Cases={1:"Afiliar",2:"Consultar",3:"Desafiliar",4:"Vacunar",5:"Volver",6:"Salir"} #Diccionario de Casos
    #Mensajes de Inicio del Menu
    print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
    print("1.Afiliar un Paciente \n2.Consultar un Afiliado\n3.Desafiliar un Paciente\n4.Vacunar\n5.Volver\n6.Salir")
    #Recepcion de la respuesta del Usuario
    resp=int(input())
    #Casos de funcionamiento
    if Cases[resp] == "Afiliar":
        afiliarPaciente(con)
    elif Cases[resp] == "Consultar":
        consultarAfiliado(con)
    elif Cases[resp] == "Desafiliar":
        desafiliarPaciente(con)
    elif Cases[resp] == "Vacunar":
        vacunarAfiliado(con)
    elif Cases[resp]=="Volver":
        menuPrincipal()
    elif Cases[resp] == "Salir":
        con.close()
        exit()



#Funcion menu de gestion de lotes de vacunas
def menuLotes(con):
    Cases={1:"Crear",2:"Consultar"}
    #Mensajes de Inicio del Menu
    resp=input("1.Crear Lote\n2.Consultar Lote\n3.Regresar")

#Función afiliarPaciente: Esta función recibe los datos de un nuevo paciente a afiliar
def afiliarPaciente(con):
    cursorObj = con.cursor()
    #Ingreso de No. de identificación de un nuevo paciente
    noIdentificacion=input("Ingrese el número de identificación del paciente: ")
    #Ingreso de nombre de un nuevo paciente
    nombre=input("Ingrese el nombre del paciente: ")
    #Ingreso de apellido de un nuevo paciente
    apellido=input("Ingrese el apellido del paciente: ")
    #Ingreso de dirección de residencia de un nuevo paciente
    direccion=input("Ingrese la dirección de residencia del paciente: ")
    #Ingreso de telefono de un nuevo paciente
    telefono=int(input("Ingrese un número de contacto: "))
    #Ingreso de correo de un nuevo paciente
    correo=input("Ingrese el correo electrónico del paciente: ")
    #Ingreso de ciudad de origen de un nuevo paciente
    ciudad=input("Ingrese la ciudad en la que reside el paciente: ")
    #Ingreso de año de nacimiento de un nuevo paciente
    year=int(input("Ingrese el año de nacimiento:"))
    #Ingreso de mes de nacimiento de un nuevo paciente
    month=int(input("Ingrese el mes de nacimiento: "))
    #Ingreso de día de nacimiento de un nuevo paciente
    day=int(input("Ingrese el día de nacimiento: "))
    #Unificación de la fecha de nacimiento del nuevo paciente
    fechaNacimiento=date(year, month, day)
    #Tupla con todos los datos ingresados anteriormente
    datosPaciente=(noIdentificacion,nombre,apellido,direccion,telefono,correo,ciudad,fechaNacimiento,date.today(),None,False)
    #Añadir los datos a la tabla de Afiliados
    cursorObj.execute("INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?)",datosPaciente)
    con.commit()

def consultarAfiliado(con):
    cursorObj = con.cursor()
    noIdentificacion=int(input("Ingrese el número de identificación del paciente a consultar: "))
    cursorObj.execute('SELECT * FROM Afiliados WHERE Numero_de_identificacion=?',(noIdentificacion,))
    consultados=cursorObj.fetchall()
    for consultados in consultados:
        print(consultados)

    
def desafiliarPaciente(con):
    cursorObj = con.cursor()
    noIdentificacion=int(input("Ingrese el número de identificación del paciente a desafiliar: "))
    cursorObj.execute('UPDATE Afiliados SET Fecha_de_desafiliacion=? WHERE Numero_de_identificacion=?',(date.today(),noIdentificacion))
    con.commit()

def vacunarAfiliado(con):
    cursorObj = con.cursor()
    noIdentificacion=int(input("Ingrese el número de identificación del paciente a Vacunar: "))
    cursorObj.execute('UPDATE Afiliados SET Vacunado=True WHERE Numero_de_identificacion=?',(noIdentificacion,))
    con.commit()

#Conexion con la base de datos
con=sql_connection()

#Ejecucion de funciones
sql_table(con)
menuPrincipal()

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