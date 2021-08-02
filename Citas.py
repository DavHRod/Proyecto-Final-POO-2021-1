#--------- Importaciones de librerias a usar -----------------------------------------------------------------
from datetime import date 
from datetime import datetime #datetime: Libreria integrada en python 3, permite el manejo y operación de variables tipo datetime,
#es usada para comprobacion y validacion de fechas bajo parametros propios
from sql import sql #Modulo que maneja base de datos
from Afiliados import * #Importe módulo Afiliados

#-----DESDE AQUI MODULO DE CITAS-------------------------------------------------------------------------------------------------------------------------------------

class citas:
    def __init__(self, numero, plan, ide, ciudad, lote, fecha, hora): #Método principal de la clase
        self.__numero = numero
        self.__plan = plan
        self.__ide = ide
        self.__ciudad = ciudad
        self.__lote = lote
        self.__fecha = fecha
        self.__hora = hora
        self.__sql = sql()
    
    #Número de cita
    def set_numero(self,numero):
            self.__numero = numero
    def get_numero(self):
        return self.__numero

    #id plan
    def set_plan(self,id_plan):
        self.__plan = id_plan
    def get_id_plan(self):
        return self.__plan
    
    #id de afiliado
    def set_ide(self,ide):
        self.__ide = ide
    def get_ide(self):
        return self.__ide

    #Ciudad de la cita
    def set_ciudad(self,ciudad):
            self.__ciudad = ciudad
    def get_ciudad(self):
        return self.__ciudad

    #Lote de vacuna
    def set_lote(self,lote):
            self.__lote = lote
    def get_lote(self):
        return self.__lote

    #Fecha de la cita
    def set_fecha(self,fecha):
            self.__fecha = fecha
    def get_fecha(self):
        return self.__fecha

    #Hora de la cita
    def set_hora(self,hora):
            self.__hora = hora
    def get_hora(self):
        return self.__hora
    #tupla
    def to_tuple(self):
        objtupla = (self.__numero, 
        self.__plan, 
        self.__ide, 
        self.__ciudad, 
        self.__lote, 
        self.__fecha, 
        self.__hora)
        return objtupla

    def set_cita(self): #Método para guardar la información de la tabla Citas
        return self.__sql.guardar_tabla("Citas",self.to_tuple())
    
    def asignada(self): #Método para sumar el conteo de vacunas asiganadas
        lote_array = []
        lotes = self.__sql.cargar_instancia_lote(self.get_lote())
        for item in lotes[0]:
            lote_array.append(item)
        lote_array[4] = lote_array[4] + 1
        lote_tupla = tuple(lote_array)
        self.__sql.guardar_tabla("Lotes",lote_tupla) 