#--------- Importaciones de librerias a usar -----------------------------------------------------------------
from validate_email import validate_email#Validate_email: Es la libreria que permite realizar la validación de un correo electrónico, su dominio y su existencia en el dominio señalado.
#Requiere instalación de py3DNS mediante el comando pip install py3DNS, esto con permisos de administrador activos

from datetime import date
from datetime import datetime #datetime: Libreria integrada en python 3, permite el manejo y operación de variables tipo datetime,
#es usada para comprobacion y validacion de fechas bajo parametros propios

from Planes import * #Importe módulo Planes
from sql import * #Modulo que maneja base de datos

#-----DESDE AQUI MODULO DE AFILIADOS-------------------------------------------------------------------------------------------------------------------------------------

class afiliado:
    def __init__(self,ide,id_plan,nombre,apellido,direccion,telefono,correo,ciudad,nacimiento,edad,afiliacion,desafiliacion,vacunado): #Método principal de la clase
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

    #id de afiliado
    def set_ide(self,ide):
        self.__ide = ide
    def get_ide(self):
        return self.__ide

    #id plan
    def set_id_plan(self,id_plan):
        self.__id_plan = id_plan
    def get_id_plan(self):
        return self.__id_plan

    #Nombre del afiliado
    def set_nombre(self,nombre):
            self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre

    #Apellido del afiliado
    def set_apellido(self,apellido):
            self.__apellido = apellido
    def get_apellido(self):
        return self.__apellido

    #Dirección del afiliado
    def set_direccion(self,direccion):
            self.__direccion = direccion
    def get_direccion(self):
        return self.__direccion

    #Teléfono del afiliado
    def set_telefono(self,telefono):
            self.__telefono = telefono
    def get_telefono(self):
        return self.__telefono

    #Correo del afiliado
    def set_correo(self,correo):
            self.__correo = correo
    def get_correo(self):
        return self.__correo

    #Ciudad de residencia
    def set_ciudad(self,ciudad):
            self.__ciudad = ciudad
    def get_ciudad(self):
        return self.__ciudad

    #Fecha de nacimiento del afiliado
    def set_nacimiento(self,nacimiento):
            self.__nacimiento = nacimiento
    def get_nacimiento(self):
        return self.__nacimiento

    #Edad del paciente (la calcula automáticamente)
    def set_edad(self,edad):
            self.__edad = edad
    def get_edad(self):
        return self.__edad

    #Fecha de afiliación
    def set_afiliacion(self,afiliacion):
            self.__afiliacion = afiliacion
    def get_afiliacion(self):
        return self.__afiliacion

    #Fecha de desafiliación
    def set_desafiliacion(self,desafiliacion):
            self.__desafiliacion = desafiliacion
    def get_desafiliacion(self):
        return self.__desafiliacion
 
    #Estado de vacunación
    def set_vacunado(self,vacunado):
            self.__vacunado = vacunado
    def get_vacunado(self):
        return self.__vacunado

    def __calc_edad(self, fechaNacimiento): #Método para calcular la edad del paciente según su fecha de nacimiento
        fechaNacimiento = datetime.strptime(fechaNacimiento, "%d/%m/%Y")
        actual=datetime.today().strftime("%d/%m/%Y")
        actual=datetime.strptime(actual,"%d/%m/%Y")
        self.__edad = actual.year - fechaNacimiento.year
        self.__edad -= ((actual.month, actual.day) <(fechaNacimiento.month, fechaNacimiento.day))

    def set_afiliado(self): #Método para guardar la información de los afiliados
            self.carga = self.to_tuple()
            self.__sql.guardar_tabla("Afiliados",self.carga)

    #tupla
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

    def vacunar(self): #Método para descontar las vacunas de los lotes existentes
        lote_array = []
        citas = self.__sql.cargar_tabla("Citas")
        for x in citas:
            if str(x[2]) == self.get_ide():
                self.lote_id = x[4]
                break
        lotes = self.__sql.cargar_instancia_lote(self.lote_id)
        for item in lotes[0]:
            lote_array.append(item)
        lote_array[5] = lote_array[5] + 1
        lote_tupla = tuple(lote_array)
        self.__sql.guardar_tabla("Lotes",lote_tupla)

    def calcular_plan(self): #Método para calcular un plan a un nuevo afiliado (si existen planes)
        self.planes = self.__sql.cargar_tabla("Planes")
        if len(self.planes) > 0:
            for x in self.planes:
                rango = range(x[1], x[2])
                if self.get_edad() in rango:
                    self.set_id_plan(x[0])
                    break
