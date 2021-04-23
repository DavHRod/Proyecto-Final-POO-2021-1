#Importacion de librerias a usar
import sqlite3
from sqlite3 import Error
from datetime import date
from datetime import datetime

#Funcion de iniciacion de la base de datos
def sql_connection():
    try:
        con = sqlite3.connect('ProgramaDeVacunacion.db')
        return con
    except Error:
        print(Error)

#Funcion de creacion primary keys
def sql_table(con):
    cursorObj = con.cursor()
    #Creacion de la tabla Afiliados
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Afiliados(Numero_de_identificacion integer PRIMARY KEY, Nombre text, Apellido text, Direccion text, Telefono integer, Correo text, Ciudad text,Fecha_de_nacimiento text,Fecha_de_afiliacion text,Fecha_de_desafiliacion text,Vacunado bool)")
    #Creacion de la tabla Lotes
    cursorObj.execute("CREATE TABLE IF NOT EXISTS Lotes(Numero_De_Lote integer PRIMARY KEY, Fabricante text, Tipo_De_Vacuna text, Cantidad_Recibida integer, Cantidad_Usada integer, Dosis_Necesarias integer, Temperatura_De_Almacenamiento integer,Efectividad_Identificada integer,Tiempo_De_Proteccion integer,Fecha_de_Vencimiento text,Imagen text)")

#Funcion Menu Principal Para Acceso A Funciones de Datos y Lotes

#-----DESDE AQUI MODULO DE MENU-------------------------------------------------------------------------------------------------------

def menuPrincipal():
    #Diccionario de casos del menu principal
    casosPrincipal={1:"Datos",2:"Lotes",3:"Salir"}
    #Mensaje de inicio 
    print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
    #Recepcion de la respuesta para el menu
    resp=int(input("1.Gestionar Datos\n2.Gestionar Lotes\n3.Salir\n"))
    #Condicionales de uso del Menu Principal
    if casosPrincipal[resp]=="Datos":
        menuDatos()
    elif casosPrincipal[resp]=="Lotes":
        menuLotes()
    else:
        con.close()
        exit()

#Funcion Menu para gestion de datos de los pacientes
def menuDatos():
    #Diccionario de casos del menu datos
    cases={1:"Afiliar",2:"Consultar",3:"Desafiliar",4:"Vacunar",5:"Volver",6:"Salir"} #Diccionario de Casos
    #Mensajes de Inicio del Menu
    print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
    print("1.Afiliar un Paciente \n2.Consultar un Afiliado\n3.Desafiliar un Paciente\n4.Vacunar\n5.Volver\n6.Salir")
    #Recepcion de la respuesta del Usuario
    resp=int(input())
    #Condicionales de uso del Menu Para Gestion De Datos
    if cases[resp] == "Afiliar":
        afiliarPaciente(con)
    elif cases[resp] == "Consultar":
        consultarAfiliado(con)
    elif cases[resp] == "Desafiliar":
        desafiliarPaciente(con)
    elif cases[resp] == "Vacunar":
        vacunarAfiliado(con)
    elif cases[resp]=="Volver":
        menuPrincipal()
    elif cases[resp] == "Salir":
        con.close()
        exit()

#Funcion menu de gestion de lotes de vacunas
def menuLotes():
    #Diccionario de casos del menu Lotes
    cases={1:"Crear",2:"Consultar", 3:"Regresar",4:"Salir"}
    #Mensajes de Inicio del Menu
    resp=int(input("1.Crear Lote\n2.Consultar Lote\n3.Regresar\n4.Salir"))
    #Condicionales de uso del Menu Para Gestion De Lotes
    if cases[resp] == "Crear":
        crearLote(con)
    elif cases[resp] == "Consultar":
        consultarLote(con)
    elif cases[resp] == "Regresar":
        menuPrincipal()
    elif cases[resp] == "Salir":
        con.close()
        exit()

#-----DESDE AQUI MODULO DE AFILIADOS-------------------------------------------------------------------------------------------------------

#Función afiliarPaciente: Esta función recibe los datos de un nuevo paciente a afiliar y realiza la insercion en la tabla
def afiliarPaciente(con):
    cursorObj = con.cursor()
    #Ingreso de No. de identificación de un nuevo paciente
    noIdentificacion=input("Ingrese el número de identificación del paciente: ")
    noIdentificacion=noIdentificacion.ljust(12)
    #Ingreso de nombre de un nuevo paciente
    nombre=input("Ingrese el nombre del paciente: ")
    nombre=nombre.ljust(20)
    #Ingreso de apellido de un nuevo paciente
    apellido=input("Ingrese el apellido del paciente: ")
    apellido=apellido.ljust(20)
    #Ingreso de dirección de residencia de un nuevo paciente
    direccion=input("Ingrese la dirección de residencia del paciente: ")
    direccion=direccion.ljust(20)
    #Ingreso de telefono de un nuevo paciente
    telefono=input("Ingrese un número de contacto: ")
    telefono=telefono.ljust(12)
    #Ingreso de correo de un nuevo paciente
    correo=input("Ingrese el correo electrónico del paciente: ")
    correo=correo.ljust(20)
    #Ingreso de ciudad de origen de un nuevo paciente
    ciudad=input("Ingrese la ciudad en la que reside el paciente: ")
    ciudad=ciudad.ljust(20)
    #Ingreso de día de nacimiento de un nuevo paciente
    day=input("Ingrese el día de nacimiento: ")
    day=day.rjust(2,"0")
    #Ingreso de mes de nacimiento de un nuevo paciente
    month=input("Ingrese el mes de nacimiento: ")
    month=month.rjust(2,"0")
    #Ingreso de año de nacimiento de un nuevo paciente
    year=input("Ingrese el año de nacimiento:")
    year=year.rjust(4)
    #Concatenación de la fecha de nacimiento del nuevo paciente
    fechaNacimiento=day+"/"+month+"/"+year
    #Función para obtener la fecha actual
    today = date.today()
    #Día actual
    dayActual=today.day
    #Mes actual
    monthActual=today.month
    #Año actual
    yearActual=today.year
    #Concatenación fecha actual
    fechaActual=str(dayActual)+"/"+str(monthActual)+"/"+str(yearActual)
    #Tupla con todos los datos ingresados En la funcion Afiliar
    datosPaciente=(noIdentificacion,nombre,apellido,direccion,telefono,correo,ciudad,fechaNacimiento,fechaActual,None,False)
    #Insercion de los datos a la tabla de Afiliados, Nueva Fila
    cursorObj.execute("INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?)",datosPaciente)
    #Envio de la peticion a la base de datos
    con.commit()

#Función consultarAfiliado: Esta función permite al usuario consultar los datos de un paciente,
#Se debe ingresar el número de identificación del paciente para que la función busque en la tabla los datos
def consultarAfiliado(con):
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    noIdentificacion=int(input("Ingrese el número de identificación del paciente a consultar: "))
    #Seleccion de campos basado en la identificacion de pacientes basado en el Numero_de_identificacion
    cursorObj.execute('SELECT * FROM Afiliados WHERE Numero_de_identificacion=?',(noIdentificacion,))
    #Recoleccion de los datos en la tupla "consultados"
    consultados=cursorObj.fetchall()
    #Impresion de la tupla correspondiente al paciente
    for consultados in consultados:
        print(consultados)

#Función desafiliarPaciente: Con esta función se ingresa la fecha de desafiliación de un paciente    
def desafiliarPaciente(con):
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    noIdentificacion=int(input("Ingrese el número de identificación del paciente a desafiliar: "))
    #Día actual
    dayActual=today.day
    #Mes actual
    monthActual=today.month
    #Año actual
    yearActual=today.year
    #Concatenación fecha actual
    fechaDesafiliacion=str(dayActual)+"/"+str(monthActual)+"/"+str(yearActual)
    #Insercion de la fecha concatenada en la base de datos basado en el Numero_de_identificacion, columna Fecha_de_desafiliacion
    cursorObj.execute('UPDATE Afiliados SET Fecha_de_desafiliacion=? WHERE Numero_de_identificacion=?',(fechaDesafiliacion,noIdentificacion))
    #Envio de la peticion a la base de datos
    con.commit()

#Función vacunarAfiliado: Con esta función se actualiza el estado de vacunación de un afiliado en la tabla afiliado 
def vacunarAfiliado(con):
    cursorObj = con.cursor()
    #Ingreso de número de identificación del paciente a vacunar
    noIdentificacion=int(input("Ingrese el número de identificación del paciente a Vacunar: "))
    #Actualización del estado de vacunación del afiliado basado en el Numero_de_identificacion, columna "Vacunado"
    cursorObj.execute('UPDATE Afiliados SET Vacunado=True WHERE Numero_de_identificacion=?',(noIdentificacion,))
    #Envio de la peticion a la base de datos
    con.commit()

#-----DESDE AQUI MODULO DE LOTES-------------------------------------------------------------------------------------------------------

def crearLote(con):
    cursorObj = con.cursor()
    #Ingreso de No. de lote
    noLote=input("Ingrese el número de lote: ")
    noLote=noLote.ljust(12)
    #Ingreso de nombre del fabricante del lote de vacunas
    fabricante=input("Ingrese el fabricante: ")
    fabricante=fabricante.ljust(12)
    #Ingreso de tipo de vacuna
    tipoVacuna=input("Ingrese el Tipo de Vacuna: ")
    tipoVacuna=tipoVacuna.ljust(20)
    #Ingreso de la cantidad de vacunas recibidas
    cantidadRecibida=input("Ingrese la cantidad recibida: ")
    cantidadRecibida=cantidadRecibida.ljust(6)
    #Ingreso de la cantidad de vacunas usadas
    cantidadUsada=input("Ingrese la cantidad recibida: ")
    cantidadUsada=cantidadUsada.ljust(6)
    #Ingreso de cantidad dosis necesarias
    dosisNecesarias=input("Ingrese el número de dosis necesarias: ")
    dosisNecesarias=dosisNecesarias.ljust(1)
    #Ingreso de temperatura a la que debe ser almacenadas las vacunas
    temperatura=input("Ingrese la temperatura de almacenamiento: ")
    temperatura=temperatura.ljust(3)
    #Ingreso de la efectividad conocida de la vacuna
    efectividad=input("Ingrese la fecha de vencimiento: ")
    efectividad=efectividad.rjust(2,"0")
    #Ingreso de tiempo de protección conocido de la vacuna
    tiempoProteccion=input("Ingrese el tiempo de proteccion de que ofrece la vacuna: ")
    tiempoProteccion=tiempoProteccion.ljust(3)
    #Ingreso de día de vencimiento de la vacuna 
    day=input("Ingrese el día de vencimiento de la vacuna: ")
    day=day.rjust(2,"0")
    #Ingreso de mes de vencimiento de la vacuna
    month=input("Ingrese el mes de vencimiento de la vacuna: ")
    month=month.rjust(2,"0")
    #Ingreso de año de vencimiento de la vacuna
    year=input("Ingrese el año de vencimiento de la vacuna:")
    year=year.rjust(4)
    #Concatenación de la fecha de vencimiento de la vacuna 
    fechaVencimiento=day+"/"+month+"/"+year
    #Imagen: proximamente
    imagen="todavia no prro"
    datosLotes=(noLote,fabricante,tipoVacuna,cantidadRecibida,cantidadUsada,dosisNecesarias,temperatura,efectividad,tiempoProteccion,fechaVencimiento,imagen)
    #Insercion de los datos a la tabla de Lotes, Nueva Fila
    cursorObj.execute("INSERT INTO Lotes VALUES(?,?,?,?,?,?,?,?,?,?,?)",datosLotes)
    #Envio de la peticion a la base de datos
    con.commit()

def consultarLote(con):
    cursorObj = con.cursor()
    #Recepcion del Numero del lote a consultar
    noLote=int(input("Ingrese el número de lote a consultar: "))
    #Seleccion de datos basado en el Numero_De_Lote
    cursorObj.execute('SELECT * FROM Lotes WHERE Numero_De_Lote=?',(noLote,))
    #Recoleccion de los datos en la tupla "consultados"
    consultados=cursorObj.fetchall()
    #Impresion de la tupla correspondiente al lote
    for consultados in consultados:
        print(consultados)
        
#-----DESDE AQUI MODULO DE PLAN DE VACUNACION-------------------------------------------------------------------------------------------------------

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