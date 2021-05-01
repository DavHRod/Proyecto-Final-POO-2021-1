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
    #Creacion de la tabla Lotes
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
        ID_Plan integer,
        Numero_De_Identificacion integer,
        Ciudad_De_Vacunacion text,
        Codigo_De_Lote integer,
        Fecha_De_Cita text,
        Hora_De_Cita integer)''')


#-----DESDE AQUI MODULO DE MENU-------------------------------------------------------------------------------------------------------
#Funcion Menu Principal Para Acceso A Funciones de Datos y Lotes
def menuPrincipal():
    #Diccionario de casos del menu principal
    casosPrincipal={1:"Datos",2:"Lotes",3:"Plan",4:"Citas",5:"Salir"}
    #Mensaje de inicio 
    while True:
        print("\nBienvenido\nPorfavor escoja que tarea quiere realizar")
        #Recepcion de la respuesta del Usuario
        try:
            #Recepcion de la respuesta para el menu
            resp=int(input("1.Gestionar Datos\n2.Gestionar Lotes\n3.Gestionar Plan\n4.Gestionar Citas\n5.Salir\n"))
            break
        except:
            print("Debe ser un Numero")
    #Condicionales de uso del Menu Principal
    if resp > 0 and resp < 6:
        if casosPrincipal[resp]=="Datos":
            menuDatos()
        elif casosPrincipal[resp]=="Lotes":
            menuLotes()
        elif casosPrincipal[resp] == "Plan":
            menuPlanes()
        elif casosPrincipal[resp] == "Citas":
            menuCitas()
        elif casosPrincipal[resp] == "Salir":
            con.close()
            exit()
    else:
        print("Deber se una respuesta Valida")
        menuPrincipal()

#Funcion Menu para gestion de datos de los pacientes
def menuDatos():
    #Diccionario de casos del menu datos
    casosDatos={1:"Afiliar",2:"Consultar",3:"Desafiliar",4:"Vacunar",5:"Volver",6:"Salir"} #Diccionario de Casos
    #Mensajes de Inicio del Menu
    while True:
        print("Bienvenido\nPorfavor escoja que tarea quiere realizar")
        print("1.Afiliar un Paciente \n2.Consultar un Afiliado\n3.Desafiliar un Paciente\n4.Vacunar\n5.Volver\n6.Salir\n")
        #Recepcion de la respuesta del Usuario
        try:
            resp = int(input())
            break
        except:
            print("Debe ser un Numero")
    if resp > 0 and resp < 7:
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
    else:
        print("\nDebe se una opcion valida\n")
        menuDatos()

#Funcion menu de gestion de lotes de vacunas
def menuLotes():
    #Diccionario de casos del menu Lotes
    casosLotes={1:"Crear",2:"Consultar", 3:"Regresar",4:"Salir"}
    #Mensajes de Inicio del Menu
    while True:
        try:
            resp=int(input("1.Crear Lote\n2.Consultar Lote\n3.Regresar\n4.Salir\n"))
            break
        except:
            print("Debe ser un Numero")
    #Condicionales de uso del Menu Para Gestion De Lotes
    if resp > 0 and resp < 5:
        if casosLotes[resp] == "Crear":
            crearLote(con)
        elif casosLotes[resp] == "Consultar":
            consultarLote(con)
        elif casosLotes[resp] == "Regresar":
            menuPrincipal()
        elif casosLotes[resp] == "Salir":
            con.close()
            exit()
    else:
        print("Deber se una respuesta Valida")
        menuLotes()
#Funcion menu para gestion de planes de vacunacion
def menuPlanes():
    #Diccionario de casos del menu Planes
    casosPlan={1:"Crear",2:"Calcular",3:"Consultar", 4:"Regresar",5:"Salir"}
    #Mensajes de Inicio del Menu#Condicionales de uso del Menu Para Gestion De Lotes
    while True:
        try:           
            resp=int(input("1.Crear Plan\n2.Calcular Plan para los afiliados actuales\n3.Consultar Plan por ID\n4.Regresar\n5.Salir\n"))
            break
        except:
            print("Debe ser un Numero")
    #Condicionales de uso del Menu Para Gestion De Lotes
    if resp > 0 and resp < 6:
        if casosPlan[resp] == "Crear":
            crearPlan(con)
        elif casosPlan[resp] == "Calcular":
            calcularPlan(con)
        elif casosPlan[resp] == "Consultar":
            consultarPlan(con)
        elif casosPlan[resp] == "Regresar":
            menuPrincipal()
        elif casosPlan[resp] == "Salir":
            con.close()
            exit()
    else:
        print("Deber se una respuesta Valida")
        menuPlanes()
def menuCitas():
    #Diccionario de casos del menu Citas
    casosCitas={1:"Calcular Citas",2:"Consulta Individual",3:"Consulta General",4:"Regresar",5:"Salir"} 
    while True:
        try:           
            resp=int(input("1. Calcular Citas\n2. Consulta Individual\n3. Consulta General\n4. Regresar\n5.Salir\n")) 
            break
        except:
            print("Debe ser un Numero")
    #Condicionales de uso del Menu Para Gestion De Lotes
    if resp > 0 and resp < 6:
        if casosCitas[resp] == "Calcular Citas":
            calcularProgramacion(con)
        elif casosCitas[resp] == "Consulta Individual":
            consultarProgramaIndividual()
        elif casosCitas[resp] == "Consulta General":
            consultarProgramaGeneral()
        elif casosCitas[resp] == "Regresar":
            menuPrincipal()
        elif casosCitas[resp] == "Salir":
            con.close()
            exit()
    else:
        print("Deber se una respuesta Valida")
        menuCitas()
    
#-----DESDE AQUI MODULO DE AFILIADOS-------------------------------------------------------------------------------------------------------

#Función afiliarPaciente: Esta función recibe los datos de un nuevo paciente a afiliar y realiza la insercion en la tabla
def afiliarPaciente(con):
    cursorObj = con.cursor()
    #Ingreso de No. de identificación de un nuevo paciente
    while True:
        noIdentificacion=input("Ingrese el número de identificación del paciente: ")
        noIdentificacion=noIdentificacion.rjust(12," ")
        try:
            noIdentificacion = int(noIdentificacion)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
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
    while True:
        telefono=input("Ingrese un número de contacto: ")
        telefono=telefono.ljust(12)
        try:
            telefono = int(telefono)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de correo de un nuevo paciente
    correo=input("Ingrese el correo electrónico del paciente: ")
    correo=correo.ljust(20)
    #Ingreso de ciudad de origen de un nuevo paciente
    ciudad=input("Ingrese la ciudad en la que reside el paciente: ")
    ciudad=ciudad.ljust(20)
    #Ingreso de día de nacimiento de un nuevo paciente
    while True:
        day=input("Ingrese el día de nacimiento: ")
        day=day.rjust(2,"0")
        try:
            if int(day) < 32 and int(day) >0 :
                break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de mes de nacimiento de un nuevo paciente
    while True:
        month=input("Ingrese el mes de nacimiento: ")
        month=month.rjust(2,"0")
        try:
            if int(month) < 13 and int(month) >0 :
                break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    
    #Ingreso de año de nacimiento de un nuevo paciente
    while True:
        year=input("Ingrese el año de nacimiento: ")
        year=year.rjust(2,"0")
        try:
            year = int(year)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    
    #Concatenación de la fecha de nacimiento del nuevo paciente
    fechaNacimiento=str(day)+"/"+str(month)+"/"+str(year)
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
    salir=False
    while not salir:
        vacunado=input("¿Fue vacunado?: ")
        if (vacunado=='No' or vacunado=='no'):
            salir=True
    datosPaciente=(noIdentificacion,IDPlan,nombre,apellido,direccion,telefono,correo,ciudad,fechaNacimiento,fechaActual,None,vacunado)
    
    #Insercion de los datos a la tabla de Afiliados, Nueva Fila
    cursorObj.execute("INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosPaciente)
    #Envio de la peticion a la base de datos
    con.commit()
    menuDatos()

#Función consultarAfiliado: Esta función permite al usuario consultar los datos de un paciente,
#Se debe ingresar el número de identificación del paciente para que la función busque en la tabla los datos
def consultarAfiliado(con):
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    while True:
        noIdentificacion=input("Ingrese el número de identificación del paciente a consultar: ")
        try:
            noIdentificacion = int(noIdentificacion)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Seleccion de campos basado en la identificacion de pacientes basado en el Numero_de_identificacion
    cursorObj.execute('SELECT * FROM Afiliados WHERE Numero_de_identificacion = ? ',(noIdentificacion,))
    #Recoleccion de los datos en la tupla "consultados"
    consultados=cursorObj.fetchall()
    #Impresion de la tupla correspondiente al paciente
    for consultados in consultados:
        print(consultados)
    menuDatos()
#Función desafiliarPaciente: Con esta función se ingresa la fecha de desafiliación de un paciente    
def desafiliarPaciente(con):
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    while True:
        noIdentificacion=input("Ingrese el número de identificación del paciente a desafiliar: ")
        try:
            noIdentificacion = int(noIdentificacion)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
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
    menuDatos()
#Función vacunarAfiliado: Con esta función se actualiza el estado de vacunación de un afiliado en la tabla afiliado 
def vacunarAfiliado(con):
    cursorObj = con.cursor()
    #Ingreso de número de identificación del paciente a vacunar
    while True:
        noIdentificacion=input("Ingrese el número de identificación del paciente a Vacunar: ")
        try:
            noIdentificacion = int(noIdentificacion)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Actualización del estado de vacunación del afiliado basado en el Numero_de_identificacion, columna "Vacunado"
    cursorObj.execute('UPDATE Afiliados SET Vacunado="Si" WHERE Numero_de_identificacion=?',(noIdentificacion,))
    contadorVacunacion(noIdentificacion)
    #Envio de la peticion a la base de datos
    con.commit()
    menuDatos()

def contadorVacunacion(noIdentificacion):
    cursorObj = con.cursor()
    #Select que obtiene los datos de la tabla de Citas
    cursorObj.execute('SELECT Codigo_De_Lote FROM Citas WHERE Numero_De_Identificacion=?',(noIdentificacion,))
    codLote=cursorObj.fetchall()
    try:
        codLote=codLote[0]
        codLote1=codLote[0]
    except IndexError:
        print("No hay datos disponibles")
    #Select que obtiene los datos de la tabla de Lotes
    cursorObj.execute('SELECT Cantidad_Recibida, Cantidad_Usada FROM Lotes WHERE Codigo_De_Lote=?',(codLote1,))
    cantReUs=cursorObj.fetchall()
    cantReUs=cantReUs[0]
    cantReUs1=cantReUs[0]
    cantReUs2=cantReUs[1]
    if cantReUs1>0:
        usado=cantReUs2+1
        #Actualización de la cantiadad de vacunas usada basada en Cantidad_Usada
        cursorObj.execute('UPDATE Lotes SET Cantidad_Usada=? WHERE Codigo_De_Lote=?',(usado,codLote1))
    con.commit()
#-----DESDE AQUI MODULO DE LOTES-------------------------------------------------------------------------------------------------------

def crearLote(con):
    cursorObj = con.cursor()
    #Ingreso de No. de lote
    while True:
        try:
            noLote=int(input("Ingrese el número de lote: "))
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de nombre del fabricante del lote de vacunas
    fabricante=input("Ingrese el fabricante: ")
    fabricante=fabricante.ljust(12)
    #Ingreso de tipo de vacuna
    tipoVacuna=input("Ingrese el Tipo de Vacuna: ")
    tipoVacuna=tipoVacuna.ljust(20)
    #Ingreso de la cantidad de vacunas recibidas
    
    while True:
        cantidadRecibida=input("Ingrese la cantidad recibida: ")
        try:
            cantidadRecibida = int(cantidadRecibida)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Asignacion de la cantidad Asignada
    cantidadAsignada=0
    #Ingreso de la cantidad de vacunas usadas
    
    while True:
        cantidadUsada=input("Ingrese la cantidad Usada: ")
        try:
            cantidadUsada = int(cantidadUsada)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de cantidad dosis necesarias
    while True:
        dosisNecesarias=input("Ingrese el número de dosis necesarias: ")
        try:
            dosisNecesarias = int(dosisNecesarias)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de temperatura a la que debe ser almacenadas las vacunas
    temperatura=input("Ingrese la temperatura de almacenamiento: ")
    temperatura=temperatura.ljust(3)
    #Ingreso de la efectividad conocida de la vacuna
    while True:
        efectividad=input("Ingrese el valor de efectivadad (0-100): ")
        try:
            efectividad = int(efectividad)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de tiempo de protección conocido de la vacuna
    
    while True:
        tiempoProteccion=input("Ingrese el tiempo de proteccion de que ofrece la vacuna (Años): ")
        try:
            tiempoProteccion = int(tiempoProteccion)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de día de vencimiento de la vacuna
    while True:
        day=input("Ingrese el día de vencimiento de la vacuna: ")
        day=day.rjust(2,"0")
        try:
            if int(day) >0 and int(day) < 32:
                break
            else:
                print("El Numero debe estar entre 1 y 31")
        except:
            print("La entrada debe ser Digito")
    #Ingreso de mes de vencimiento de la vacuna
    while True:
        month=input("Ingrese el mes de vencimiento de la vacuna: ")
        month=month.rjust(2,"0")
        try:
            if int(month) >0 and int(month) < 13:
                break
            else:
                print("El Numero debe estar entre 1 y 12")
        except:
            print("El Numero debe ser Digito")
    #Ingreso de año de vencimiento de la vacuna
    while True:
        year=input("Ingrese el año de vencimiento de la vacuna:")
        year=year.rjust(4)
        try:
            if int(year) >= 2021:
                break
            else:
                print("El Número debe estar entre 1 y 12")
        except:
            print("El Número debe ser Digito")

    #Concatenación de la fecha de vencimiento de la vacuna 
    fechaVencimiento=day+"/"+month+"/"+year
    #Imagen: proximamente
    imagen="Aún no"
    datosLotes=(noLote,fabricante,tipoVacuna,cantidadRecibida,cantidadUsada,cantidadAsignada,dosisNecesarias,temperatura,efectividad,tiempoProteccion,fechaVencimiento,imagen)
    #Insercion de los datos a la tabla de Lotes, Nueva Fila
    cursorObj.execute("INSERT INTO Lotes VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosLotes)
    #Envio de la peticion a la base de datos
    con.commit()
    menuLotes()
#Función contadorVacunacion(noIdentificacion)


def consultarLote(con):
    cursorObj = con.cursor()
    #Recepcion del Numero del lote a consultar
    while True:
        noLote=(input("Ingrese el número de lote a consultar: "))
        try:
            noLote = int(noLote)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")    
    #Seleccion de datos basado en el Numero_De_Lote
    cursorObj.execute('SELECT * FROM Lotes WHERE Codigo_De_Lote=?',(noLote,))
    #Recoleccion de los datos en la tupla "consultados"
    lote=cursorObj.fetchall()
    #Impresion de la tupla correspondiente al lote
    for lote in lote:
        print(lote)
    menuLotes()
#-----DESDE AQUI MODULO DE PLANES DE VACUNACION-------------------------------------------------------------------------------------------------------

def crearPlan(con):
    cursorObj = con.cursor()
    #Ingreso de un id para asignarlo a un plan
    idPlan=input("Ingrese el consecutivo del plan de vacunación:")
    idPlan=idPlan.ljust(2)
    #Ingreso el día de de inicio del plan de vacunación
    while True:
        day=input("Ingrese el día de la fecha de inicio del plan de vacunación: ")
        day=day.rjust(2,"0")
        try:
            if int(day) >0 and int(day) < 32:
                break
            else:
                #Mensaje en pantalla de un error al digitar
                print("El Numero debe estar entre 1 y 31")
        except:
            #Mensaje en pantalla de un error al digitar
            print("La entrada debe ser Digito")
    #Ingreso de mes de inicio del plan de vacunación
    while True:
        month=input("Ingrese el mes de la fecha de inicio del plan de vacunación: ")
        month=month.rjust(2,"0")
        try:
            if int(month) >0 and int(month) < 13:
                break
            else:
                #Mensaje en pantalla de un error al digitar
                print("El Numero debe estar entre 1 y 12")
        except:
            #Mensaje en pantalla de un error al digitar
            print("El Numero debe ser Digito")
    #Ingreso de año de inicio del plan de vacunación
    while True:
        year=input("Ingrese el año de la fecha de inicio del plan de vacunación: ")
        year=year.rjust(4)
        try:
            if int(year) > 1950:
                break
            else:
                #Mensaje en pantalla de un error al digitar
                print("El Número debe estar entre 1 y 12")
        except:
            #Mensaje en pantalla de un error al digitar
            print("El Número debe ser Digito")
    #Concatenación de la fecha de inicio del plan de vacunación
    fechaInicio=day+"/"+month+"/"+year
    #Concatenación de la fecha de fin del plan de vacunación
    fechaFin = "24/05/2121"
    while True:
        try:
            edadMin=int(input("Ingrese la edad mínima para clasificar a este plan: "))
            break
        except:
            #Mensaje en pantalla de un error al digitar
            print("El Número debe ser Digito")
    
    while True:
        try:
            edadMax=int(input("Ingrese la edad máxima para clasificar a este plan: "))
            break
        except:
            #Mensaje en pantalla de un error al digitar
            print("El Número debe ser Digito")
    datosPlanes=(idPlan,edadMin,edadMax,fechaInicio,fechaFin)
    cursorObj.execute("INSERT INTO Planes VALUES(?,?,?,?,?)",datosPlanes)
    con.commit()
    menuPlanes()
#Funcion de consulta de planes
def consultarPlan(con):
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    while True:
        try:
            noId=int(input("Ingrese el ID del plan a consultar: "))
            break
        except:
            #Mensaje en pantalla de un error al digitar
            print("El Número debe ser Digito")
    #Seleccion de campos basado en el ID suministrado
    cursorObj.execute('SELECT * FROM Planes WHERE ID = ? ',(noId,))
    #Recoleccion de los datos en la tupla "consultados"
    planes=cursorObj.fetchall()
    #Impresion de la tupla correspondiente al paciente
    for planes in planes:
        print(planes)
    menuPlanes()
def calcularPlan(con):
    confirmacion=input("""Este modulo asignará un numero de plan con respecto a los planes vigentes
    ¿Desea Ejecutar? Y/N\n""")
    confirmacion=confirmacion.upper()
    if confirmacion == "Y":
        cursorObj = con.cursor()
        #Seleccion de todos lo numeros de identificacion
        cursorObj.execute("SELECT Numero_de_identificacion FROM Afiliados")
        #Recopilacion en la tupla "identificaciones"
        identificaciones=cursorObj.fetchall()
        #Seleccion de Planes Existentes
        cursorObj.execute("SELECT ID FROM Planes")
        ids = cursorObj.fetchall()
        identificacionActual = 0
        idActual = 0
        for identificacionesIterando in identificaciones :
            cursorObj.execute("SELECT fecha_de_Nacimiento FROM Afiliados WHERE Numero_de_identificacion =?",identificacionesIterando)
            nacimiento = cursorObj.fetchall()
            edad = list(nacimiento[0])
            edad = datetime.strptime(edad[0], "%d/%m/%Y")
            today = datetime.today()
            today = today.year
            edad = today-edad.year
            identificacionActual=identificacionesIterando[0]
            for idIterando in ids:
                cursorObj.execute("SELECT Edad_Max,Edad_Min FROM Planes WHERE ID = ?",idIterando)
                restricciones = cursorObj.fetchall()
                restricciones = restricciones[0]
                restricciones = [int(restricciones[0]),int(restricciones[1])]
                if restricciones[0] >= edad and restricciones[1] <= edad:
                    asignacion=(idIterando[0],identificacionActual)
                    cursorObj.execute("UPDATE Afiliados SET ID_Plan = ? WHERE Numero_De_Identificacion = ?",asignacion)
                    con.commit()
                    break
    else:
        menuPlanes()

#-----DESDE AQUI MODULO DE PROGRAMA DE VACUNAS-------------------------------------------------------------------------------------------------------
def calcularProgramacion(con):
    cursorObj=con.cursor()
    print("""Bienvenido al Creador de progamas de vacunación
    Una vez ingresados los datos requeridos acontinución, se le asignará una cita a todos los afiliados actuales.
    Teniendo en cuenta los planes de vacunacion existentes y asignados, asi como los parametros que ingresará acontinuacion
    Recuerde que debido a la situacion COVID actual, las citas se asignaran 30 minutos una despues de la otra""")
    print("Ingrese los datos de las fechas dentro de las que quiere asignar las citas")
    while True:
        day=input("Dia de Inicio de la asignacion de citas: ")
        day=day.rjust(2,"0")
        try:
            if int(day) < 32 and int(day) >0 :
                break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de mes de inicio de la asignacion de citas
    while True:
        month=input("Mes de Inicio de la asignacion de citas: ")
        month=month.rjust(2,"0")
        try:
            if int(month) < 13 and int(month) >0 :
                break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Ingreso de año de inicio de la asignacion de citas
    while True:
        year=input("Año de Inicio de la asignacion de citas: ")
        year=year.ljust(4,"0")
        try:
            if int(year) > 1000:
                break
            else:
                print("Debe ser mayor a 1000")
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Concatenación de la fecha de inicio de la asignacion de citas
    fechaInicio= day + "/" + month + "/" + year
    #Ingreso de día de de fin de la asignacion de citas
    year = "2121"
    fechaFin = day + "/" + month + "/" + year

    while True:
        print("Ingrese los datos de su horario de atencion deseado")
        horaInicio= input("Hora de Inicio del horario de atención (24 hrs)(00:00) : ")
        horaInicio=horaInicio.rjust(5,"0")
        horaInicio=horaInicio.split(":")
        try:
            horaInicio=[int(horaInicio[0]),int(horaInicio[1])]
            break

        except (ValueError):
            #Mensaje en pantalla de un error al digitar
            print("Debe ser formato 00:00")
    if horaInicio[1] < 30:
        horaInicio[1] = 30
    elif horaInicio[1] > 30:
        horaInicio[1] = 00
        horaInicio[0] = int(horaInicio[0]) + 1

    while True:
        horaFin=input("Hora de Fin del horario de atención (24 hrs)(00:00) : ")
        horaFin=horaFin.rjust(5,"0")
        horaFin=horaFin.split(":")
        try:
            horaFin=[int(horaFin[0]),int(horaFin[1])]
            break
        except (ValueError):
            #Mensaje en pantalla de un error al digitar
            print("Debe ser formato 00:00")
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
    
    #Seleccion de los datos de los pacientes
    cursorObj.execute("SELECT Numero_De_Identificacion, Ciudad_De_Residencia FROM Afiliados")
    #Recopilacion en la tupla "afiliados"
    afiliados=cursorObj.fetchall()
    #Seleccion de los Planes vigentes
    cursorObj.execute("SELECT ID FROM Planes")
    #Recopilacion en la tupla "Planes"
    planes=cursorObj.fetchall()
    secuencial = 1
    loteActual = 0
    for plan in range(1,len(planes)+1):
        cursorObj.execute("SELECT Numero_De_Identificacion, Ciudad_De_Residencia, ID_Plan FROM Afiliados WHERE ID_Plan = ?",(plan,))
        #Recopilacion en la tupla "afiliados"
        afiliados=cursorObj.fetchall()
        #Fecha Inicio Plan
        cursorObj.execute("SELECT Fecha_Inicio FROM Planes WHERE ID = ? ",(plan,))
        fechaPlan=cursorObj.fetchall()
        fechaPlan = fechaPlan[0]
        fechaPlan = fechaPlan[0]
        #Codigo de Lote
        afiliado = 0
        while afiliado != len(afiliados):
            #Select que obtinene los datos de la tabla Lotes
            cursorObj.execute("SELECT Codigo_De_Lote, Cantidad_Recibida, Cantidad_Asignada, Cantidad_Usada FROM Lotes")
            vacunas=cursorObj.fetchall()
            vacunas=vacunas[loteActual]
            lote=int(vacunas[0])
            recibidas=int(vacunas[1])
            asignadas=int(vacunas[2])
            usadas=int(vacunas[3])
            existentes = recibidas - usadas
            horaCitaActual=horaCitas[afiliado]
            horaCitaActual=str(horaCitaActual[0])+":"+str(horaCitaActual[1])
            afiliadoActual=afiliados[afiliado]
            if asignadas != existentes:
                cursorObj.execute("UPDATE Lotes SET Cantidad_Asignada = ? WHERE Codigo_De_Lote = ?",(asignadas + 1,lote))
                con.commit()
            else:
                loteActual += 1
            nuevaCita=(secuencial,afiliadoActual[2],afiliadoActual[0],afiliadoActual[1],lote,fechaPlan,horaCitaActual)
            cursorObj.execute("INSERT INTO Citas Values (?,?,?,?,?,?,?)",nuevaCita)
            con.commit()
            secuencial += 1
            afiliado += 1
    menuCitas()
#Función consultarProgramaIndividual(): Esta función permite al usuario visualizar los datos de la cita
#a partir de un número de identificación
def consultarProgramaIndividual():
    cursorObj = con.cursor()
    #Recepcion del numero de identificacion
    while True:
        noIdentificacion=input("Ingrese el número de identificación del paciente: ")
        noIdentificacion=noIdentificacion.rjust(12," ")
        try:
            noIdentificacion = int(noIdentificacion)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Select que obtiene los datos asociados al número de identificación ingresado de la tabla citas 
    cursorObj.execute('SELECT * FROM Citas WHERE Numero_De_Identificacion=?',(noIdentificacion,))
    citas=cursorObj.fetchall()#citas guarda la tupla con los datos obtenidos
    citas=citas[0] #Guarda la tupla con los datos del número de identificación 
    noId=citas[0] #Guarda el consecutivo de cita
    idPlan=citas[1] #Guarda el número de plan correspondiente
    idAfiliado=citas[2] #Guarda el número de identificación del afiliado 
    ciudad=citas[3] #Guarda el dato de la ciudad donde fue o será vacunado el afiliado
    codLote=citas[4] #Guarda el código de lote de la vacuna con que fue o será vacunado el afiliado
    fechaCita=citas[5] #Guarda la fecha de la cita de vacunación
    horaCita=citas[6] #Guarda la hora de la cita de vacunación
    print(
        "Número de cita: ", noId,"\n" #Imprime el consecutivo de cita
        "Número de plan: ", idPlan, "\n" #Imprime el número de plan correspondiente
        "Identificación Afiliado: ", idAfiliado,"\n" #Imprime el número de identificación del afiliado
        "Ciudad de Vacunación: ", ciudad,"\n" #Imprime la ciudad donde fue o será vacunado el afiliado
        "Código de lote: ", codLote,"\n" #Imprime el código de lote de la vacuna con que fue o será vacunado el afiliado
        "Fecha y hora de cita: ", fechaCita, "a las ", horaCita,"\n" #Imprime la fecha y hora de la cita de vacunación
    )
    menuCitas()
#Función consultarProgramaGeneral(): Esta función permite al usuario visualizar todos los datos de la tabla citas
def consultarProgramaGeneral():
    cursorObj = con.cursor()
    #Select que obtiene los datos de la tabla de citas
    cursorObj.execute('SELECT * FROM Citas')
    citas=cursorObj.fetchall() #citas guarda la tupla con los datos obtenidos
    #Encabezado de la tabla que imprime los datos de las citas agendadas
    print("\n| No. Cita | IdPlan | Identificación | Ciudad               | Lote Asignado | Fecha De La Cita | Hora De La Cita |")
    print("------------------------------------------------------------------------------------------------------------------")
    #Tabla que imprime los datos de las citas agendadas
    for citas in citas:
        cita= "| {:<8} | {:<6} | {:<14} | {:<5} | {:<13} | {:<16} | {:<15} |".format(citas[0],citas[1],citas[2],citas[3],citas[4],citas[5],citas[6])
        print(cita)
    menuCitas()

#Conexion con la base de datos
con=sql_connection()

#Ejecucion de funciones
sql_table(con)

menuPrincipal()
#calcularPlan(con)
#crearProgramacion(con)
#crearPlan(con)

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