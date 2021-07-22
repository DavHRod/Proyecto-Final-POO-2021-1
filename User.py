from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from Afiliados import *
from PyQt5 import QtWidgets 
from principal import Ui_principal
from afiliadoUi import Ui_afil_win
from menu_afiliado import Ui_afil_menu
import sys
class principal_win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.afil_menu = afil_menu()
        self.ui = Ui_principal()
        self.ui.setupUi(self)
        self.ui.push_afiliados.clicked.connect(self.show_afil_menu)

    def show_afil_menu(self):
        self.hide()
        self.afil_menu.show()

class afil_menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.a_ui = afiliado_win()
        self.a_menu = Ui_afil_menu()
        self.a_menu.setupUi(self)
        self.a_menu.push_nuevo.clicked.connect(self.show_afil)

    def show_afil(self):
        self.hide()
        self.a_ui.show()

class afiliado_win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.a_ui = Ui_afil_win()
        self.a_ui.setupUi(self)
        self.set_lines()
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))
        self.a_ui.push_guardar.clicked.connect(self.btn_guardar)
        self.a_ui.calendar_nacimiento.setMaximumDate(QDate.currentDate())
        self.only_int = QIntValidator()
        self.a_ui.line_ide.setValidator(self.only_int)
        self.a_ui.line_telefono.setValidator(self.only_int)
        self.a_ui.calendar_nacimiento.selectionChanged.connect(self.set_line_date)
    
    def set_line_date(self):
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))    
    
    def set_lines(self):
        afil = afiliado("", "", "", "", "", "", "", "", f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}", "", "", "", "")
        self.a_ui.line_ide.setText(afil.get_ide())
        self.a_ui.line_apellido.setText(afil.get_apellido())
        self.a_ui.line_direccion.setText(afil.get_direccion())
        self.a_ui.line_telefono.setText(afil.get_telefono())
        self.a_ui.line_correo.setText(afil.get_correo())
        self.a_ui.line_ciudad.setText(afil.get_ciudad())
        

    def btn_guardar(self):
        if self.a_ui.checkBox.isChecked():
            vacunado = "Si"
        else:
            vacunado = "-"
        datos = {"ide":int(self.a_ui.line_ide.text()), 
            "id_plan":"-", 
            "nombre":self.a_ui.line_nombre.text(), 
            "apellido":self.a_ui.line_apellido.text(),
            "direccion":self.a_ui.line_direccion.text(),
            "telefono":int(self.a_ui.line_telefono.text()),
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
        print (afilN.to_tuple())
