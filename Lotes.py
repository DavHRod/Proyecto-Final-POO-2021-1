#Importación de librerias a usar
#sqlite3: Es una libreria integrada en python para el manejo de bases de datos generalmente de tipo local
#utiliza comandos sql estandar y requiere el uso de un objeto tipo sql_connect
#Validate_email: Es la libreria que permite realizar la validación de un correo electrónico, su dominio y su existencia en el dominio señalado.
from sql import sql

class lote():
    
    def __init__(self, no_lote, fabrica, tipo_vac, cant_recibida, cant_usada, cant_asignada, no_dosis, temperatura, efectividad, proteccion, fecha_vencimiento, imagen):
        self.__no_lote=no_lote
        self.__fabrica=fabrica
        self.__tipo_vac=tipo_vac
        self.__cant_recibida=cant_recibida
        self.__cant_usada=cant_usada
        self.__cant_asignada=cant_asignada
        self.__no_dosis=no_dosis
        self.__temperatura=temperatura
        self.__efectividad=efectividad 
        self.__proteccion=proteccion
        self.__fecha_vencimiento=fecha_vencimiento
        self.__imagen=imagen
        self.__sql=sql()

    def set_no_lote(self, no_lote):
        self.__no_lote=no_lote
    def get_no_lote(self):
        return self.__no_lote
        
    def set_fabrica(self, fabrica):
            self.__fabrica=fabrica
    def get_fabrica(self):
        return self.__fabrica

    def set_tipo_vac(self, tipo_vac):
        self.__tipo_vac=tipo_vac
    def get_tipo_vac(self):
        return self.__tipo_vac

    def set_cant_recibida(self, cant_recibida):
        self.__cant_recibida=cant_recibida
    def get_cant_recibida(self):
        return self.__cant_recibida

    def set_cant_usada(self, cant_usada):
        self.__cant_usada=cant_usada
    def get_cant_usada(self):
        return self.__cant_usada

    def set_cant_asignada(self, cant_asignada):
        self.__cant_asignada=cant_asignada
    def get_cant_asignada(self):
        return self.__cant_asignada
    
    def set_no_dosis(self, no_dosis):
        self.__no_dosis=no_dosis
    def get_no_dosis(self):
        return self.__no_dosis

    def set_temperatura(self, temperatura):
        self.__temperatura=temperatura
    def get_temperatura(self):
        return self.__temperatura

    def set_efectividad(self, efectividad):
        self.__efectividad=efectividad
    def get_efectividad(self):
        return self.__efectividad

    def set_proteccion(self, proteccion):
        self.__proteccion=proteccion
    def get_proteccion(self):
        return self.__proteccion

    def set_fecha_vencimiento(self, fecha_vencimiento):
        self.__fecha_vencimiento=fecha_vencimiento
    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento  

    def set_imagen(self, imagen):
        self.__imagen=imagen
    def get_imagen(self):
        return self.__imagen

    def to_tuple(self):
        objt_tuple=(self.__no_lote,
        self.__fabrica,
        self.__tipo_vac,
        self.__cant_recibida,
        self.__cant_usada,
        self.__cant_asignada,
        self.__no_dosis,
        self.__temperatura,
        self.__efectividad, 
        self.__proteccion,
        self.__fecha_vencimiento,
        self.__imagen)
        return objt_tuple

    def set_lote(self):
            self.carga = self.to_tuple()
            self.__sql.guardar_tabla("Lotes",self.carga)
