from Afiliados import *

def sql_connection():
    try:
        #Conexión con la base de datos
        con = sqlite3.connect('ProgramaDeVacunacion.db')
        return con
    except Error:
        print(Error)
        
con=sql_connection()
afil=afiliado()
#afil.afiliar(con)
afil.vacunar(con)
"""
from datetime import date
from datetime import datetime

def calcEdad(fechaNacimiento,fechaActual):
        fechaNacimiento = datetime.strptime(fechaNacimiento, "%d/%m/%Y")
        edad = fechaNacimiento - fechaActual
        if fechaNacimiento >= fechaActual:
            return False
        else:
            return True
naci="05/05/2022"
print (calcEdad(naci,datetime.today()))
"""