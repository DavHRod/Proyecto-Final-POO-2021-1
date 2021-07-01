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
#-----DESDE AQUI MODULO DE AFILIADOS-------------------------------------------------------------------------------------------------------
#Función afiliarPaciente: Esta función recibe los datos de un nuevo paciente a afiliar y realiza la inserción en la tabla

class afiliado:
    def __init__(self):
        self.ide = 0
        self.nombre = ""
        self.apellido = ""
        self.direccion = ""
        self.telefono = 0
        self.correo = ""
        self.ciudad = ""
        self.nacimiento = ""
        self.edad = 0
        self.afiliacion = ""
        self.desafiliacion = ""
        self.vacunado = ""

    def calcEdad(self,fechaNacimiento,fechaActual):
        fechaNacimiento=datetime.strptime(fechaNacimiento, "%d/%m/%Y")
        self.edad = fechaNacimiento - fechaActual
        if fechaNacimiento >= fechaActual:
            return False
        else:
            return True

    def afiliar(self,con):
        cursorObj = con.cursor()
        #Bucle de comprobacion de entrada
        while True:
            #Recepción del número de identificación
            self.ide = input("Ingrese el número de identificación del paciente: ")
            #Variable con la longitud máxima
            longMax = 12
            #Variable con la longitud del string
            longId = len(self.ide)
            #Condicional para comprobar la longuitud de la respuesta
            if longId <= longMax:
                self.ide = self.ide.rjust(longMax," ")
                #Comprobación para el tipo de dato
                try:
                    self.ide = int(self.ide)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            else:
                #Mensaje de Error por longuitud del dato
                print("Máximo escriba 12 digitos")
            
        #Ingreso de nombre de un nuevo paciente
        self.nombre = input("Ingrese el nombre del paciente: ")
        self.nombre = self.nombre.ljust(20)
        #Limitación del tamaño del string
        self.nombre = self.nombre[:20]
        #Ingreso de apellido de un nuevo paciente
        self.apellido = input("Ingrese el apellido del paciente: ")
        self.apellido = self.apellido.ljust(20)
        #Limitación del tamaño del string
        self.apellido = self.apellido[:20]
        #Ingreso de dirección de residencia de un nuevo paciente
        self.direccion = input("Ingrese la dirección de residencia del paciente: ")
        self.direccion = self.direccion.ljust(30)
        #Limitación del tamaño del string
        self.direccion = self.direccion[:30]
        #Ingreso de telefono de un nuevo paciente
        #Bucle de comprobación de entrada
        while True:
            #Recepción del número de telefono
            self.telefono = input("Ingrese un número de contacto: ")
            #Variable con la longitud máxima
            longitud = 10
            #Variable con la longitud del string
            longVariable = len(self.telefono)
            #Condicional para comprobar la longuitud de la respuesta
            if longVariable <= longitud:
                #Comprobación para el tipo de dato
                try:
                    self.telefono = int(self.telefono)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
                self.telefono = self.telefono.ljust(10)
            else:
                #Mensaje de Error por longuitud del dato
                print("Máximo escriba 10 digitos")

        #Ingreso de correo de un nuevo paciente
        #Bucle de comprobación de entrada, de existencia real de correo ingresado
        while True:
            #Recepción del correo
            self.correo = input("Ingrese el correo electrónico del paciente: ")
            #Uso del metodo validate_email y recepción del retorno en la variable es_valido
            #es_valido = validate_email(self.correo, verify=True)
            #Comprobación del retorno del metodo
            #if es_valido == False:
                #Mensaje de Error
                #print("No valido, ingrese un correo valido")
            #else: 
                #Ruptura del bucle de comprobación
            break
        #Ingreso de ciudad de origen de un nuevo paciente
        self.ciudad = input("Ingrese la ciudad en la que reside el paciente: ")
        self.ciudad = self.ciudad.ljust(20)
        #Limitación del tamaño del string
        self.ciudad = self.ciudad[:20]
        #Bucle de comprobacion de entrada para fecha
        while True:
            #Bucle de comprobacion de entrada
            while True:
                #Ingreso de día de self.nacimiento de un nuevo paciente
                day = input("Ingrese el día de nacimiento: ")
                day = day.rjust(2,"0")
                #Comprobación para el tipo de dato
                try:
                    #Condicional para comprobación de rango de la entrada
                    if int(day) < 32 and int(day) >0 :
                        #Ruptura del bucle de comprobación
                        break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            #Bucle de comprobacion de entrada
            while True:
                #Ingreso de mes de nacimiento de un nuevo paciente
                month = input("Ingrese el mes de nacimiento: ")
                month = month.rjust(2,"0")
                #Comprobación para el tipo de dato
                try:
                    #Condicional para comprobación de rango de la entrada
                    if int(month) < 13 and int(month) >0 :
                        #Ruptura del bucle de comprobación
                        break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            
            #Bucle de comprobacion de entrada
            while True:
                #Ingreso de año de nacimiento de un nuevo paciente
                year = input("Ingrese el año de nacimiento: ")
                year = year.rjust(4,"0")
                #Comprobación para el tipo de dato
                try:
                    year = int(year)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            #Concatenación de la fecha de nacimiento del nuevo paciente
            self.nacimiento=str(day)+"/"+str(month)+"/"+str(year)
            #Obtención de la fecha actual
            fechaActual=datetime.today()
            #Uso de una variable auxiliar para comprobar la existencia de la fecha
            try:
                #Comprobación de integridad de la fecha
                if self.calcEdad(self.nacimiento,datetime.today()):
                    #Ruptura del bucle de comprobación
                    break
                else:
                    print("Fecha Invalida") 
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
        datosPaciente=(self.ide,"None",self.nombre,self.apellido,self.direccion,self.telefono,self.correo,self.ciudad,self.nacimiento,fechaActual,"No","No")
        #Insercion de los datos a la tabla de Afiliados, Nueva Fila
        cursorObj.execute("INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosPaciente)
        #Envio de la petición a la base de datos
        con.commit()

    #Función consultarAfiliado: Esta función permite al usuario consultar los datos de un paciente,
    #Se debe ingresar el número de identificación del paciente para que la función busque en la tabla los datos
    def consultar(self,con):
        cursorObj = con.cursor()
        #Bucle de comprobación
        while True:
            while True:
                #Recepcion del número de identificación a consultar
                self.ide=input("Ingrese el número de identificación del paciente a consultar: ")
                #Comprobación del tipo de dato
                try:
                    self.ide = int(self.ide)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            #Selección de campos basado en la identificación de pacientes basado en el Numero_de_identificacion
            consultados="Vacio"
            cursorObj.execute('SELECT * FROM Afiliados WHERE Numero_de_identificacion = ? ',(self.ide,))
            #Recolección de los datos en la tupla "consultados"
            consultados=cursorObj.fetchall()
            if len(consultados) <= 0:
                print("No existe")
            elif len(consultados) > 0:
                consultados1=consultados[0]
                #Impresión de la tupla correspondiente a la información paciente en forma de tabla
                print("------------------------------------------------------------")
                print("| No. Identificación     || {:<30} |\n| IdPlan                 || {:<30} |\n| Nombre                 || {:<30} |\n| Apellido               || {:<30} |\n| Dirección              || {:<1} |\n| telefono               || {:<30} |\n| correo                 || {:<30} |\n| ciudad de Residencia   || {:<30} |\n| Fecha de nacimiento    || {:<30} |\n| Fecha de Afiliación    || {:<30} |\n| Fecha de desafiliación || {:<30} |\n| Vacunado SI/NO         || {:<30} |".format(consultados1[0],consultados1[1],consultados1[2],consultados1[3],consultados1[4],consultados1[5],consultados1[6],consultados1[7],consultados1[8],consultados1[9],consultados1[10],consultados1[11]))
                print("------------------------------------------------------------")
                break

    #Función desafiliarPaciente: Con esta función se ingresa la fecha de desafiliación de un paciente    
    def desafiliar(self,con):
        cursorObj = con.cursor()
        #Bucle de comprobación
        while True:
            #Recepción del número de identificación
            self.ide=input("Ingrese el número de identificación del paciente a desafiliar: ")
            #Comprobación del tipo de dato
            try:
                self.ide = int(self.ide)
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
        cursorObj.execute('UPDATE Afiliados SET Fecha_De_Desafiliacion = ? WHERE Numero_de_identificacion = ?',(fechaDesafiliacion,self.ide))
        #Envio de la petición a la base de datos
        con.commit()
        #Llamado del menú de gestión de datos

    #Función vacunarAfiliado: Con esta función se actualiza el estado de vacunación de un afiliado en la tabla afiliado 
    def vacunar(self,con):    
        cursorObj = con.cursor()    
        #Bucle de comprobación
        while True:
            #Ingreso de número de identificación del paciente a vacunar
            self.ide=input("Ingrese el número de identificación del paciente a Vacunar: ")
            #Comprobación del tipo de dato
            try:
                self.ide = int(self.ide)
                #Ruptura del bucle de comprobación
                break
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        desafiliado="vacio"
        #Selección de la fecha de desafiliacion del paciente a vacunar
        cursorObj.execute('SELECT Fecha_De_Desafiliacion FROM Afiliados WHERE Numero_De_Identificacion=?',(self.ide,))
        #Recopilación en el array "desafiliado"
        desafiliado=cursorObj.fetchall()
        if len(desafiliado) <= 0:
            print("No existe")
            
        else:
            #Acceso a la tupla del afiliado
            desafiliado1=desafiliado[0]
            #Acceso al dato
            desafiliado2=desafiliado1[0]
            #Condicional de comprobacíon de desafiliación
            if desafiliado2 != "No":
                #Mensaje de Advertencia
                print("El paciente está desafiliado y no será vacunado\n")
            else:
                #Actualización del estado de vacunación del afiliado basado en el Numero_de_identificacion, columna "Vacunado"
                cursorObj.execute('UPDATE Afiliados SET Vacunado="Si" WHERE Numero_de_identificacion=?',(self.ide,))
                self.contadorVacunacion(con)
                #Envio de la petición a la base de datos
                con.commit()

    #Función contadorVacunacion(self.ide): Esta función actualiza la cantidad de vacunas utilizadas en la tabla Lotes
    def contadorVacunacion(self,con):
        cursorObj = con.cursor()
        codLote="vacio"
        #Select que obtiene los datos de la tabla de Citas
        cursorObj.execute('SELECT Codigo_De_Lote FROM Citas WHERE Numero_De_Identificacion=?',(self.ide,))
        codLote=cursorObj.fetchall()
        #Verificación de existencia de datos en la tabla de citas
        if len(codLote) == 0:
            #Mensaje de error
            print("Este Paciente No Posee Cita\n")
        else:
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
            #Verificación de vacunas existentes
            if cantReUs1>0:
                usado=cantReUs2+1
                #Actualización de la cantiadad de vacunas usada basada en Cantidad_Usada
                cursorObj.execute('UPDATE Lotes SET Cantidad_Usada=? WHERE Codigo_De_Lote=?',(usado,codLote1))
            con.commit()