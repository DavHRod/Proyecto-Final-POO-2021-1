from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from MenuPlanes import *
from CrearPlan import *
from PyQt5 import QtWidgets 
from principal import Ui_principal

from afiliadoUi import Ui_afil_win
from menu_afiliado import Ui_afil_menu
from edit_afil import Ui_Dialog_edit

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
        self.a_ui = afiliado_win()
        self.a_menu = Ui_afil_menu()
        self.a_edit = afil_edit()
        self.a_menu.setupUi(self)
        self.a_menu.push_nuevo.clicked.connect(self.show_afil)
        self.a_menu.push_editar.clicked.connect(self.show_edit)
        self.a_menu.push_regresar.clicked.connect(self.show_principal)
    
    def show_principal(self):
        self.hide()

    def show_edit(self):
        self.hide()
        self.a_edit.show()
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


class afil_edit(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.a_edit = Ui_Dialog_edit()
        self.a_ui = afiliado_win()
        self.sql = sql()
        self.a_edit.setupUi(self)
        self.tupla = self.sql.cargar_tabla("Afiliados")
        self.fill_combo()
        self.a_edit.push_aceptar.clicked.connect(self.show_afil)
    
    def show_afil(self):
        self.close()
        self.a_ui.set_lines(self.tupla[self.a_edit.combo_carga.currentIndex()])
        self.a_ui.show()

    def back(self):
        self.close()
        self.a_menu.show()

    def fill_combo(self):
        index = 1
        for x in self.tupla:
            self.a_edit.combo_carga.insertItem(index, str(x[0]))
            index += 1
        

class afiliado_win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.sql = sql()
        self.a_ui = Ui_afil_win()
        self.a_ui.setupUi(self)
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))
        self.a_ui.push_guardar.clicked.connect(self.btn_guardar)
        self.a_ui.calendar_nacimiento.setMaximumDate(QDate.currentDate())
        self.only_int = QIntValidator()
        self.a_ui.line_ide.setValidator(self.only_int)
        self.a_ui.line_telefono.setValidator(self.only_int)
        self.a_ui.calendar_nacimiento.selectionChanged.connect(self.set_line_date)
    
    def set_line_date(self):
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))    
    
    def set_lines(self,carga):
        afil = afiliado(carga[0], carga[1], carga[2], carga[3], carga[4], carga[5], carga[6], carga[7], carga[8], carga[9], carga[10], carga[11], carga[12])
        self.a_ui.line_ide.setText(str(afil.get_ide()))
        self.a_ui.line_nombre.setText(afil.get_nombre())
        self.a_ui.line_apellido.setText(afil.get_apellido())
        self.a_ui.line_direccion.setText(afil.get_direccion())
        self.a_ui.line_telefono.setText(str(afil.get_telefono()))
        self.a_ui.line_correo.setText(afil.get_correo())
        self.a_ui.line_ciudad.setText(afil.get_ciudad())
        

    def btn_guardar(self):
        if self.a_ui.checkBox.isChecked():
            vacunado = "Si"
        else:
            vacunado = "-"
        datos = {"ide":self.a_ui.line_ide.text(), 
            "id_plan":"-", 
            "nombre":self.a_ui.line_nombre.text(), 
            "apellido":self.a_ui.line_apellido.text(),
            "direccion":self.a_ui.line_direccion.text(),
            "telefono":self.a_ui.line_telefono.text(),
            "correo":self.a_ui.line_correo.text(),
            "ciudad":self.a_ui.line_ciudad.text(),
            "nacimiento":self.a_ui.line_show_date.text(),
            "edad":"",
            "afiliacion":f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}",
            "desafiliacion":"-",
            "vacunado": vacunado}

        afilN = afiliado(datos["ide"],
            datos["id_plan"],
            datos["nombre"],
            datos["apellido"],
            datos["direccion"],
            datos["telefono"],
            datos["correo"],
            datos["ciudad"],
            datos["nacimiento"],
            datos["edad"],
            datos["afiliacion"],
            datos["desafiliacion"],
            datos["vacunado"])
        self.sql.guardar_tabla("Afiliados",afilN.to_tuple())


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
