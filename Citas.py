from datetime import datetime
from datetime import date
from Afiliados import *
class citas:
    def __init__(self):
        self.__numero = 0
        self.__plan = 0
        self.__ide = 0
        self.__ciudad = ""
        self.__fecha = ""
        self.__hora = ""
    def calcular(self, con):
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
            if self.comprobarFecha(fechaInicio) == "Mayor":
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
                self.calcular(con)
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
        for plan in range(1,len(planes)+1):
            cursorObj.execute('SELECT Numero_De_Identificacion, Ciudad_De_Residencia, ID_Plan FROM Afiliados WHERE ID_Plan = ? AND Fecha_De_Desafiliacion = "-"',(plan,))
            #Recopilacion en la tupla "afiliados"
            afiliados=cursorObj.fetchall()
            #Fecha Inicio Plan
            cursorObj.execute("SELECT Fecha_Inicio FROM Planes WHERE ID = ? ",(plan,))
            fecha_plan=cursorObj.fetchall()
            fecha_plan = fecha_plan[0]
            fecha_plan = fecha_plan[0]
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
                    return 0
                lote=int(vacunas[0])
                recibidas=int(vacunas[1])
                asignadas=int(vacunas[2])
                usadas=int(vacunas[3])
                existentes = recibidas - usadas
                horaCitaActual=horaCitas[afiliado]
                horaCitaActual=str(horaCitaActual[0])+":"+str(horaCitaActual[1])
                afiliado_actual=afiliados[afiliado]
                if asignadas != existentes:
                    cursorObj.execute("UPDATE Lotes SET Cantidad_Asignada = ? WHERE Codigo_De_Lote = ?",(asignadas + 1,lote))
                    con.commit()
                else:
                    loteActual += 1
                self.__numero = secuencial
                self.__plan = afiliado_actual[2]
                self.__ide = afiliado_actual[0]
                self.__ciudad = afiliado_actual[1]
                self.__fecha = fecha_plan
                self.__hora = horaCitaActual
                nueva_cita=(self.__numero,self.__plan,self.__ide,self.__ciudad,lote,self.__fecha,self.__hora)
                try:
                    cursorObj.execute("INSERT INTO Citas Values (?,?,?,?,?,?,?)",nueva_cita)
                    con.commit()
                    #Aumento del secuencial de citas
                    secuencial += 1
                    #Aumento para cambio de afiliado
                    afiliado += 1
                except:
                    #Aumento del secuencial de citas
                    secuencial += 1
                    #Aumento para cambio de afiliado
                    afiliado += 1
                
        
    #Función consultarProgramaIndividual(): Esta función permite al usuario visualizar los datos de la cita
    #a partir de un número de identificación
    def consultaIndividual(self, con):
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

    #Función consultarProgramaGeneral(): Esta función permite al usuario visualizar todos los datos de la tabla citas
    def consultaGeneral(self, con):
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

    def comprobarFecha(self, fechaDada):
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