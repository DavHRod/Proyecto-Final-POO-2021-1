#Importación de librerias a usar
#Validate_email: Es la libreria que permite realizar la validación de un correo electrónico, su dominio y su existencia en el dominio señalado.
#Requiere instalación de py3DNS mediante el comando pip install py3DNS, esto con permisos de administrador activos
from validate_email import validate_email
#datetime: Libreria integrada en python 3, permite el manejo y operación de variables tipo datetime,
#es usada para comprobacion y validacion de fechas bajo parametros propios
from datetime import date
from datetime import datetime
from Planes import *
from sql import *
#-----DESDE AQUI MODULO DE AFILIADOS-------------------------------------------------------------------------------------------------------
#Función afiliarPaciente: Esta función recibe los datos de un nuevo paciente a afiliar y realiza la inserción en la tabla


class afiliado:
    def __init__(self,ide,id_plan,nombre,apellido,direccion,telefono,correo,ciudad,nacimiento,edad,afiliacion,desafiliacion,vacunado):
        self.__ide = ide
        self.__id_plan = id_plan
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__ciudad = ciudad
        self.__nacimiento = nacimiento
        self.__edad = edad
        self.__afiliacion = afiliacion
        self.__desafiliacion = desafiliacion
        self.__vacunado = vacunado
        self.__calc_edad(self.__nacimiento)
        self.__sql = sql()

    def set_ide(self,ide):
        self.__ide = ide
    def get_ide(self):
        return self.__ide

    def set_id_plan(self,id_plan):
        self.__id_plan = id_plan
    def get_id_plan(self):
        return self.__id_plan

    def set_nombre(self,nombre):
            self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre

    def set_apellido(self,apellido):
            self.__apellido = apellido
    def get_apellido(self):
        return self.__apellido

    def set_direccion(self,direccion):
            self.__direccion = direccion
    def get_direccion(self):
        return self.__direccion

    def set_telefono(self,telefono):
            self.__telefono = telefono
    def get_telefono(self):
        return self.__telefono

    def set_correo(self,correo):
            self.__correo = correo
    def get_correo(self):
        return self.__correo

    def set_ciudad(self,ciudad):
            self.__ciudad = ciudad
    def get_ciudad(self):
        return self.__ciudad

    def set_nacimiento(self,nacimiento):
            self.__nacimiento = nacimiento
    def get_nacimiento(self):
        return self.__nacimiento

    def set_edad(self,edad):
            self.__edad = edad
    def get_edad(self):
        return self.__edad

    def set_afiliacion(self,afiliacion):
            self.__afiliacion = afiliacion
    def get_afiliacion(self):
        return self.__afiliacion

    def set_desafiliacion(self,desafiliacion):
            self.__desafiliacion = desafiliacion
    def get_desafiliacion(self):
        return self.__desafiliacion

    def set_vacunado(self,vacunado):
            self.__vacunado = vacunado
    def get_vacunado(self):
        return self.__vacunado

    def __calc_edad(self, fechaNacimiento):
        fechaNacimiento = datetime.strptime(fechaNacimiento, "%d/%m/%Y")
        actual=datetime.today().strftime("%d/%m/%Y")
        actual=datetime.strptime(actual,"%d/%m/%Y")
        self.__edad = actual.year - fechaNacimiento.year
        self.__edad -= ((actual.month, actual.day) <(fechaNacimiento.month, fechaNacimiento.day))
            

    def load_all(self):
        tupla = self.__sql.get_table("Afiliados")
        return tupla

    def to_tuple(self):
        obj_tuple = (self.__ide,
            self.__id_plan,
            self.__nombre,
            self.__apellido,
            self.__direccion,
            self.__telefono,
            self.__correo,
            self.__ciudad,
            self.__nacimiento,
            self.__edad,
            self.__afiliacion,
            self.__desafiliacion,
            self.__vacunado)
        return obj_tuple
"""
    def afiliar(self, con):
        planN=plan()
        cursorObj = con.cursor()
        #Bucle de comprobacion de entrada
        while True:
            #Recepción del número de identificación
            self.__ide = input("Ingrese el número de identificación del paciente: ")
            #Variable con la longitud máxima
            longitudId = 12
            #Variable con la longitud del string
            longId = len(self.__ide)
            #Condicional para comprobar la longuitud de la respuesta
            if longId <= longitudId:
                self.__ide = self.__ide.rjust(longitudId, " ")
                #Comprobación para el tipo de dato
                try:
                    self.__ide = int(self.__ide)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            else:
                #Mensaje de Error por longuitud del dato
                print("Máximo escriba 12 digitos")

        #Ingreso de nombre de un nuevo paciente
        self.__nombre = input("Ingrese el nombre del paciente: ")
        self.__nombre = self.__nombre.ljust(20)
        #Limitación del tamaño del string
        self.__nombre = self.__nombre[:20]
        #Ingreso de apellido de un nuevo paciente
        self.__apellido = input("Ingrese el apellido del paciente: ")
        self.__apellido = self.__apellido.ljust(20)
        #Limitación del tamaño del string
        self.__apellido = self.__apellido[:20]
        #Ingreso de dirección de residencia de un nuevo paciente
        self.__direccion = input("Ingrese la dirección de residencia del paciente: ")
        self.__direccion = self.__direccion.ljust(30)
        #Limitación del tamaño del string
        self.__direccion = self.__direccion[:30]
        #Ingreso de telefono de un nuevo paciente
        #Bucle de comprobación de entrada
        while True:
            #Recepción del número de telefono
            self.__telefono = input("Ingrese un número de contacto: ")
            #Variable con la longitud máxima
            longitud = 10
            #Variable con la longitud del string
            longVariable = len(self.__telefono)
            #Condicional para comprobar la longuitud de la respuesta
            if longVariable <= longitud:
                #Comprobación para el tipo de dato
                try:
                    self.__telefono = int(self.__telefono)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
                self.__telefono = self.__telefono.ljust(10)
            else:
                #Mensaje de Error por longuitud del dato
                print("Máximo escriba 10 digitos")

        #Ingreso de correo de un nuevo paciente
        #Bucle de comprobación de entrada, de existencia real de correo ingresado
        while True:
            #Recepción del correo
            self.__correo = input("Ingrese el correo electrónico del paciente: ")
            #Uso del metodo validate_email y recepción del retorno en la variable es_valido
            es_valido = validate_email(self.__correo, verify=True)
            #Comprobación del retorno del metodo
            if es_valido == False:
                #Mensaje de Error
                print("No valido, ingrese un correo valido")
            else:
                #Ruptura del bucle de comprobación
                break
        #Ingreso de ciudad de origen de un nuevo paciente
        self.__ciudad = input("Ingrese la ciudad en la que reside el paciente: ")
        self.__ciudad = self.__ciudad.ljust(20)
        #Limitación del tamaño del string
        self.__ciudad = self.__ciudad[:20]
        #Bucle de comprobacion de entrada para fecha
        while True:
            #Bucle de comprobacion de entrada
            while True:
                #Ingreso de día de nacimiento de un nuevo paciente
                day = input("Ingrese el día de nacimiento: ")
                day = day.rjust(2, "0")
                #Comprobación para el tipo de dato
                try:
                    #Condicional para comprobación de rango de la entrada
                    if int(day) < 32 and int(day) > 0:
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
                month = input("Ingrese el mes de nacimiento: ")
                month = month.rjust(2, "0")
                #Comprobación para el tipo de dato
                try:
                    #Condicional para comprobación de rango de la entrada
                    if int(month) < 13 and int(month) > 0:
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
                year = input("Ingrese el año de nacimiento: ")
                year = year.rjust(4, "0")
                #Comprobación para el tipo de dato
                try:
                    year = int(year)
                    if int(year) < datetime.today().year:
                        #Ruptura del bucle de comprobación
                        break
                    else:
                        print("Año invalido")
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            #Concatenación de la fecha de nacimiento del nuevo paciente
            self.__nacimiento = str(day)+"/"+str(month)+"/"+str(year)
            #Obtención de la fecha actual
            fechaActual = datetime.today()
            #Uso de una variable auxiliar para comprobar la existencia de la fecha
            try:
                #Uso de una variable auxiliar para comprobar la existencia de la fecha
                fechaNacimientoComprobacion = datetime.strptime(self.__nacimiento, "%d/%m/%Y")
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
        dayActual = today.day
        #Mes actual
        monthActual = today.month
        #Año actual
        yearActual = today.year
        #Concatenación fecha actual
        self.__afiliacion = str(dayActual)+"/"+str(monthActual)+"/"+str(yearActual)
        #Tupla con todos los datos ingresados En la funcion Afiliar
        datosPaciente = (self.__ide, "-", self.__nombre, self.__apellido, self.__direccion,self.__telefono, self.__correo, self.__ciudad, self.__nacimiento, self.__afiliacion, "-", "-")
        try:
            #Insercion de los datos a la tabla de Afiliados, Nueva Fila
            cursorObj.execute( "INSERT INTO Afiliados VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", datosPaciente)
            #Envio de la petición a la base de datos
            con.commit()
            planN.calcular(con)
        except:
            print("El Afiliado ya existe")
        
    #Función consultarAfiliado: Esta función permite al usuario consultar los datos de un paciente,
    #Se debe ingresar el número de identificación del paciente para que la función busque en la tabla los datos

    def consultar(self, con):
        cursorObj = con.cursor()
        #Bucle de comprobación
        while True:
            while True:
                #Recepcion del número de identificación a consultar
                self.__ide = input(
                    "Ingrese el número de identificación del paciente a consultar: ")
                #Comprobación del tipo de dato
                try:
                    self.__ide = int(self.__ide)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("Escriba un número entero")
            #Selección de campos basado en la identificación de pacientes basado en el Numero_de_identificacion
            consultados = "Vacio"
            cursorObj.execute(f'SELECT * FROM Afiliados WHERE Numero_de_identificacion = {self.__ide} ')
            #Recolección de los datos en la tupla "consultados"
            consultados = cursorObj.fetchall() 
            if len(consultados) <= 0:
                print("No existe")
            elif len(consultados) > 0:
                consultados1 = consultados[0]
                #Impresión de la tupla correspondiente a la información paciente en forma de tabla
                print("------------------------------------------------------------")
                print("| No. Identificación     || {:<30} |\n| IdPlan                 || {:<30} |\n| Nombre                 || {:<30} |\n| Apellido               || {:<30} |\n| Dirección              || {:<1} |\n| telefono               || {:<30} |\n| correo                 || {:<30} |\n| ciudad de Residencia   || {:<30} |\n| Fecha de nacimiento    || {:<30} |\n| Fecha de Afiliación    || {:<30} |\n| Fecha de desafiliación || {:<30} |\n| Vacunado SI/NO         || {:<30} |".format(consultados1[0], consultados1[1], consultados1[2], consultados1[3], consultados1[4], consultados1[5], consultados1[6], consultados1[7], consultados1[8], consultados1[9], consultados1[10], consultados1[11]))
                print("------------------------------------------------------------")
                break

    #Función desafiliarPaciente: Con esta función se ingresa la fecha de desafiliación de un paciente
    def desafiliar(self, con):
        cursorObj = con.cursor()
        #Bucle de comprobación
        while True:
            #Recepción del número de identificación
            self.__ide = input("Ingrese el número de identificación del paciente a desafiliar: ")
            #Comprobación del tipo de dato
            try:
                self.__ide = int(self.__ide)
                break
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        #Seleccion de la columna Facha_De_Desafilaicion basado en el ide
        cursorObj.execute(f"SELECT Fecha_De_Desafiliacion FROM Afiliados WHERE Numero_De_Identificacion = {self.__ide}")
        #Obetencion en la tupla "desafiliado"
        desafiliado = cursorObj.fetchall()
        desafiliado = desafiliado[0]
        desafiliado = desafiliado[0]
        #Comprobacion de desafiliacion
        if desafiliado == "-":
            #Fecha Actual
            today = date.today()
            #Concatenación fecha actual
            self.__desafiliacion = str(today.day)+"/" + str(today.month)+"/"+str(today.year)
            #Inserción de la fecha concatenada en la base de datos basado en el Numero_de_identificacion, columna Fecha_de_desafiliacion
            cursorObj.execute(f'UPDATE Afiliados SET Fecha_De_Desafiliacion = ? WHERE Numero_de_identificacion = {self.__ide}',(self.__desafiliacion,))
            #Envio de la petición a la base de datos
            con.commit()
        else:
            print("El paciente ya está desafiliado")

    #Función vacunarAfiliado: Con esta función se actualiza el estado de vacunación de un afiliado en la tabla afiliado
    def vacunar(self, con):
        cursorObj = con.cursor()
        #Bucle de comprobación
        while True:
            #Ingreso de número de identificación del paciente a vacunar
            self.__ide = input("Ingrese el número de identificación del paciente a Vacunar: ")
            #Comprobación del tipo de dato
            try:
                self.__ide = int(self.__ide)
                #Ruptura del bucle de comprobación
                break
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        desafiliado = "vacio"
        #Selección de la fecha de desafiliacion del paciente a vacunar
        cursorObj.execute('SELECT Fecha_De_Desafiliacion FROM Afiliados WHERE Numero_De_Identificacion = ? AND Vacunado = "-"', (self.__ide,))
        #Recopilación en el array "desafiliado"
        desafiliado = cursorObj.fetchall()
        if len(desafiliado) <= 0:
            print("El paciente no existe o ya fue vacunado")

        else:
            #Acceso a la tupla del afiliado
            desafiliado1 = desafiliado[0]
            #Acceso al dato
            desafiliado2 = desafiliado1[0]
            #Condicional de comprobacíon de desafiliación
            
            if desafiliado2 != "-":
                #Mensaje de Advertencia
                print("El paciente está desafiliado y no será vacunado\n")
            else:
                #Actualización del estado de vacunación del afiliado basado en el Numero_de_identificacion, columna "Vacunado"
                self.__contadorVacunacion(con)
                self.__vacunado= "Si"
                cursorObj.execute('UPDATE Afiliados SET Vacunado = ? WHERE Numero_de_identificacion = ? ',(self.__vacunado,self.__ide))
                #Envio de la petición a la base de datos
                con.commit()

    #Función contadorVacunacion(self.__ide): Esta función actualiza la cantidad de vacunas utilizadas en la tabla Lotes
    def __contadorVacunacion(self, con):
        cursorObj = con.cursor()
        codLote = "vacio"
        #Select que obtiene los datos de la tabla de Citas
        cursorObj.execute('SELECT Codigo_De_Lote FROM Citas WHERE Numero_De_Identificacion=?', (self.__ide,))
        codLote = cursorObj.fetchall()
        #Verificación de existencia de datos en la tabla de citas
        if len(codLote) == 0:
            return False
        else:
            try:
                codLote = codLote[0]
                codLote1 = codLote[0]
            except IndexError:
                return False
            #Select que obtiene los datos de la tabla de Lotes
            cursorObj.execute(
                'SELECT Cantidad_Recibida, Cantidad_Usada FROM Lotes WHERE Codigo_De_Lote=?', (codLote1,))
            cantReUs = cursorObj.fetchall()
            cantReUs = cantReUs[0]
            cantReUs1 = cantReUs[0]
            cantReUs2 = cantReUs[1]
            #Verificación de vacunas existentes
            if cantReUs1 > 0:
                usado = cantReUs2+1
                #Actualización de la cantiadad de vacunas usada basada en Cantidad_Usada
                cursorObj.execute(
                    'UPDATE Lotes SET Cantidad_Usada=? WHERE Codigo_De_Lote=?', (usado, codLote1))
            con.commit()
            return True
"""