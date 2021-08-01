import sqlite3
from sqlite3 import Error
from validate_email import validate_email
#datetime: Libreria integrada en python 3, permite el manejo y operación de variables tipo datetime,
#es usada para comprobacion y validacion de fechas bajo parametros propios
from sql import sql
#-----DESDE AQUI MODULO DE PLANES DE VACUNACION-------------------------------------------------------------------------------------------------------
##Función crearPlan(con): Permite generar un nuevo plan de vacunación y almacenar la información en la tabla de Planes

class plan:
    def __init__(self, id_plan,fecha_inicio,fecha_fin,edad_min,edad_max):
        self.__id_plan = id_plan
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__edad_min = edad_min
        self.__edad_max = edad_max
        self.__sql = sql()

    #id plan
    def set_id_plan(self,id_plan):
        self.__id_plan = id_plan

    def get_id_plan(self):
        return self.__id_plan

    #fecha inicio
    def set_fecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_fecha_inicio(self):
        return self.__fecha_inicio

    #fecha fin
    def set_fecha_fin(self,fecha_fin):
        self.__fecha_fin = fecha_fin

    def get_fecha_fin(self):
        return self.__fecha_fin

    #edad_min
    def set_edad_min(self,edad_min):
        self.__edad_min = edad_min

    def get_edad_min(self):
        return self.__edad_min

    #edad_max
    def set_edad_max(self,edad_max):
        self.__edad_max = edad_max

    def get_fecha_fin(self):
        return self.__edad_max

    def set_plan(self):
        
        self.__sql.guardar_tabla("Planes", self.to_tuple())
        

    #tupla
    def to_tuple(self):
        obj_tuple = (self.__id_plan, 
            self.__fecha_inicio, 
            self.__fecha_fin, 
            self.__edad_min, 
            self.__edad_max)
        return obj_tuple



        """
        
    def crear(self,con):
        cursorObj = con.cursor()

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
            error = False
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

            try:
                cursorObj.execute("INSERT INTO Planes VALUES(?,?,?,?,?)",datosPlanes)
                con.commit()
                self.calcular(con)
            except: 
                print ("El Plan ya existe")
            
    def consultar(self,con):
        cursorObj = con.cursor()
        #Bucle de comprobación
        while True:
            while True:
                #Recepcion del número de identificación a consultar
                self.idPlan=input("Ingrese el número de ID del plan a consultar: ")
                #Comprobación del tipo de dato
                try:
                    self.idPlan = int(self.idPlan)
                    #Ruptura del bucle de comprobación
                    break
                except ValueError:
                    #Mensaje en pantalla de un error al digitar
                    print("El número debe ser digito")
            cursorObj.execute('SELECT * FROM Planes WHERE ID = ? ',(self.idPlan,))
            #Recolección de los datos en la tupla "consultados"
            planes=cursorObj.fetchall()
            if len(planes) <= 0:
                print("El plan no existe")
            else:
                planes1=planes[0]
                #Impresión de la tupla correspondiente a la información paciente en forma de tabla
                print("---------------------------------------------")
                print("| Consecutivo Plan  || {:<20} |\n| Edad Mínima       || {:<20} |\n| Edad Máxima       || {:<20} |\n| Fecha de Inicio   || {:<20} |\n| Fecha de Fin      || {:<20} |".format(planes1[0],planes1[1],planes1[2],planes1[3],planes1[4]))
                print("---------------------------------------------")
            break


    #Función calcularPlan: Función que sirve para asignar un plan de vacunación a un afiliado de acuerdo a los datos registrados en la tabla de afiliados
    def calcular(self,con):
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
                   
    def comprobarFecha(self,fechaDada):
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


    def cerrar(self,con):
        cursorObj = con.cursor()
    #Ingreso de un id para asignarlo a un plan
        self.idPlan=input("Ingrese el consecutivo del plan de vacunación: ")
        longMax = 20
        longId = len(self.ide)
            
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
            self.fechaFin=str(day)+"/"+str(month)+"/"+str(year)
            fechaFinComprobacion = datetime.strptime(self.fechaFin, '%d/%m/%Y')
            fechaActual = datetime.today()
            cursorObj.execute('SELECT Fecha_Inicio FROM Planes WHERE ID=?',(idPlan,))
            minMax=cursorObj.fetchall()
            fechaIn=minMax[0]
            fechaIn1=fechaIn[0]
            fechaInComprobacion = datetime.strptime(fechaIn1, '%d/%m/%Y')
            fechaActual = datetime.today()
            if fechaInComprobacion <= fechaFinComprobacion or fechaFinComprobacion >= fechaActual:
                break
            else:
                print("Fecha Invalida")
        cursorObj.execute('UPDATE Planes SET Fecha_Fin=? WHERE ID=?',(fechaFin,idPlan))
        con.commit()
    """
