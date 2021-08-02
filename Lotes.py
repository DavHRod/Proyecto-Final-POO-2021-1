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
"""
    #Función crearLote(con):
    def crear(self, con):
        cursorObj = con.cursor()
        #Ingreso de No. de lote y verificación de longitud de la entrada
        while True:
            self.noLote=input("Ingrese el número de lote: ")
            longitud=10
            longCod=len(self.noLote)
            if longCod<=longitud:
                self.noLote=self.noLote.rjust(longitud," ")
                break
            else:
                print("Máximo escriba 10 digitos")
        
        #Seleccion Del Fabricante De La Vacuna
        while True:
            #Impresión del listado se fabricantes de vacunas
            print('''1. Sinovac\n2. Pfizer\n3. Moderna\n4. Sputnik\n5. AstraZeneca\n6. Sinopharm\n7. Covaxim''')
            try:
                self.fabricante=int(input("\nSeleccione un Fabricante: "))
                if self.fabricante > 0 and self.fabricante < 8:
                    break
                else:
                    print("Fabricante Invalido")
            except:
                ("Debe ser Numero")
        self.fabricante=self.fabricantes(self.fabricante)
        #Ingreso de la cantidad de vacunas recibidas
        while True:
            self.cantidadRecibida=input("Ingrese la cantidad recibida: ")
            try:
                self.cantidadRecibida = int(self.cantidadRecibida)
                break
            except ValueError:
                #Mensaje en pantalla de un error al digitar
                print("Escriba un número entero")
        #Asignacion de la cantidad Asignada
        self.cantidadAsignada=0
        self.cantidadUsada=0
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
            self.fechaVencimiento=day+"/"+month+"/"+year
            if self.comprobarFecha(self.fechaVencimiento) == "Mayor":
                break
        #Imagen: proximamente
        self.imagen="Aún no"
        self.fabrica=self.fabricante[0]
        self.tipoVac=self.fabricante[1]
        self.noDosis=self.fabricante[2]
        self.temperatura=self.fabricante[3]
        self.efectividad=self.fabricante[4]
        self.protección=self.fabricante[5]
        datosLotes=(self.noLote,self.fabrica,self.tipoVac,self.cantidadRecibida,self.cantidadUsada,self.cantidadAsignada,self.noDosis,self.temperatura,self.efectividad,self.protección,self.fechaVencimiento,self.imagen)
        #Insercion de los datos a la tabla de Lotes, Nueva Fila
        try:
            cursorObj.execute("INSERT INTO Lotes VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",datosLotes)
            #Envio de la peticion a la base de datos
            con.commit()
        except:
            print("El Lote ya existe")
        #Llamado del menú de gestión de lotes 
        #menuLotes()

    #Función fabricantes(fabricante): De acuerdo a la elección de fabricante retorna la información del la vacuna correspondiente al fabricante
    def fabricantes(self, fabricante):
        tiposFabricantes = {1:"Sinovac",2:"Pfizer",3:"Moderna",4:"SputnikV",5:"AstraZeneca",6:"Sinopharm",7:"Covaxim"}
        if tiposFabricantes[fabricante] == "Sinovac":
            return ("Sinovac","Virus Desactivado",2,"2°","50%","No se sabe")
        elif tiposFabricantes[fabricante] == "Pfizer":
            return ("Pfizer","ARN",2,"-80°","95%","No se sabe")
        elif tiposFabricantes[fabricante] == "Moderna":
            return ("Moderna","ARN",2,"-25°","94.5%","90 Dias")
        elif tiposFabricantes[fabricante] == "SputnikV":
            return ("SputnikV","Vector Viral",2,"-18°","92%","150 Dias")
        elif tiposFabricantes[fabricante] == "AstraZeneca":
            return ("AstraZeneca","Vector Viral",2,"2°","62%","No se sabe")
        elif tiposFabricantes[fabricante] == "Sinopharm":
            return ("Sinopharm","Vector Viral",2,"2°","79.3%","No se sabe")
        elif tiposFabricantes[fabricante] == "Covaxin":
            return ("Covaxim","Virus Desactivado",2,"2°","78%","No se sabe")

    #Función consultarLote(con):Esta función permite visualizar la información contenida en la tabla de lotes de acuerdo a un código de lote
    def consultar(self, con):
        cursorObj = con.cursor()
        #Recepcion del Numero del lote a consultar
        self.noLote=(input("Ingrese el número de lote a consultar: "))
        self.noLote=self.noLote.ljust(10)
        self.noLote=self.noLote[:10]
        lote="Vacio"
        #Seleccion de datos basado en el Numero_De_Lote
        cursorObj.execute('SELECT * FROM Lotes WHERE Codigo_De_Lote = ?',(self.noLote,))
        #Recoleccion de los datos en la tupla "consultados"
        lote=cursorObj.fetchall()
        if len(lote) <= 0:
            print("El Lote No Existe")
        else:    
            #Impresion de la tupla correspondiente al lote
            lote1=lote[0]
            print("-------------------------------------------------------------------")
            print("| Código Lote                   || {:<30} |\n| Fabricante                    || {:<30} |\n| Tipo de Vacuna                || {:<30} |\n| Cantidad Recibida             || {:<30} |\n| Cantidad Asignada             || {:<30} |\n| Cantidad Usada                || {:<30} |\n| Dosis Necesarias              || {:<30} |\n| Temperatura de Almacenamiento || {:<30} |\n| Efectividad Identificada      || {:<30} |\n| Tiempo de Protección          || {:<30} |\n| Fecha de Vencimiento          || {:<30} |\n| Imágen                        || {:<30} |".format(lote1[0],lote1[1],lote1[2],lote1[3],lote1[4],lote1[5],lote1[6],lote1[7],lote1[8],lote1[9],lote1[10],lote1[11]))
            print("-------------------------------------------------------------------")
        #Llamado del menú de gestión de lotes
        #menuLotes()

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
"""