#Importación de librerias a usar
#sqlite3: Es una libreria integrada en python para el manejo de bases de datos generalmente de tipo local
#utiliza comandos sql estandar y requiere el uso de un objeto tipo sql_connect
import sqlite3
from sqlite3 import Error
#Validate_email: Es la libreria que permite realizar la validación de un correo electrónico, su dominio y su existencia en el dominio señalado.
#Requiere instalación de py3DNS mediante el comando pip install py3DNS, esto con permisos de administrador activos
from validate_email import validate_email
#datetime: Libreria integrada en python 3, permite el manejo y operación de variables tipo datetime,
#es usada para comprobacion y validacion de fechas bajo parametros propios
from datetime import date
from datetime import datetime

#Función de iniciación de la base de datos
def sql_connection():
    try:
        #Conexión con la base de datos
        con = sqlite3.connect('ProgramaDeVacunacion.db')
        return con
    except Error:
        print(Error)

#Función de creación primary keys
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


#-----DESDE AQUI MODULO DE MENU-------------------------------------------------------------------------------------------------------
#Función Menu Principal Para Acceso A Funciones de Datos y Lotes
def menuPrincipal():
    #Diccionario de casos del menu principal
    casosPrincipal={1:"Datos",2:"Lotes",3:"Plan",4:"Citas",5:"Salir"}
    #Bucle de comprobación
    while True:
        print("\nPorfavor escoja que tarea quiere realizar")
        #Comprobación del tipo de dato
        try:
            #Recepcion de la respuesta para el menu
            resp=int(input("1.Gestionar Datos\n2.Gestionar Lotes\n3.Gestionar Plan\n4.Gestionar Citas\n5.Salir\n"))
            #Ruptura del bucle de comprobación
            break
        except:
            #Mensaje de Error
            print("Debe ser un Numero")
    #Condicionales de uso del Menu Principal: verifica que la entrada se encuentre entre las opciones ofrecidas por el menú
    if resp > 0 and resp < 6:
        #Llamado de las funciones según opción elegida 
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
        #Mensaje de Error
        print("Deber se una respuesta Valida")
        menuPrincipal()

#Funcion Menu para gestion de datos de los pacientes
def menuDatos():
    #Diccionario de casos del menu datos
    casosDatos={1:"Afiliar",2:"Consultar",3:"Desafiliar",4:"Vacunar",5:"Volver",6:"Salir"} #Diccionario de Casos
    #Mensajes de Inicio del Menu
    while True:
        #Comprobacion del tipo de dato
        try:
            #Recepción de la respuesta del usuario
            resp = int(input("\nPorfavor escoja que tarea quiere realizar\n1.Afiliar un Paciente \n2.Consultar un Afiliado\n3.Desafiliar un Paciente\n4.Vacunar\n5.Volver\n6.Salir\n"))
            #Ruptura del bucle de comprobación
            break
        except:
            #Mensaje de Error
            print("Debe ser un Numero")
    #Condicionales de uso del Menu de Gestión de Datos: verifica que la entrada se encuentre entre las opciones ofrecidas por el menú
    if resp > 0 and resp < 7:
        #Condicionales de uso del Menu Para Gestion De Datos: Llamado de las funciones según opción elegida 
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
        #Mensaje de Error
        print("\nDebe ser una opcion valida")
        menuDatos()

#Funcion menu de gestion de lotes de vacunas
def menuLotes():
    #Diccionario de casos del menu Lotes
    casosLotes={1:"Crear",2:"Consultar", 3:"Regresar",4:"Salir"}
    #Bucle de comprobación de entrada
    while True:
        #Comprobación para el tipo de dato
        try:
            #Recepción de la respuesta
            resp=int(input("\nPorfavor escoja que tarea quiere realizar\n1.Crear Lote\n2.Consultar Lote\n3.Regresar\n4.Salir\n"))
            #Ruptura del bucle de comprobación
            break
        except:
            #Mensaje de Error
            print("Debe ser un Numero")
    #Condicional para mantener la respuesta dentro del rango del menú
    if resp > 0 and resp < 5:
        #Condicionales de uso del Menu Para Gestion De Lotes: Llamado de las funciones según opción elegida 
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
        #Mensaje de error en caso de no estar en el intervalo
        print("Deber se una respuesta Valida")
        menuLotes()
#Funcion menu para gestion de planes de vacunacion
def menuPlanes():
    #Diccionario de casos del menu Planes
    casosPlan={1:"Crear",2:"Consultar", 3:"Cerrar Plan", 4:"Regresar",5:"Salir"}
    #Bucle de comprobación de entrada
    while True:
        #Comprobación para el tipo de dato
        try:
            #Recepción de la respuesta
            resp=int(input("\nPorfavor escoja que tarea quiere realizar\n1.Crear Plan\n2.Consultar Plan por ID\n3.Cerrar Plan\n4.Regresar\n5.Salir\n"))
            #Ruptura del bucle de comprobación
            break
        except:
            #Mensaje de Error
            print("Debe ser un Numero")
    #Condicional para mantener la respuesta dentro del rango del menú
    if resp > 0 and resp < 7:
        #Condicionales de uso del Menu Para Gestion De Planes: Llamado de las funciones según opción elegida 
        if casosPlan[resp] == "Crear":
            crearPlan(con)
        elif casosPlan[resp] == "Consultar":
            consultarPlan(con)
        elif casosPlan[resp] == "Cerrar Plan":
            cierrePlanVacunacion(con)
        elif casosPlan[resp] == "Regresar":
            menuPrincipal()
        elif casosPlan[resp] == "Salir":
            con.close()
            exit()
    else:
        #Mensaje de error en caso de no estar en el intervalo
        print("Deber se una respuesta Valida")
        menuPlanes()
#Funcion menu para gestion de citas de vacunacion
def menuCitas():
    #Diccionario de casos del menu Citas
    casosCitas={1:"Calcular Citas",2:"Consulta Individual",3:"Consulta General",4:"Regresar",5:"Salir"} 
    #Bucle de comprobacion de entrada
    while True:
        #Comprobación para el tipo de dato
        try:
            #Recepción de la respuesta
            resp=int(input("\nPorfavor escoja que tarea quiere realizar\n1.Calcular Citas\n2.Consulta Individual\n3.Consulta General\n4.Regresar\n5.Salir\n")) 
            #Ruptura del bucle de comprobación
            break
        except:
            #Mensaje de Error
            print("Debe ser un Numero")
    #Condicional para mantener la respuesta dentro del rango del menú
    if resp > 0 and resp < 6:
        #Condicionales de uso del Menu Para Gestion De Citas: Llamado de las funciones según opción elegida 
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
        #Mensaje de error en caso de no estar en el intervalo
        print("Deber se una respuesta Valida")
        menuCitas()
    
#-----DESDE AQUI MODULO DE AFILIADOS-------------------------------------------------------------------------------------------------------

#Función afiliarPaciente: Esta función recibe los datos de un nuevo paciente a afiliar y realiza la inserción en la tabla
def afiliarPaciente(con):
    cursorObj = con.cursor()
    #Bucle de comprobacion de entrada
    while True:
        #Recepción del número de identificación
        noIdentificacion=input("Ingrese el número de identificación del paciente: ")
        #Variable con la longitud máxima
        longitudId=12
        #Variable con la longitud del string
        longId=len(noIdentificacion)
        #Condicional para comprobar la longuitud de la respuesta
        if longId<=longitudId:
            noIdentificacion=noIdentificacion.rjust(longitudId," ")
            #Comprobación para el tipo de dato
            try:
                noIdentificacion = int(noIdentificacion)
                #Ruptura del bucle de comprobación
                break
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        else:
            #Mensaje de Error por longuitud del dato
            print("Máximo escriba 12 digitos")
        
    #Ingreso de nombre de un nuevo paciente
    nombre=input("Ingrese el nombre del paciente: ")
    nombre=nombre.ljust(20)
    #Limitación del tamaño del string
    nombre=nombre[:20]
    #Ingreso de apellido de un nuevo paciente
    apellido=input("Ingrese el apellido del paciente: ")
    apellido=apellido.ljust(20)
    #Limitación del tamaño del string
    apellido=apellido[:20]
    #Ingreso de dirección de residencia de un nuevo paciente
    direccion=input("Ingrese la dirección de residencia del paciente: ")
    direccion=direccion.ljust(30)
    #Limitación del tamaño del string
    direccion=direccion[:30]
    #Ingreso de telefono de un nuevo paciente
    #Bucle de comprobación de entrada
    while True:
        #Recepción del número de telefono
        telefono=input("Ingrese un número de contacto: ")
        #Variable con la longitud máxima
        longitud=10
        #Variable con la longitud del string
        longVariable=len(telefono)
        #Condicional para comprobar la longuitud de la respuesta
        if longVariable<=longitud:
            #Comprobación para el tipo de dato
            try:
                telefono = int(telefono)
                #Ruptura del bucle de comprobación
                break
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
            telefono=telefono.ljust(10)
        else:
            #Mensaje de Error por longuitud del dato
            print("Máximo escriba 10 digitos")

    #Ingreso de correo de un nuevo paciente
    #Bucle de comprobación de entrada, de existencia real de correo ingresado
    while True:
        #Recepción del correo
        correo=input("Ingrese el correo electrónico del paciente: ")
        #Uso del metodo validate_email y recepción del retorno en la variable es_valido
        es_valido = validate_email(correo, verify=True)
        #Comprobación del retorno del metodo
        if es_valido==False:
            #Mensaje de Error
            print("No valido, ingrese un correo valido")
        else: 
            #Ruptura del bucle de comprobación
            break
    #Ingreso de ciudad de origen de un nuevo paciente
    ciudad=input("Ingrese la ciudad en la que reside el paciente: ")
    ciudad=ciudad.ljust(20)
    #Limitación del tamaño del string
    ciudad=ciudad[:20]
    #Bucle de comprobacion de entrada para fecha
    while True:
        #Bucle de comprobacion de entrada
        while True:
            #Ingreso de día de nacimiento de un nuevo paciente
            day=input("Ingrese el día de nacimiento: ")
            day=day.rjust(2,"0")
            #Comprobación para el tipo de dato
            try:
                #Condicional para comprobación de rango de la entrada
                if int(day) < 32 and int(day) >0 :
                    #Ruptura del bucle de comprobación
                    break
                else:
                    print("Dia invalido")
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        #Bucle de comprobacion de entrada
        while True:
            #Ingreso de mes de nacimiento de un nuevo paciente
            month=input("Ingrese el mes de nacimiento: ")
            month=month.rjust(2,"0")
            #Comprobación para el tipo de dato
            try:
                #Condicional para comprobación de rango de la entrada
                if int(month) < 13 and int(month) >0 :
                    #Ruptura del bucle de comprobación
                    break
                else:
                    print("Mes invalido")
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        
        #Bucle de comprobacion de entrada
        while True:
            #Ingreso de año de nacimiento de un nuevo paciente
            year=input("Ingrese el año de nacimiento: ")
            year=year.rjust(4,"0")
            #Comprobación para el tipo de dato
            try:
                year = int(year)
                if int(year) < datetime.today().year :
                    #Ruptura del bucle de comprobación
                    break
                else:
                    print("Año invalido")
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        #Concatenación de la fecha de nacimiento del nuevo paciente
        fechaNacimiento=str(day)+"/"+str(month)+"/"+str(year)
        #Obtención de la fecha actual
        fechaActual=datetime.today()
        #Uso de una variable auxiliar para comprobar la existencia de la fecha
        try:
            #Uso de una variable auxiliar para comprobar la existencia de la fecha
            fechaNacimientoComprobacion=datetime.strptime(fechaNacimiento, "%d/%m/%Y")
            #Comprobación de integridad de la fecha
            if fechaNacimientoComprobacion > fechaActual:
                print("Fecha Invalida")
               
            else:
                #Ruptura del bucle de comprobación
                break
        except:
            #Mensaje de Error
            print("Fecha Inexistente")

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
    datosPaciente=(noIdentificacion,"-",nombre,apellido,direccion,telefono,correo,ciudad,fechaNacimiento,fechaActual,"-","No")
    try:
        #Insercion de los datos a la tabla de Afiliados, Nueva Fila
        cursorObj.execute("INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosPaciente)
        con.commit()
        calcularPlan(con)
    except:
        print ("El Afiliado ya existe")
    #Envio de la petición a la base de datos
    
    menuDatos()

#Función consultarAfiliado: Esta función permite al usuario consultar los datos de un paciente,
#Se debe ingresar el número de identificación del paciente para que la función busque en la tabla los datos
def consultarAfiliado(con):
    cursorObj = con.cursor()
    #Bucle de comprobación
    while True:
        #Recepcion del número de identificación a consultar
        noIdentificacion=input("Ingrese el número de identificación del paciente a consultar: ")
        #Comprobación del tipo de dato
        try:
            noIdentificacion = int(noIdentificacion)
            #Ruptura del bucle de comprobación
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Selección de campos basado en la identificación de pacientes basado en el Numero_de_identificacion
    cursorObj.execute('SELECT * FROM Afiliados WHERE Numero_de_identificacion = ? ',(noIdentificacion,))
    consultados="Vacio"
    #Recolección de los datos en la tupla "consultados"
    consultados=cursorObj.fetchall()
    if len(consultados) <= 0:
        print("El Paciente No Existe")
    else:
        consultados1=consultados[0]
        #Impresión de la tupla correspondiente a la información paciente en forma de tabla
        print("------------------------------------------------------------")
        print("| No. Identificación     || {:<30} |\n| IdPlan                 || {:<30} |\n| Nombre                 || {:<30} |\n| Apellido               || {:<30} |\n| Dirección              || {:<1} |\n| Telefono               || {:<30} |\n| Correo                 || {:<30} |\n| Ciudad de Residencia   || {:<30} |\n| Fecha de Nacimiento    || {:<30} |\n| Fecha de Afiliación    || {:<30} |\n| Fecha de desafiliación || {:<30} |\n| Vacunado SI/NO         || {:<30} |".format(consultados1[0],consultados1[1],consultados1[2],consultados1[3],consultados1[4],consultados1[5],consultados1[6],consultados1[7],consultados1[8],consultados1[9],consultados1[10],consultados1[11]))
        print("------------------------------------------------------------")
    
    menuDatos()

#Función desafiliarPaciente: Con esta función se ingresa la fecha de desafiliación de un paciente    
def desafiliarPaciente(con):
    cursorObj = con.cursor()
    #Bucle de comprobación
    while True:
        #Recepción del número de identificación
        noIdentificacion=input("Ingrese el número de identificación del paciente a desafiliar: ")
        #Comprobación del tipo de dato
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
    #Inserción de la fecha concatenada en la base de datos basado en el Numero_de_identificacion, columna Fecha_de_desafiliacion
    cursorObj.execute('UPDATE Afiliados SET Fecha_De_Desafiliacion = ? WHERE Numero_de_identificacion = ?',(fechaDesafiliacion,noIdentificacion))
    #Envio de la petición a la base de datos
    con.commit()
    #Llamado del menú de gestión de datos
    menuDatos()

#Función vacunarAfiliado: Con esta función se actualiza el estado de vacunación de un afiliado en la tabla afiliado 
def vacunarAfiliado(con):    
    cursorObj = con.cursor()    
    #Bucle de comprobación
    while True:
        #Ingreso de número de identificación del paciente a vacunar
        noIdentificacion=input("Ingrese el número de identificación del paciente a Vacunar: ")
        #Comprobación del tipo de dato
        try:
            noIdentificacion = int(noIdentificacion)
            #Ruptura del bucle de comprobación
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Selección de la fecha de desafiliacion del paciente a vacunar
    cursorObj.execute('SELECT Fecha_De_Desafiliacion FROM Afiliados WHERE Numero_De_Identificacion = ? AND Vacunado = "No"',(noIdentificacion,))
    #Recopilación en el array "desafiliado"
    desafiliado=cursorObj.fetchall()
    if len(desafiliado) <= 0:
        print("El paciente no existe o ya está vacunado")
    else:
        #Acceso a la tupla del afiliado
        desafiliado1=desafiliado[0]
        #Acceso al dato
        desafiliado2=desafiliado1[0]
        #Condicional de comprobacíon de desafiliación
        if desafiliado2 != "-":
            #Mensaje de Advertencia
            print("El paciente está desafiliado y no será vacunado\n")
            menuDatos()
        else:
            #Actualización del estado de vacunación del afiliado basado en el Numero_de_identificacion, columna "Vacunado"
            if contadorVacunacion(noIdentificacion):
                cursorObj.execute(f'UPDATE Afiliados SET Vacunado="Si" WHERE Numero_de_identificacion = {noIdentificacion}')
            #Envio de la petición a la base de datos
            con.commit()
    menuDatos()

#Función contadorVacunacion(noIdentificacion): Esta función actualiza la cantidad de vacunas utilizadas en la tabla Lotes
def contadorVacunacion(noIdentificacion):
    cursorObj = con.cursor()
    codLote="vacio"
    #Select que obtiene los datos de la tabla de Citas
    cursorObj.execute(f'SELECT Codigo_De_Lote FROM Citas WHERE Numero_De_Identificacion= {noIdentificacion}')
    codLote=cursorObj.fetchall()
    #Verificación de existencia de datos en la tabla de citas
    if len(codLote) == 0:
        #Mensaje de error
        print("Este Paciente No Posee Cita\n")
        return False
    else:
        try:
            codLote=codLote[0]
            codLote1=codLote[0]
        except IndexError:
            print("No hay datos disponibles")
            return False
        #Select que obtiene los datos de la tabla de Lotes
        cursorObj.execute(f'SELECT Cantidad_Recibida, Cantidad_Usada FROM Lotes WHERE Codigo_De_Lote= {codLote1}')
        cantReUs=cursorObj.fetchall()
        cantReUs=cantReUs[0]
        cantReUs1=cantReUs[0]
        cantReUs2=cantReUs[1]
        #Verificación de vacunas existentes
        if cantReUs1>0:
            usado=cantReUs2+1
            #Actualización de la cantiadad de vacunas usada basada en Cantidad_Usada
            cursorObj.execute(f'UPDATE Lotes SET Cantidad_Usada = {usado} WHERE Codigo_De_Lote = {codLote1}')
        con.commit()
        return True
    
#-----DESDE AQUI MODULO DE LOTES-------------------------------------------------------------------------------------------------------

#Función crearLote(con): 
def crearLote(con):
    cursorObj = con.cursor()
    #Ingreso de No. de lote y verificación de longitud de la entrada
    while True:
        noLote=input("Ingrese el número de lote: ")
        longitud=10
        longCod=len(noLote)
        if longCod<=longitud:
            noLote=noLote.rjust(longitud," ")
            break
        else:
            print("Máximo escriba 10 digitos")
    
    #Seleccion Del Fabricante De La Vacuna
    while True:
        #Impresión del listado se fabricantes de vacunas
        print('''1. Sinovac\n2. Pfizer\n3. Moderna\n4. Sputnik\n5. AstraZeneca\n6. Sinopharm\n7. Covaxim''')
        try:
            fabricante=int(input("\nSeleccione un Fabricante: "))
            if fabricante > 0 and fabricante < 8:
                break
            else:
                print("Fabricante Invalido")
        except:
            ("Debe ser Numero")
    fabricante=fabricantes(fabricante)
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
    cantidadUsada=0
    #Ingreso de día de vencimiento de la vacuna con verificacines de entrada
    while True:
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
            year=year.rjust(4,"0")
            try:
                if int(year) >= date.today().year:
                    break
                else:
                    print("Debe ser Mayor o Igual al Año actual")
            except:
                print("El Número debe ser Digito")
        #Concatenación de la fecha de vencimiento de la vacuna
        fechaVencimiento=day+"/"+month+"/"+year
        if comprobarFecha(fechaVencimiento) == "Mayor":
            break
    #Imagen: proximamente
    imagen="Aún no"
    datosLotes=(noLote,fabricante[0],fabricante[1],cantidadRecibida,cantidadUsada,cantidadAsignada,fabricante[2],fabricante[3],fabricante[4],fabricante[5],fechaVencimiento,imagen)
    #Insercion de los datos a la tabla de Lotes, Nueva Fila
    try:
        cursorObj.execute("INSERT INTO Lotes VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosLotes)
        #Envio de la peticion a la base de datos
        con.commit()
    except:
        print("El Lote ya existe")
    #Llamado del menú de gestión de lotes 
    menuLotes()

#Función fabricantes(fabricante): De acuerdo a la elección de fabricante retorna la información del la vacuna correspondiente al fabricante
def fabricantes(fabricante):
    tiposFabricantes = {1:"Sinovac",2:"Pfizer",3:"Moderna",4:"SputnikV",5:"AstraZeneca",6:"Sinopharm",7:"Covaxim"}
    if tiposFabricantes[fabricante] == "Sinovac":
        return ("Sinovac","Virus Desactivado",2,"2°","50%","No se sabe")
    elif tiposFabricantes[fabricante] == "Pfizer":
        return ("Pfizer","ARN",2,"-80°","95%","No se sabe")
    elif tiposFabricantes[fabricante] == "Moderna":
        return ("Moderna","ARN",2,"-25°","94.5%","90 Dias")
    elif tiposFabricantes[fabricante] == "SputnikV":
        return ("SputnikV","Vector Viral",2,"-18°","92%","150 Dias")
    elif tiposFabricantes[fabricante] == "AstraZeneca":
        return ("AstraZeneca","Vector Viral",2,"2°","62%","No se sabe")
    elif tiposFabricantes[fabricante] == "Sinopharm":
        return ("Sinopharm","Vector Viral",2,"2°","79.3%","No se sabe")
    elif tiposFabricantes[fabricante] == "Covaxin":
        return ("Covaxim","Virus Desactivado",2,"2°","78%","No se sabe")

#Función consultarLote(con):Esta función permite visualizar la información contenida en la tabla de lotes de acuerdo a un código de lote
def consultarLote(con):
    cursorObj = con.cursor()
    #Recepcion del Numero del lote a consultar
    noLote=(input("Ingrese el número de lote a consultar: "))
    noLote=noLote.ljust(10)
    noLote=noLote[:10]
    lote="Vacio"
    #Seleccion de datos basado en el Numero_De_Lote
    cursorObj.execute(f'SELECT * FROM Lotes WHERE Codigo_De_Lote = {noLote}')
    #Recoleccion de los datos en la tupla "consultados"
    lote=cursorObj.fetchall()
    if len(lote) <= 0:
        print("El Lote No Existe")
    else:    
        #Impresion de la tupla correspondiente al lote
        lote1=lote[0]
        print("-------------------------------------------------------------------")
        print("| Código Lote                   || {:<30} |\n| Fabricante                    || {:<30} |\n| Tipo de Vacuna                || {:<30} |\n| Cantidad Recibida             || {:<30} |\n| Cantidad Asignada             || {:<30} |\n| Cantidad Usada                || {:<30} |\n| Dosis Necesarias              || {:<30} |\n| Temperatura de Almacenamiento || {:<30} |\n| Efectividad Identificada      || {:<30} |\n| Tiempo de Protección          || {:<30} |\n| Fecha de Vencimiento          || {:<30} |\n| Imágen                        || {:<30} |".format(lote1[0],lote1[1],lote1[2],lote1[3],lote1[4],lote1[5],lote1[6],lote1[7],lote1[8],lote1[9],lote1[10],lote1[11]))
        print("-------------------------------------------------------------------")
    #Llamado del menú de gestión de lotes
    menuLotes()
    
#-----DESDE AQUI MODULO DE PLANES DE VACUNACION-------------------------------------------------------------------------------------------------------

#Función crearPlan(con): Permite generar un nuevo plan de vacunación y almacenar la información en la tabla de Planes
def crearPlan(con):
    cursorObj = con.cursor()
    #Ingreso de un id para asignarlo a un plan
    idPlan=input("CONSECUTIVO del plan de vacunación: ")
    idPlan=idPlan.ljust(2)
    while True:
        #Ingreso el día de de inicio del plan de vacunación
        while True:
            day=input("DÍA de inicio del plan de vacunación: ")
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
            month=input("MES de inicio del plan de vacunación: ")
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
            year=input("AÑO de inicio del plan de vacunación: ")
            year=year.rjust(4,"0")
            try:
                int(year)
                break
                #Concatenación de la fecha de inicio del plan de vacunación
            except:
                print("Debe Ser Un Numero")
        fechaInicio=day+"/"+month+"/"+year
        if comprobarFecha(fechaInicio) == "Mayor":
            break
        else:
            print("fecha invalida")
    #Concatenación de la fecha de fin del plan de vacunación
    fechaFin = "24/05/2121"
    error=False
    while True:
        while True:
            try:
                edadMin=int(input("Ingrese la edad mínima para clasificar a este plan: "))
                break
            except:
                #Mensaje en pantalla de un error al digitar
                print("El Número debe ser Digito")
        cursorObj.execute('SELECT Edad_Min, Edad_Max FROM Planes')
        minMax=cursorObj.fetchall()
        intervaloActual = 0
        #Validación de cruce de la edad mínima con los otros planes
        while intervaloActual != len(minMax):
            intervalo=minMax[intervaloActual]
            minima=intervalo[0]
            maxima=intervalo[1]
            if edadMin >= minima-1 and  edadMin <= maxima:
                error=True
                print("Edad Presenta Cruce")
                break
            else:
                error=False
            intervaloActual += 1
        if error == False:
            break

    while True:
        while True:
            try:
                edadMax=int(input("Ingrese la edad máxima para clasificar a este plan: "))
                if edadMin < edadMax:
                    break
                else:
                    print("La edad Maxima debe ser mayor a la Minima")
            except:
                #Mensaje en pantalla de un error al digitar
                print("El Número debe ser Digito")
        
        cursorObj.execute('SELECT Edad_Min, Edad_Max FROM Planes')
        minMax=cursorObj.fetchall()
        intervaloActual = 0
        #Validación de cruce de la edad máxima con los otros planes
        while intervaloActual != len(minMax):
            intervalo=minMax[intervaloActual]
            menor=intervalo[0]
            mayor=intervalo[1]
            if edadMax >= menor and edadMax <= mayor :
                error=True
                print("Edad Presenta Cruce")
                break
            else:
                error=False
            intervaloActual += 1
        intervaloActual = 0
        if error == False:
            while intervaloActual != len(minMax):
                intervalo=minMax[intervaloActual]
                minima=intervalo[0]
                maxima=intervalo[1]
                if edadMin <= minima <= edadMax or edadMin <= maxima <= edadMax:
                    print ("El Intervalo presenta cruce con otro plan")
                    error = True
                    break
                intervaloActual += 1
        if error == False:
            break
    datosPlanes=(idPlan,edadMin,edadMax,fechaInicio,fechaFin)
    try:
        cursorObj.execute("INSERT INTO Planes VALUES(?,?,?,?,?)",datosPlanes)
        con.commit()
        calcularPlan(con)
    except: 
        print ("El Plan ya existe")
    55
    menuPlanes()

#Función cierrePlanVacunacion(con): Esta función sirve para actualizar la fecha de terminación de un plan de vacunación 
def cierrePlanVacunacion(con):
    cursorObj = con.cursor()
    #Ingreso de un id para asignarlo a un plan
    idPlan=input("Ingrese el consecutivo del plan de vacunación: ")
    idPlan=idPlan.ljust(2)
    #Ingreso el día de de inicio del plan de vacunación
    while True:
        while True:
            day=input("Ingrese el día de la fecha en la que quiere cerrar el plan de vacunación: ")
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
            month=input("Ingrese el mes de la fecha en la que quiere cerrar el plan de vacunación: ")
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
            year=input("Año en el que quiere cerrar el plan de vacunación: ")
            year=year.rjust(4,"0")
            try:
                int(year)
                break
                #Concatenación de la fecha de cierre del plan de vacunación
            except:
                print("Debe Ser Un Numero")
        fechaFin=day+"/"+month+"/"+year
        fechaFinComprobacion = datetime.strptime(fechaFin, '%d/%m/%Y')
        fechaActual = datetime.today()
        minMax= "Vacio"
        cursorObj.execute(f'SELECT Fecha_Inicio FROM Planes WHERE ID = {idPlan}')
        minMax=cursorObj.fetchall()
        if len(minMax) <= 0:
            print ("El Plan no existe")
            break
        else:
            fechaIn=minMax[0]
            fechaIn1=fechaIn[0]
            fechaInComprobacion = datetime.strptime(fechaIn1, '%d/%m/%Y')
            fechaActual = datetime.today()
            if fechaInComprobacion <= fechaFinComprobacion or fechaFinComprobacion >= fechaActual:
                break
            else:
                print("Fecha Invalida")
    cursorObj.execute(f'UPDATE Planes SET Fecha_Fin = {fechaFin} WHERE ID = {idPlan}')
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
    planes="Vacio"
    #Seleccion de campos basado en el ID suministrado
    cursorObj.execute(f'SELECT * FROM Planes WHERE ID = {noId} ')
    #Recoleccion de los datos en la tupla "consultados"
    planes=cursorObj.fetchall()
    if len(planes) <= 0:
        print("El plan no existe")
    else:
        #Impresion de la tupla correspondiente al plan
        planes1=planes[0]
        print("---------------------------------------------")
        print("| Consecutivo Plan  || {:<20} |\n| Edad Mínima       || {:<20} |\n| Edad Máxima       || {:<20} |\n| Fecha de Inicio   || {:<20} |\n| Fecha de Fin      || {:<20} |".format(planes1[0],planes1[1],planes1[2],planes1[3],planes1[4]))
        print("---------------------------------------------")
        
    menuPlanes()

#Función calcularPlan(con): Función que sirve para asignar un plan de vacunación a un afiliado de acuerdo a los datos registrados en la tabla de afiliados
def calcularPlan(con):
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
    #Bucle para acceso a los datos dentro de "Afiliados"
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
    menuPrincipal()

#-----DESDE AQUI MODULO DE PROGRAMA DE VACUNAS-------------------------------------------------------------------------------------------------------
def calcularProgramacion(con):
    cursorObj=con.cursor()
    print("""Bienvenido al Creador de progamas de vacunación
    Una vez ingresados los datos requeridos acontinuación, se le asignará una cita a todos los afiliados actuales.
    Teniendo en cuenta los planes de vacunacion existentes y asignados, asi como los parametros que ingresará acontinuacion
    Recuerde que debido a la situacion COVID actual, las citas se asignaran 30 minutos una despues de la otra""")
    print("Ingrese los datos de las fechas dentro de las que quiere asignar las citas")
    while True:
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
                if int(year) > 2020:
                    break
                else:
                    print("Debe ser mayor a 2020")
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        #Concatenación de la fecha de inicio de la asignacion de citas
        fechaInicio= day + "/" + month + "/" + year
        if comprobarFecha(fechaInicio) == "Mayor":
            break
        else:
            print("La fecha debe ser mayor a la actual")
    #Ingreso de día de de fin de la asignacion de citas
    year = "2121"
    fechaFin = day + "/" + month + "/" + year
    while True:
        while True:
            print("Ingrese los datos de su horario de atencion deseado")
            horaInicio= input("Hora de Inicio del horario de atención (24 hrs)(00:00) : ")
            horaInicio=horaInicio.split(":")
            try:
                horaComprobacion=int(horaInicio[0]),int(horaInicio[1])
                inicio = datetime.strptime(fechaInicio +" "+ str(horaInicio[0]) +":"+ str(horaInicio[1]), "%d/%m/%Y %H:%M")
                break
            except :
                #Mensaje en pantalla de un error al digitar
                print("Debe ser formato 24hrs")
        if inicio < datetime.today():
            print("La fecha y hora de inicio deben ser mayores a la hora actual")
            calcularProgramacion(con)
        else:
            break
    if int(horaInicio[1]) < 30 and int(horaInicio[1]) != 0:
        horaInicio[1] = 30
    elif int(horaInicio[1]) > 30:
        horaInicio[1] = "00"
        horaInicio[0] = int(horaInicio[0]) + 1
    if int(horaInicio[1]) == 0:
        horaInicio[1] == "00"
    horaCitas=[]
    horaIterando=horaInicio
    while int(horaIterando[0]) < 24:
        horaCitas.append(horaIterando)
        horaIterando=[int(horaIterando[0]),int(horaIterando[1])]
        horaIterando[1] += 30
        if horaIterando[1] == 0 or horaIterando[1] =="00":
            horaIterando[1] = "00"
        if horaIterando[1] >= 60:
            horaIterando[0] += 1
            horaIterando[1] = "00"
        horaIterando=[str(horaIterando[0]),str(horaIterando[1])]
    #Seleccion de los datos de los pacientes
    cursorObj.execute("SELECT Numero_De_Identificacion, Ciudad_De_Residencia, Fecha_De_Desafiliacion FROM Afiliados")
    #Recopilacion en la tupla "afiliados"
    afiliados=cursorObj.fetchall()
    #Seleccion de los Planes vigentes
    cursorObj.execute("SELECT ID FROM Planes")
    #Recopilacion en la tupla "Planes"
    planes=cursorObj.fetchall()
    secuencial = 1
    loteActual = 0
    for plan in range(1,len(planes)):
        cursorObj.execute(f'SELECT Numero_De_Identificacion, Ciudad_De_Residencia, ID_Plan FROM Afiliados WHERE ID_Plan = {plan} AND Fecha_De_Desafiliacion = "-"')
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
            try:
                vacunas=vacunas[loteActual]
            except:
                print("No hay vacunas suficientes")
                menuCitas()
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
            try:
                cursorObj.execute("INSERT INTO Citas Values (?,?,?,?,?,?,?)",nuevaCita)
                con.commit()
            except:
                print("Ya existen citas para este afiliado")
            #Aumento del secuencial de citas
            secuencial += 1
            #Aumento para cambio de afiliado
            afiliado += 1
    #Retorno a la funcion de origen
    menuCitas()
    
#Función consultarProgramaIndividual(): Esta función permite al usuario visualizar los datos de la cita
#a partir de un número de identificación
def consultarProgramaIndividual():
    cursorObj = con.cursor()
    #Recepcion del numero de identificación
    while True:
        #Recepción del numero de identificacion a consultar
        noIdentificacion=input("Ingrese el número de identificación del paciente: ")
        noIdentificacion=noIdentificacion.rjust(12," ")
        try:
            #Comporobacion de tipo para la variable noIdentificacion
            noIdentificacion = int(noIdentificacion)
            break
        except ValueError:
            #Mensaje en pantalla de un error al digitar
            print("Escriba un número entero")
    #Select que obtiene los datos asociados al número de identificación ingresado de la tabla citas 
    citas="Vacio"
    cursorObj.execute('SELECT * FROM Citas WHERE Numero_De_Identificacion=?',(noIdentificacion,))
    citas=cursorObj.fetchall()#citas guarda la tupla con los datos obtenidos
    if len(citas) != 0:
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
    else:
        #Mensaje en caso de que la tabla este vacia o el paciente no se encuentre
        print("No existen citas para este paciente")
    menuCitas()

#Función consultarProgramaGeneral(): Esta función permite al usuario visualizar todos los datos de la tabla citas
def consultarProgramaGeneral():
    cursorObj = con.cursor()
    #Select que obtiene los datos de la tabla de citas
    cursorObj.execute('SELECT * FROM Citas')
    citas=cursorObj.fetchall() #Citas guarda la tupla con los datos obtenidos
    #Encabezado de la tabla que imprime los datos de las citas agendadas
    print("\n| No. Cita | IdPlan | Identificación | Ciudad               | Lote Asignado | Fecha De La Cita | Hora De La Cita |")
    print("------------------------------------------------------------------------------------------------------------------")
    #Tabla que imprime los datos de las citas agendadas
    for citas in citas:
        cita= "| {:<8} | {:<6} | {:<14} | {:<5} | {:<13} | {:<16} | {:<15} |".format(citas[0],citas[1],citas[2],citas[3],citas[4],citas[5],citas[6])
        print (cita)
    menuCitas()
#Funcion para comprobar la validez de una fecha dada sobre la actual
def comprobarFecha(fechaDada):
    try:
        #Obtencion de la fecha actual
        fechaActual=datetime.today()
        fechaActual = str(datetime.today().day)+"/"+str(datetime.today().month)+"/"+str(datetime.today().year)
        fechaActual=datetime.strptime(fechaActual,"%d/%m/%Y")
        #Comprobación de existencia de la fecha dada
        fechaComprobar=datetime.strptime(fechaDada, "%d/%m/%Y")
        #Comprobación de Consistencia de la fecha
        if fechaComprobar < fechaActual:
            return "Menor"
        elif fechaComprobar >= fechaActual:
            return "Mayor"
    except ValueError:
        #Valor de retorno de la funcion
        return "Inexistente"

#Conexion con la base de datos
con=sql_connection()

#Ejecucion de funciones
sql_table(con)
print("Bienvenido")
menuPrincipal()

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