import sqlite3
from sqlite3 import Error
#datetime: Libreria integrada en python 3, permite el manejo y operación de variables tipo datetime,
#es usada para comprobacion y validacion de fechas bajo parametros propios
from datetime import date
from datetime import datetime
#-----DESDE AQUI MODULO DE PLANES DE VACUNACION-------------------------------------------------------------------------------------------------------
##Función crearPlan(con): Permite generar un nuevo plan de vacunación y almacenar la información en la tabla de Planes

class plan:
    def __init__(self):
        self.idPlan = 0
        self.fechaInicio = ""
        self.fechaFin = ""
        self.edadMin = 0
        self.edadMax = 0
        self.confirmacion = ""

    def fecha(self,fechaNacimiento):
        fechaNacimiento=datetime.strptime(fechaNacimiento, "%d/%m/%Y")
        if fechaNacimiento >= datetime.today():
            return True
        else:
            return False
    
    #Función crearPlan(con): Permite generar un nuevo plan de vacunación y almacenar la información en la tabla de Planes
    def crear(self,con):
        cursorObj = con.cursor()
        #Ingreso de un id para asignarlo a un plan
        self.idPlan=input("CONSECUTIVO del plan de vacunación: ")
        self.idPlan=self.idPlan.ljust(2)
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
            self.fechaInicio = day+"/"+month+"/"+year
            if self.fecha(self.fechaInicio):
                break
            else: 
                print("Fecha Invalida")
        #Concatenación de la fecha de fin del plan de vacunación
        self.fechaFin = "24/05/2121"
        error=False
        while True:
            while True:
                try:
                    self.edadMin=int(input("Ingrese la edad mínima para clasificar a este plan: "))
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
                if self.edadMin >= minima-1 and  self.edadMin <= maxima:
                    error=True
                    print("Edad Presenta Cruce")
                    break
                else:
                    error=False
                    intervaloActual += 1
                if error == False:
                    break
            error=False
            while True:
                while True:
                    try:
                        self.edadMax=int(input("Ingrese la edad máxima para clasificar a este plan: "))
                        if self.edadMin < self.edadMax:
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
                    if self.edadMax >= menor and self.edadMax <= mayor :
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
                            if self.edadMin <= minima <= self.edadMax or self.edadMin <= maxima <= self.edadMax:
                                print ("El Intervalo presenta cruce con otro plan")
                                error = True
                                break
                            intervaloActual += 1
                    if error == False:
                        break
                    
                datosPlanes=(self.idPlan,self.edadMin,self.edadMax,self.fechaInicio,self.fechaFin)
                cursorObj.execute("INSERT INTO Planes VALUES(?,?,?,?,?)",datosPlanes)
                con.commit()

    #Función cierrePlanVacunacion(con): Esta función sirve para actualizar la fecha de terminación de un plan de vacunación 
    def cierre(self,con):
        cursorObj = con.cursor()
        #Ingreso de un id para asignarlo a un plan
        self.idPlan=input("Ingrese el consecutivo del plan de vacunación: ")
        self.idPlan=self.idPlan.ljust(2)
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
                year=year.rjust(4)
                try:
                    int(year)
                    break
                    #Concatenación de la fecha de cierre del plan de vacunación
                except:
                    print("Debe Ser Un Numero")
            self.fechaFin=day+"/"+month+"/"+year
            fechaFinComprobacion = datetime.strptime(self.fechaFin, '%d/%m/%Y')
            fechaActual = datetime.today()
            cursorObj.execute('SELECT Fecha_Inicio FROM Planes WHERE ID=?',(self.idPlan,))
            minMax=cursorObj.fetchall()
            fechaIn=minMax[0]
            fechaIn1=fechaIn[0]
            fechaInComprobacion = datetime.strptime(fechaIn1, '%d/%m/%Y')
            fechaActual = datetime.today()
            if fechaInComprobacion <= fechaFinComprobacion or fechaFinComprobacion >= fechaActual:
                break
            else:
                print("Fecha Invalida")
        cursorObj.execute('UPDATE Planes SET Fecha_Fin=? WHERE ID=?',(self.fechaFin,self.idPlan))
        con.commit()

    #Funcion de consulta de planes
    def consultar(self,con):
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
        #Impresion de la tupla correspondiente al plan
        planes1=planes[0]
        print("---------------------------------------------")
        print("| Consecutivo Plan  || {:<20} |\n| Edad Mínima       || {:<20} |\n| Edad Máxima       || {:<20} |\n| Fecha de Inicio   || {:<20} |\n| Fecha de Fin      || {:<20} |".format(planes1[0],planes1[1],planes1[2],planes1[3],planes1[4]))
        print("---------------------------------------------")
        

    #Función calcularPlan(con): Función que sirve para asignar un plan de vacunación a un afiliado de acuerdo a los datos registrados en la tabla de afiliados
    def calcular(self,con):
        self.confirmacion=input("""Este modulo asignará un numero de plan con respecto a los planes vigentes
        ¿Desea Ejecutar? Y/N\n""")
        self.confirmacion=self.confirmacion.upper()
        if self.confirmacion == "Y":
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
            menuPlanes()
            print("Calculado")
        else:
            menuPlanes()