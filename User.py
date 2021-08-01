from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from MenuPlanes import *
from CrearPlan import *
from PyQt5 import QtWidgets 
from principal import Ui_principal
from sql import sql
import sys
class principal_win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_principal()
        self.ui.setupUi(self)
        self.ui.push_planes.clicked.connect(self.show_planes_menu)


    def show_planes_menu(self):
        self.hide()
        self.planes_menu = planes_menu()
        self.planes_menu.show()

class planes_menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_menuplanes = Ui_MenuPlanesWindow()
        self.ui_menuplanes.setupUi(self)
        self.ui_menuplanes.pushButton_CrearPlan.clicked.connect(self.show_plan)
        self.ui_menuplanes.pushButton_Regresar.clicked.connect(self.show_principal)

    def show_plan(self):
        self.hide()
        self.planes_crear = planes_crear()
        self.planes_crear.show()
    
    def show_principal(self):
        self.hide()
        self.principal = principal_win()
        self.principal.show()


class planes_crear(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_crearPlan = Ui_CrearPlanWindow()
        self.ui_crearPlan.setupUi(self)
        self.set_line_date()
        self.ui_crearPlan.calendar_fechaInicio.setMinimumDate(QDate.currentDate())
        self.ui_crearPlan.calendar_fechaInicio.selectionChanged.connect(self.set_line_date)
        self.ui_crearPlan.pushButton_Regresar.clicked.connect(self.show_menuplanes)
        self.ui_crearPlan.pushButton_Guardar.clicked.connect(self.btn_guardar)
        self.sql = sql()


    def show_menuplanes(self):
        self.hide()
        self.ui_crearplanes = planes_crear()
        self.planes_menu = planes_menu()
        self.planes_menu.show()

    def set_line_date(self):
        self.ui_crearPlan.lineEdit_FechaInicio.setText(self.ui_crearPlan.calendar_fechaInicio.selectedDate().toString("dd/MM/yyyy"))


    def btn_guardar(self):
        self.tabla = self.sql.cargar_tabla("Planes")
        id = len(self.tabla) + 1

        datos = { 
            "ID": id,
            "Edad_Max":int(self.ui_crearPlan.spinBox_Max.text()),
            "Edad_Min":int(self.ui_crearPlan.spinBox_Min.text()),
            "Fecha_Inicio":self.ui_crearPlan.lineEdit_FechaInicio.text(),
            "Fecha_Fin":str("05/07/3000"),
            }

        PlanN = plan(datos["ID"],
            datos["Edad_Max"],
            datos["Edad_Min"],
            datos["Fecha_Inicio"],
            datos["Fecha_Fin"],
            )

        PlanN.set_plan()