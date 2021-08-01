from datetime import datetime
from datetime import date
from sql import sql
from Afiliados import *
class citas:
    def __init__(self, numero, plan, ide, ciudad, lote, fecha, hora):
        self.__numero = numero
        self.__plan = plan
        self.__ide = ide
        self.__ciudad = ciudad
        self.__lote = lote
        self.__fecha = fecha
        self.__hora = hora
        self.__sql = sql()
    
    def set_numero(self,numero):
            self.__numero = numero
    def get_numero(self):
        return self.__numero

    def set_plan(self,id_plan):
        self.__plan = id_plan
    def get_id_plan(self):
        return self.__plan
    
    def set_ide(self,ide):
        self.__ide = ide
    def get_ide(self):
        return self.__ide

    def set_ciudad(self,ciudad):
            self.__ciudad = ciudad
    def get_ciudad(self):
        return self.__ciudad

    def set_lote(self,lote):
            self.__lote = lote
    def get_lote(self):
        return self.__lote

    def set_fecha(self,fecha):
            self.__fecha = fecha
    def get_fecha(self):
        return self.__fecha

    def set_hora(self,hora):
            self.__hora = hora
    def get_hora(self):
        return self.__hora
    
    def to_tuple(self):
        objtupla = (self.__numero, self.__plan, self.__ide, self.__ciudad, self.__lote, self.__fecha, self.__hora)
        return objtupla

    def set_cita(self):
        carga = (self.__numero, self.__plan, self.__ide, self.__ciudad, self.__lote, self.__fecha, self.__hora)
        return self.__sql.guardar_tabla("Citas",carga)
                
        
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