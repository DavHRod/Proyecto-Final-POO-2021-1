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
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS 
    Afiliados(
        Numero_De_Identificacion integer PRIMARY KEY, 
        ID_Plan FOREING KEY integer,
        Nombre text, 
        Apellido text, 
        Direccion text, 
        Telefono integer, 
        Correo text, 
        Ciudad text,
        Fecha_De_Nacimiento text,
        Fecha_De_Afiliacion text,
        Fecha_De_Desafiliacion text,
        Vacunado bool)''')
    #Creacion de la tabla Lotes
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS 
    Lotes(
        Codigo_De_Lote integer PRIMARY KEY,
        Fabricante text, 
        Tipo_De_Vacuna text, 
        Cantidad_Recibida integer, 
        Cantidad_Usada integer, 
        Dosis_Necesarias integer, 
        Temperatura_De_Almacenamiento integer,
        Efectividad_Identificada integer,
        Tiempo_De_Proteccion integer,
        Fecha_De_Vencimiento text,
        Imagen text)''')
    #Creacion de la tabla Planes
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS 
    Planes(
        ID integer PRIMARY KEY, 
        Edad_Min integer, 
        Edad_Max integer,
        Fecha_Inicio text,
        Fecha_Fin text)''')
    #Creacion de la tabla Citas
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS
    Citas(
        Numero_De_Cita integer PRIMARY KEY,
        Numero_De_Identificaion integer,
        Tipo_De_Identificacion text,
        Ciudad_De_Vacunacion text,
        Codigo_De_Lote integer,
        Fecha_De_Cita text,
        Hora_De_Cita integer)''')


#-----DESDE AQUI MODULO DE MENU-------------------------------------------------------------------------------------------------------
#Funcion Menu Principal Para Acceso A Funciones de Datos y Lotes
def menuPrincipal():
    #Diccionario de casos del menu principal
    casosPrincipal={1:"Datos",2:"Lotes",3:"Plan",4:"Salir"}
    #Mensaje de inicio 
    print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
    #Recepcion de la respuesta para el menu
    resp=int(input("1.Gestionar Datos\n2.Gestionar Lotes\n3.Plan\n4.Salir\n"))
    #Condicionales de uso del Menu Principal
    if casosPrincipal[resp]=="Datos":
        menuDatos()
    elif casosPrincipal[resp]=="Lotes":
        menuLotes()
    elif casosPrincipal[resp] == "Plan":
        menuPlanes()
    elif casosPrincipal[resp] == "Salir":
        con.close()
        exit()
    

#Funcion Menu para gestion de datos de los pacientes
def menuDatos():
    #Diccionario de casos del menu datos
    casosDatos={1:"Afiliar",2:"Consultar",3:"Desafiliar",4:"Vacunar",5:"Volver",6:"Salir"} #Diccionario de Casos
    #Mensajes de Inicio del Menu
    print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
    print("1.Afiliar un Paciente \n2.Consultar un Afiliado\n3.Desafiliar un Paciente\n4.Vacunar\n5.Volver\n6.Salir\n")
    #Recepcion de la respuesta del Usuario
    resp=int(input())
    #Condicionales de uso del Menu Para Gestion De Datos
    if casosDatos[resp] == "Afiliar":
        afiliarPaciente(con)
    elif casosDatos[resp] == "Consultar":
        consultarAfiliado(con)
    elif casosDatos[resp] == "Desafiliar":
        desafiliarPaciente(con)
    elif casosDatos[resp] == "Vacunar":
        vacunarAfiliado(con)
    elif casosDatos[resp]=="Volver":
        menuPrincipal()
    elif casosDatos[resp] == "Salir":
        con.close()
        exit()

#Funcion menu de gestion de lotes de vacunas
def menuLotes():
    #Diccionario de casos del menu Lotes
    casosLotes={1:"Crear",2:"Consultar", 3:"Regresar",4:"Salir"}
    #Mensajes de Inicio del Menu
    resp=int(input("1.Crear Lote\n2.Consultar Lote\n3.Regresar\n4.Salir\n"))
    #Condicionales de uso del Menu Para Gestion De Lotes
    if casosLotes[resp] == "Crear":
        crearLote(con)
    elif casosLotes[resp] == "Consultar":
        consultarLote(con)
    elif casosLotes[resp] == "Regresar":
        menuPrincipal()
    elif casosLotes[resp] == "Salir":
        con.close()
        exit()

#Funcion menu para gestion de planes de vacunacion
def menuPlanes():
    #Diccionario de casos del menu Planes
    casosPlan={1:"Crear",2:"Calcular",3:"Consultar", 4:"Regresar",5:"Salir"}
    #Mensajes de Inicio del Menu
    resp=int(input("1.Crear Plan\n2.Calcular Plan para los afiliados actuales\n3.Consultar Plan por ID\n4.Regresar\n5.Salir\n"))
    #Condicionales de uso del Menu Para Gestion De Lotes
    if casosPlan[resp] == "Crear":
        crearPlan(con)
    elif casosPlan[resp] == "Calcular":
        consultarPlan(con)
    elif casosPlan[resp] == "Consultar":
        consultarPlan(con)
    elif casosPlan[resp] == "Regresar":
        menuPrincipal()
    elif casosPlan[resp] == "Salir":
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
    IDPlan=None
    datosPaciente=(noIdentificacion,IDPlan,nombre,apellido,direccion,telefono,correo,ciudad,fechaNacimiento,fechaActual,None,False)
    #Insercion de los datos a la tabla de Afiliados, Nueva Fila
    cursorObj.execute("INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosPaciente)
    #Envio de la peticion a la base de datos
    con.commit()

#Función consultarAfiliado: Esta función permite al usuario consultar los datos de un paciente,
#Se debe ingresar el número de identificación del paciente para que la función busque en la tabla los datos
def consultarAfiliado(con):
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    noIdentificacion=int(input("Ingrese el número de identificación del paciente a consultar: "))
    #Seleccion de campos basado en la identificacion de pacientes basado en el Numero_de_identificacion
    cursorObj.execute('SELECT * FROM Afiliados WHERE Numero_de_identificacion = ? ',(noIdentificacion,))
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
    #Fecha Actual
    today = date.today()
    #Día actual
    dayActual=today.day
    #Mes actual
    monthActual=today.month
    #Año actual
    yearActual=today.year
    #Concatenación fecha actual
    fechaDesafiliacion=str(dayActual)+"/"+str(monthActual)+"/"+str(yearActual)
    #Insercion de la fecha concatenada en la base de datos basado en el Numero_de_identificacion, columna Fecha_de_desafiliacion
    cursorObj.execute('UPDATE Afiliados SET Fecha_De_Desafiliacion = ? WHERE Numero_de_identificacion = ?',(fechaDesafiliacion,noIdentificacion))
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
    cantidadUsada=input("Ingrese la cantidad a Usar: ")
    cantidadUsada=cantidadUsada.ljust(6)
    #Ingreso de cantidad dosis necesarias
    dosisNecesarias=input("Ingrese el número de dosis necesarias: ")
    dosisNecesarias=dosisNecesarias.ljust(1)
    #Ingreso de temperatura a la que debe ser almacenadas las vacunas
    temperatura=input("Ingrese la temperatura de almacenamiento: ")
    temperatura=temperatura.ljust(3)
    #Ingreso de la efectividad conocida de la vacuna
    efectividad=input("Ingrese el valor de efectivadad (0-100): ")
    efectividad=efectividad.rjust(2,"0")
    #Ingreso de tiempo de protección conocido de la vacuna
    tiempoProteccion=input("Ingrese el tiempo de proteccion de que ofrece la vacuna (Años): ")
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
    imagen="Aún no"
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
    lote=cursorObj.fetchall()
    #Impresion de la tupla correspondiente al lote
    for lote in lote:
        print(lote)
        
#-----DESDE AQUI MODULO DE PLANES DE VACUNACION-------------------------------------------------------------------------------------------------------

def crearPlan(con):
    cursorObj = con.cursor()
    idPlan=input("Ingrese el consecutivo del plan de vacunación:")
    idPlan=idPlan.ljust(2)
    #Ingreso de día de de inicio del plan de vacunación
    day=input("Ingrese el día de la fecha de inicio del plan de vacunación: ")
    day=day.rjust(2,"0")
    #Ingreso de mes de inicio del plan de vacunación
    month=input("Ingrese el mes de la fecha de inicio del plan de vacunación: ")
    month=month.rjust(2,"0")
    #Ingreso de año de inicio del plan de vacunación
    year=input("Ingrese el año de la fecha de inicio del plan de vacunación: ")
    year=year.rjust(4)
    #Concatenación de la fecha de inicio del plan de vacunación
    fechaInicio=day+"/"+month+"/"+year
    #Ingreso de día de de fin del plan de vacunación
    day=input("Ingrese el día de la fecha de fin del plan de vacunación: ")
    day=day.rjust(2,"0")
    #Ingreso de mes de fin del plan de vacunación
    month=input("Ingrese el mes de la fecha de fin del plan de vacunación: ")
    month=month.rjust(2,"0")
    #Ingreso de año de fin del plan de vacunación
    year=input("Ingrese el año de la fecha de fin del plan de vacunación: ")
    year=year.rjust(4)
    #Concatenación de la fecha de fin del plan de vacunación
    fechaFin=day+"/"+month+"/"+year 
    edadMin=input("Ingrese la edad mínima para clasificar a este plan: ")
    edadMin=edadMin.ljust(3)
    edadMax=input("Ingrese la edad máxima para clasificar a este plan: ")
    edadMax=edadMax.ljust(3)
    datosPlanes=(idPlan,edadMin,edadMax,fechaInicio,fechaFin)
    cursorObj.execute("INSERT INTO Planes VALUES(?,?,?,?,?)",datosPlanes)
    con.commit()
#Funcion de consulta de planes
def consultarPlan(con):
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    noId=int(input("Ingrese el ID del plan a consultar: "))
    #Seleccion de campos basado en el ID suministrado
    cursorObj.execute('SELECT * FROM Planes WHERE ID = ? ',(noId,))
    #Recoleccion de los datos en la tupla "consultados"
    planes=cursorObj.fetchall()
    #Impresion de la tupla correspondiente al paciente
    for planes in planes:
        print(planes)

def calcularPlan(con):
    confirmacion=input("""Este modulo asignará un numero de plan con respecto a los planes vigentes
    ¿Desea Ejecutar? Y/N
    """)
    confirmacion.upper()
    if confirmacion == "Y":
        cursorObj=con.cursor()
        #Seleccion de todos lo numeros de identificacion
        cursorObj.execute("SELECT Numero_de_identificacion FROM Afiliados")
        #Recopilacion en la tupla "identificaciones"
        identificaciones=cursorObj.fetchall()
        #Seleccion de Planes Existentes
        cursorObj.execute("SELECT ID FROM Planes")
        ids=cursorObj.fetchall()
        identificacionesActual=0
        idActual=0
        for identificacionesIterando in identificaciones :
            cursorObj.execute("SELECT fecha_de_Nacimiento FROM Afiliados WHERE Numero_de_identificacion =?",identificacionesIterando)
            nacimiento=cursorObj.fetchall()
            edad=list(nacimiento[0])
            edad=edad[0]
            edad=edad[6]+""+edad[7]+""+edad[8]+""+edad[9]
            today = date.today()
            edad=today.year-int(edad)
            identificacionActual=identificacionesIterando[0]
            for idIterando in ids:
                cursorObj.execute("SELECT Edad_Max,Edad_Min FROM Planes WHERE ID = ?",idIterando)
                restricciones=cursorObj.fetchall()
                restricciones=restricciones[0]
                idActual=ids[0]
                idActual=idActual[0]
                restricciones=[int(restricciones[0]),int(restricciones[1])]
                if restricciones[0] >= edad and restricciones[1] <= edad:
                    asignacion=(idActual,identificacionActual)
                    cursorObj.execute("UPDATE Afiliados SET ID_Plan = ? WHERE Numero_De_Identificacion = ?",asignacion)
                    con.commit()
                    break
    else:
        menuPlanes()

#-----DESDE AQUI MODULO DE PROGRAMA DE VACUNAS-------------------------------------------------------------------------------------------------------
def crearProgramacion(con):
    cursorObj=con.cursor()
    print("""Bienvenido al Creador de progamas de vacunación
    Una vez ingresados los datos requeridos acontinución, se le asignará una cita a todos los afiliados actuales.
    Teniendo en cuenta los planes de vacunacion existentes y asignados, asi como los parametros que ingresará acontinuacion
    Recuerde que debido a la situacion COVID actual, las citas se asignaran 30 minutos una despues de la otra""")
    print("Ingrese los datos de las fechas dentro de las que quiere asignar las citas")
    day=input("Día de Inicio de la asignacion de citas: ")
    day=day.rjust(2,"0")
    #Ingreso de mes de inicio de la asignacion de citas
    month=input("Mes de Inicio de la asignacion de citas: ")
    month=month.rjust(2,"0")
    #Ingreso de año de inicio de la asignacion de citas
    year=input("Año de Inicio de la asignacion de citas: ")
    year=year.rjust(4)
    #Concatenación de la fecha de inicio de la asignacion de citas
    fechaInicio= day + "/" + month + "/" + year
    #Ingreso de día de de fin de la asignacion de citas
    day=input("Día de Fin de la asignacion de citas: ")
    day=day.rjust(2,"0")
    #Ingreso de mes de fin de la asignacion de citas
    month=input("Mes de Fin de la asignacion de citas: ")
    month=month.rjust(2,"0")
    #Ingreso de año de fin de la asignacion de citas
    year=input("Año de Fin de la asignacion de citas: ")
    year=year.rjust(4)
    #Concatenación de la fecha de fin de la asignacion de citas
    fechaFin= day + "/" + month + "/" + year 
    fechaFin=input("Fecha de Fin")
    
    while True:
        print("Ingrese los datos de su horario de atencion deseado")
        horaInicio= input("Hora de Inicio del horario de atención (24 hrs)(00:00) : ")
        horaInicio=horaInicio.rjust(5,"0")
        horaInicio=horaInicio.split(":")
        try:
            horaInicio=[int(horaInicio[0]),int(horaInicio[1])]
            break

        except (ValueError):
            print("Poné un numero mongolico")
    if horaInicio[1] < 30:
        horaInicio[1] = 30
    elif horaInicio[1] > 30:
        horaInicio[1] = 00
        horaInicio[0] = int(horaInicio[0]) + 1


    while True:
        horaFin= input("Hora de Fin del horario de atención (24 hrs)(00:00) : ")
        horaFin=horaFin.rjust(5,"0")
        horaFin=horaFin.split(":")
        try:
            horaFin=[int(horaFin[0]),int(horaFin[1])]
            break
        except (ValueError):
            print("Poné un numero mongolico")
    if horaFin[1] < 30:
        horaFin[1] = 30
    elif horaFin[1] > 30:
        horaFin[1] = 00
        horaFin[0] = int(horaFin[0]) + 1
    horaCitas=[]
    horaIterando=horaInicio
    horaFin=[str(horaFin[0]),str(horaFin[1])]
    while horaIterando != horaFin:
        horaCitas.append(horaIterando)
        horaIterando=[int(horaIterando[0]),int(horaIterando[1])]
        horaIterando[1] += 30
        if horaIterando[1] >= 60:
            horaIterando[0] += 1
            horaIterando[1] = "00"
        horaIterando=[str(horaIterando[0]),str(horaIterando[1])]
    for horaCitas in horaCitas:
        print(str(horaCitas[0])+":"+str(horaCitas[1]))

#Conexion con la base de datos
con=sql_connection()

#Ejecucion de funciones
sql_table(con)

#menuPrincipal()
calcularPlan(con)

#Cerrar conexion
con.close()
"""
Acá dejamos los comandos sqlite3
Crear// Tabla cursorObj.execute("CREATE TABLE Nombre_De_Tabla(Campo1 Tipo_Dato Situacional(PRIMARY KEY), Campo2 Tipo_Dato, N_Campos Su_Tipo_Dato)")
Insert// cursorObj.execute("INSERT INTO Nombre_De_Tabla VALUES(Campo1, Campo2, N_Campos_Concordes_Al_#_Campos)")
Updates// cursorObj.execute('UPDATE Nombre_De_Tabla SET Campo_Modificar = Valor_Nuevo WHERE Campo_de_Identificacion = PRIMARY KEY')

Recordar que existen comandos que no funcionan correctamente sin un SELECT
Select// cursorObj.execute('SELECT Campo1, Campo2, N_campos FROM Nombre_de_tabla')
Para seleccionar todo usar * en ves de campos

Deletes// cursorObj.execute('DELETE FROM Nombre_De_Tabla').rowcount
.rowcount, devuelve el numero de filas borradas

!!!!!Drop!!!!!// DROP TABLE Nombre_De_Tabla

"""