from Planes import *

def sql_connection():
    try:
        #Conexión con la base de datos
        con = sqlite3.connect('ProgramaDeVacunacion.db')
        return con
    except Error:
        print(Error)

con=sql_connection()
plan=plan()
plan.cierre(con)