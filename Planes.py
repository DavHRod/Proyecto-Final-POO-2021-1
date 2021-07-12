import sqlite3
from sqlite3 import Error
from validate_email import validate_email
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
        self.confirmación = ""

    def crear(self,con):
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
            planes1=planes[0]
            #Impresión de la tupla correspondiente a la información paciente en forma de tabla
            print("------------------------------------------------------------")
            print("| Consecutivo Plan     || {:<20} |\n| Edad Mínima       || {:<20} |\n| Fecha de Inicio   || {:<20} |\n| Fecha de Fin      || {:<20} |".format(planes1[0],planes1[1],planes1[2],planes1[3],planes1[4]))
            print("------------------------------------------------------------")
            break


    #Función calcularPlan: Función que sirve para asignar un plan de vacunación a un afiliado de acuerdo a los datos registrados en la tabla de afiliados
    def calcular(self,con):
        self.confirmacion=input("""Este modulo asignará un numero de plan con respecto a los planes vigentes
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
        
        """
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
