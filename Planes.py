#--------- Importaciones de librerias a usar -----------------------------------------------------------------
import sqlite3
from sqlite3 import Error
from sql import sql #Modulo que maneja base de datos

#-----DESDE AQUI MODULO DE PLANES DE VACUNACION-------------------------------------------------------------------------------------------------------
##Función crearPlan(con): Permite generar un nuevo plan de vacunación y almacenar la información en la tabla de Planes

class plan:
    def __init__(self, id_plan,edad_min,edad_max,fecha_inicio): #Método principal de la clase
        self.__id_plan = id_plan
        self.__edad_min = edad_min
        self.__edad_max = edad_max
        self.__fecha_inicio = fecha_inicio
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
    def get_edad_max(self):
        return self.__edad_max

    def set_plan(self):
        self.__sql.guardar_tabla("Planes", self.to_tuple())
        

    #tupla
    def to_tuple(self):
        obj_tuple = (self.__id_plan,
            self.__edad_min, 
            self.__edad_max, 
            self.__fecha_inicio, 
            )
        return obj_tuple
    
    def calcular(self): #Método para asignar un plan a los afiliados exixstentes
        self.afiliados = self.__sql.cargar_tabla("Afiliados")
        if len(self.afiliados) > 0:
            self.rango = range(int(self.get_edad_min()),int(self.get_edad_max()) + 1)
            for x in self.afiliados:
                if int(x[9]) in self.rango and x[11] == "-" and x[12] == "-":
                    self.afiliado_array = []
                    for y in x:
                        self.afiliado_array.append(y)
                    self.afiliado_array[1] = self.get_id_plan()
                    self.afiliado_array = tuple(self.afiliado_array)
                    self.__sql.guardar_tabla("Afiliados",self.afiliado_array)
