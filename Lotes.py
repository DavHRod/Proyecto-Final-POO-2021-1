#Importación de librerias a usar
#sqlite3: Es una libreria integrada en python para el manejo de bases de datos generalmente de tipo local
#utiliza comandos sql estandar y requiere el uso de un objeto tipo sql_connect
import sqlite3
from sqlite3 import Error
#Validate_email: Es la libreria que permite realizar la validación de un correo electrónico, su dominio y su existencia en el dominio señalado.
#Requiere instalación de py3DNS mediante el comando pip install py3DNS, esto con permisos de administrador activos
from validate_email import validate_email
#datetime: Libreria integrada en python 3, permite el manejo y operación de variables tipo datetime,
#es usada para comprobacion y validacion de fechas bajo parametros propios
from datetime import date
from datetime import datetime

class lote():
    
    def __init__(self):
        self.noLote=""
        self.fabrica=""
        self.tipoVac=""
        self.cantidadRecibida=0
        self.cantidadUsada=0
        self.cantidadAsignada=0
        self.noDosis=0
        self.temperatura=0
        self.efectividad=0 
        self.protección=0
        self.fechaVencimiento=""
        self.imagen=""
        
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