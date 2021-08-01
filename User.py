#PtQt5 es una libreria externa de python que permite la creación de interfaces graficas para programas en lenguaje python
#
from PyQt5.QtCore import QDate, QRect, QRegularExpression
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from principal import Ui_principal

from Afiliados import *
from afiliadoUi import Ui_afil_win
from menu_afiliado import Ui_afil_menu
from edit_afil import Ui_Dialog_edit
from view_afiliado import Ui_view_afiliado
from vista_general import Ui_ver_todo

from Citas import citas
from menu_citas import Ui_menu_citas
from citasUi import Ui_citas


from sql import sql
import sys

class principal_win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_principal()
        self.ui.setupUi(self)
        self.sql = sql()
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
        self.afiliados = self.sql.cargar_tabla("Afiliados")
        self.lotes = self.sql.cargar_tabla("Lotes")
        self.planes = self.sql.cargar_tabla("Planes")
        self.citas = self.sql.cargar_tabla("Citas")
        if len(self.afiliados) <= 0 or len(self.lotes) <= 0 or len(self.planes) <= 0:
            self.ui.push_citas.setEnabled(False)
            self.ui.push_citas.setStyleSheet(self.style_disable)
        else:
            self.ui.push_citas.setEnabled(True)
        self.ui.push_afiliados.clicked.connect(self.show_afil_menu)
        self.ui.push_citas.clicked.connect(self.show_citas_menu)
        
    def show_afil_menu(self):
        self.hide()
        self.afil_menu = afil_menu(self.afiliados, self.style_disable)
        self.afil_menu.show()
    
    def show_citas_menu(self):
        self.hide()
        self.citas_menu = citas_menu(self.afiliados,self.lotes, self.planes, self.citas, self.style_disable)
        self.citas_menu.show()

class afil_menu(QtWidgets.QMainWindow):
    def __init__(self,carga, style):
        super().__init__()
        self.style_disable = style
        self.a_menu = Ui_afil_menu()
        self.a_menu.setupUi(self)
        self.tupla = carga
        if len(self.tupla) == 0:
            self.a_menu.push_ver.setDisabled(True)
            self.a_menu.push_ver.setStyleSheet(self.style_disable)
            self.a_menu.push_editar.setDisabled(True)
            self.a_menu.push_editar.setStyleSheet(self.style_disable)
            self.a_menu.push_consultar.setDisabled(True)
            self.a_menu.push_consultar.setStyleSheet(self.style_disable)
        self.a_menu.push_nuevo.clicked.connect(self.show_afil)
        self.a_menu.push_editar.clicked.connect(self.show_edit)
        self.a_menu.push_consultar.clicked.connect(self.show_consulta)
        self.a_menu.push_ver.clicked.connect(self.show_ver)
        self.a_menu.push_regresar.clicked.connect(self.show_principal)
    
    def show_afil(self):
        self.hide()
        self.a_ui = afiliado_win(self.tupla, self.style_disable)
        self.a_ui.show()

    def show_edit(self):
        self.hide()
        self.a_edit = afil_edit(self.tupla, self.style_disable, True)
        self.a_edit.show()
    
    def show_consulta(self):
        self.hide()
        self.a_edit = afil_edit(self.tupla, self.style_disable, False)
        self.a_edit.show()

    def show_ver(self):
        self.hide()
        self.a_ver = afiliado_ver_todo(self.tupla, self.style_disable)
        self.a_ver.fill_tabla()
        self.a_ver.show()

    def show_principal(self):
        self.hide()
        self.principal = principal_win()
        self.principal.show()

class afil_edit(QtWidgets.QMainWindow):
    def __init__(self, tupla, style, editar):
        super().__init__()
        self.style_disable = style
        self.a_edit = Ui_Dialog_edit()
        self.a_edit.setupUi(self)
        self.tupla = tupla
        self.fill_combo()
        self.editar = editar
        if not self.editar:
            self.a_edit.label.setText("Seleccione el Afiliado a Consultar")
            self.a_edit.push_aceptar.setText("Consultar")
        self.a_edit.push_aceptar.clicked.connect(self.show_vista)
        self.a_edit.push_cancelar.clicked.connect(self.show_menu)
    
    def show_menu(self):
        self.hide()
        self.menu = afil_menu(self.tupla, self.style_disable)
        self.menu.show()
    
    def show_vista(self):
        self.hide()
        if self.editar:
            self.a_ui = afiliado_win(self.tupla, self.style_disable)
            self.a_ui.set_lines(self.tupla[self.a_edit.combo_carga.currentIndex()])
            self.a_ui.show()
        else:
            self.a_consultar = afiliado_ver(self.tupla, self.style_disable)
            self.a_consultar.setWindowTitle("Consultar Afiliado")
            self.a_consultar.set_lines(self.tupla[self.a_edit.combo_carga.currentIndex()])
            self.a_consultar.show()

    
    def fill_combo(self):
        index = 1
        for x in self.tupla:
            self.a_edit.combo_carga.insertItem(index, str(x[0]))
            index += 1

class afiliado_ver(QtWidgets.QMainWindow):
    def __init__(self, carga, style):
        super().__init__()
        self.consultar = Ui_view_afiliado()
        self.consultar.setupUi(self)
        self.tupla = carga
        self.style_disable = style
        self.consultar.push_regresar.clicked.connect(self.show_menu)

    def set_lines(self,carga):
        self.limite = 0
        afil = afiliado(carga[0], carga[1], carga[2], carga[3], carga[4], carga[5], carga[6], carga[7], carga[8], carga[9], carga[10], carga[11], carga[12])
        self.consultar.line_ide.setText(str(afil.get_ide()))
        self.consultar.line_plan.setText(str(afil.get_id_plan()))
        self.consultar.line_nombre.setText(afil.get_nombre())
        self.consultar.line_apellido.setText(afil.get_apellido())
        self.consultar.line_direccion.setText(afil.get_direccion())
        self.consultar.line_correo.setText(afil.get_correo())
        self.consultar.line_telefono.setText(str(afil.get_telefono()))
        self.consultar.line_ciudad.setText(afil.get_ciudad())
        self.consultar.line_nacimiento.setText(afil.get_nacimiento())
        self.consultar.line_edad.setText(str(afil.get_edad()))
        self.consultar.line_afiliacion.setText(afil.get_afiliacion())
        self.consultar.line_vacunado.setText(afil.get_vacunado())
        self.consultar.line_desafiliacion.setText(afil.get_desafiliacion())
    
    def show_menu(self):
        self.hide()
        self.menu = afil_menu(self.tupla, self.style_disable)
        self.menu.show()

class afiliado_ver_todo(QtWidgets.QMainWindow):
    def __init__(self, carga, style):
        super().__init__()
        self.ver_todo = Ui_ver_todo()
        self.ver_todo.setupUi(self)
        self.style_disable = style
        self.setGeometry(QRect(270, 160, 800, 160+(40*len(carga))))
        self.ver_todo.table_todos.setHorizontalHeaderLabels(("N° ID","Plan","Nombre","Apellido","Direccion","Telefono","Correo","Ciudad de Residencia","Nacimiento","Edad","Fecha de Afiliacion","Fecha de Desafiliacion","Vacunado"))
        self.carga = carga
        self.ver_todo.table_todos.setGeometry(QRect(30,10, 731, 41+(40*len(carga))))
        self.ver_todo.push_regresar.setGeometry(QRect(362,81+(40*len(carga)),75,23))
        self.ver_todo.push_regresar.clicked.connect(self.show_menu)

    def fill_tabla(self):
        self.ver_todo.table_todos.setRowCount(len(self.carga))
        row = 0
        for afiliado in self.carga:
            col = 0
            for item in afiliado:
                fill = QTableWidgetItem(str(item))
                fill.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ver_todo.table_todos.setItem(row, col, fill)
                col += 1
            row += 1
        self.ver_todo.table_todos.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def show_menu(self):
        self.hide()
        self.menu = afil_menu(self.carga, self.style_disable)
        self.menu.show()

class afiliado_win(QtWidgets.QMainWindow):
    def __init__(self, carga, style):
        super().__init__()
        self.limite = 6
        self.carga = carga
        self.style_disable = style
        self.correo_re = QRegularExpression()
        self.correo_re.setPattern("^[0-9a-zA-Z]+([0-9a-zA-Z]*[-._+])*[0-9a-zA-Z]+@[0-9a-zA-Z]+([-.][0-9a-zA-Z]+)*([0-9a-zA-Z]*[.])[a-zA-Z]")
        self.sql = sql()
        self.a_ui = Ui_afil_win()
        self.a_ui.setupUi(self)
        self.a_ui.check_desafiliado.hide()
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))
        self.a_ui.calendar_nacimiento.setMaximumDate(QDate.currentDate())
        self.only_int = QIntValidator()
        self.a_ui.line_ide.setValidator(self.only_int)
        self.a_ui.line_telefono.setValidator(self.only_int)
        self.a_ui.calendar_nacimiento.selectionChanged.connect(self.set_line_date)
        self.a_ui.push_guardar.setEnabled(self.campos_comprobacion())
        self.a_ui.push_guardar.setStyleSheet(self.style_disable)
        
        self.a_ui.line_ide.textChanged.connect(self.set_enable)
        self.a_ui.line_nombre.textChanged.connect(self.set_enable)
        self.a_ui.line_apellido.textChanged.connect(self.set_enable)
        self.a_ui.line_direccion.textChanged.connect(self.set_enable)
        self.a_ui.line_correo.textChanged.connect(self.set_enable)
        self.a_ui.line_telefono.textChanged.connect(self.set_enable)
        self.a_ui.line_ciudad.textChanged.connect(self.set_enable)

        self.a_ui.push_regresar.clicked.connect(self.show_menu)
        self.a_ui.push_guardar.clicked.connect(self.btn_guardar)
    
    def campos_comprobacion(self):
        if len(self.a_ui.line_ide.text()) > self.limite:
            self.a_ui.label_ide.hide()
        else:
            self.a_ui.label_ide.show()
            
        if self.correo_re.match(self.a_ui.line_correo.text()).hasMatch():
            self.a_ui.label_correo.hide()
        else:
            self.a_ui.label_correo.show()

        if len(self.a_ui.line_telefono.text()) > self.limite:
            self.a_ui.label_telefono.hide()
        else:
            self.a_ui.label_telefono.show()

        return (self.correo_re.match(self.a_ui.line_correo.text()).hasMatch() and len(self.a_ui.line_ide.text()) >self.limite and len(self.a_ui.line_nombre.text()) > 0 and len(self.a_ui.line_apellido.text()) > 0 and len(self.a_ui.line_direccion.text()) > 0 and  len(self.a_ui.line_correo.text()) > 0  and len(self.a_ui.line_telefono.text())> self.limite and len(self.a_ui.line_ciudad.text()) > 0)

    def set_enable(self):
        if self.campos_comprobacion():
            self.a_ui.push_guardar.setEnabled(self.campos_comprobacion())
            self.a_ui.push_guardar.setStyleSheet("color: rgb(63, 81, 181);border-style: solid;background-color:rgb(255, 255, 255) ;border-color: rgb(63, 81, 181);border-width: 2px;border-radius: 10px;")
        else:
            self.a_ui.push_guardar.setEnabled(self.campos_comprobacion())
            self.a_ui.push_guardar.setStyleSheet(self.style_disable)

    def set_line_date(self):
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))    
    
    def set_lines(self,carga):
        self.limite = 0
        self.a_ui.label_ide.destroy()
        self.a_ui.check_desafiliado.show()
        self.a_ui.checkBox.setGeometry(QRect(500,340,81,31))
        self.a_ui.label.setText("EDITAR AFILIADO")
        afil = afiliado(carga[0], carga[1], carga[2], carga[3], carga[4], carga[5], carga[6], carga[7], carga[8], carga[9], carga[10], carga[11], carga[12])
        self.a_ui.line_ide.setText(str(afil.get_ide()))
        self.a_ui.line_ide.setReadOnly(True)
        self.a_ui.line_nombre.setText(afil.get_nombre())
        self.a_ui.line_apellido.setText(afil.get_apellido())
        self.a_ui.line_direccion.setText(afil.get_direccion())
        self.a_ui.line_telefono.setText(str(afil.get_telefono()))
        self.a_ui.line_correo.setText(afil.get_correo())
        self.a_ui.line_ciudad.setText(afil.get_ciudad())
        self.a_ui.calendar_nacimiento.setSelectedDate(QDate.fromString(afil.get_nacimiento(), "dd/MM/yyyy"))
        

    def btn_guardar(self):
        if self.a_ui.checkBox.isChecked():
            vacunado = "Si"
        else:
            vacunado = "-"
        if self.a_ui.check_desafiliado.isChecked():
            desafiliado = f"{date.today().day}/{date.today().month}/{date.today().year}"
        else:
            desafiliado = "-"
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
            "desafiliacion":desafiliado,
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

        afilN.set_afiliado()
        self.show_menu()

    def show_menu(self):
        self.hide()
        self.menu = afil_menu(self.carga, self.style_disable)
        self.menu.show()

class citas_menu(QtWidgets.QMainWindow):

    def __init__(self, afiliados, lotes, planes, citas, style):
        super().__init__()
        self.lotes = lotes
        self.planes = planes
        self.afiliados = afiliados
        self.citas = citas
        self.menu = Ui_menu_citas()
        self.menu.setupUi(self)
        self.style_disable = style
        self.menu.push_calcular.clicked.connect(self.show_calcular)
        self.menu.push_regresar.clicked.connect(self.show_principal)
        self.menu.push_ver.clicked.connect(self.show_ver_todo)
        if len(self.citas) <= 0:
            self.menu.push_ver.setEnabled(False)
            self.menu.push_ver.setStyleSheet(self.style_disable)
            self.menu.push_consultar.setEnabled(False)
            self.menu.push_consultar.setStyleSheet(self.style_disable)
        else:
            self.menu.push_ver.setEnabled(True)
            self.menu.push_consultar.setEnabled(True)


    def show_calcular(self):
        self.hide()
        self.menu = citas_calcular(self.afiliados, self.lotes, self.planes, self.citas, self.style_disable)
        self.menu.show()
    
    def show_ver_todo(self):
        self.hide()
        self.ver_todo = citas_ver_todo(self.afiliados, self.lotes, self.planes, self.citas, self.style_disable)
        self.ver_todo.fill_tabla()
        self.ver_todo.show()
    def show_principal(self):
        self.hide()
        self.principal = principal_win()
        self.principal.show()

class citas_calcular(QtWidgets.QMainWindow):

    def __init__(self, afiliados, lotes, planes, citas, style):
        super().__init__()
        self.afiliados = afiliados
        self.lotes = lotes
        self.planes = planes
        self.afiliados = afiliados
        self.citas = citas
        self.style_disable = style
        self.calcular = Ui_citas()
        self.calcular.setupUi(self)
        self.set_line_date()
        self.campos_comprobar()
        self.calcular.push_calcular.setEnabled(False)
        self.calcular.push_calcular.clicked.connect(self.btn_calcular)
        self.calcular.spin_hour.valueChanged.connect(self.campos_comprobar)
        self.calcular.spin_minute.valueChanged.connect(self.campos_comprobar)
        self.calcular.calendarWidget.setMinimumDate(QDate.currentDate())
        self.calcular.calendarWidget.selectionChanged.connect(self.campos_comprobar)
        self.calcular.push_regresar.clicked.connect(self.show_menu)

    
    def campos_comprobar(self):
        self.set_line_date()
        if datetime.strptime(self.calcular.line_show_date.text(),"%d/%m/%Y %H:%M") < datetime.today():
            self.calcular.push_calcular.setEnabled(False)
            self.calcular.label_date.show()
            self.calcular.push_calcular.setStyleSheet(self.style_disable)
        else:
            self.calcular.push_calcular.setEnabled(True)
            self.calcular.label_date.hide()
            self.calcular.push_calcular.setStyleSheet("color: rgb(63, 81, 181);border-style: solid;background-color:rgb(255, 255, 255) ;border-color: rgb(63, 81, 181);border-width: 2px;border-radius: 10px;")
        

    def set_line_date(self):
        fecha = self.calcular.calendarWidget.selectedDate().toString("dd/MM/yyyy")
        self.hora = self.calcular.spin_hour.value()
        self.minuto = self.calcular.spin_minute.value()
        if self.hora >= 0 and self.hora < 10:
            self.hora = "0" + str(self.calcular.spin_hour.value())
        else:
            self.hora= str(self.calcular.spin_hour.value())
        self.calcular.line_show_date.setText(f"{fecha} {self.hora}:{self.minuto}") 
         
        if self.minuto >= 0 and self.minuto < 10:
            self.minuto = "0" + str(self.calcular.spin_minute.value())
        else:
            self.minuto = str(self.calcular.spin_minute.value())
        self.calcular.line_show_date.setText(f"{fecha} {self.hora}:{self.minuto}")   

    def btn_calcular(self):
        numero = 1
        prioridad = 1
        while prioridad <= len(self.planes):
            for afiliado in self.afiliados:
                if afiliado[1] == prioridad and afiliado[11] == "-" and afiliado[12] == "-":
                    for self.lote in self.lotes:
                        self.restantes = self.lote[3] - abs(self.lote[4] - self.lote[5])
                        if self.restantes > 0 :
                            break
                    
                    datos = {"numero":numero,
                        "plan":afiliado[1],
                        "ide": afiliado[0], 
                        "ciudad": afiliado[7],
                        "lote":self.lote[0],
                        "fecha":self.calcular.calendarWidget.selectedDate().toString("dd/MM/yyyy"),
                        "hora":str(self.hora + ":" + self.minuto)}

                    cita = citas(datos["numero"],
                        datos["plan"],
                        datos["ide"],
                        datos["ciudad"],
                        datos["lote"],
                        datos["fecha"],
                        datos["hora"])

                    if cita.set_cita():
                        pass
                    else:
                        self.minuto = str(int(self.minuto) + int("30"))
                        if int(self.minuto) == 60:
                            self.minuto = "00"
                            self.hora = str(int(self.hora) +int("01"))
                    numero += 1
            prioridad += 1
        self.show_menu()
        
    def show_menu(self):
        self.hide()
        self.sql = sql()
        self.menu = citas_menu(self.afiliados,self.lotes,self.planes, self.sql.cargar_tabla("Citas"), self.style_disable)
        self.menu.show()

class citas_ver_todo(QtWidgets.QMainWindow):
    def __init__(self, afiliados, lotes, planes, citas, style):
        super().__init__()
        self.setGeometry(QRect(0,0,0,0))
        self.afiliados = afiliados
        self.lotes = lotes
        self.planes = planes
        self.afiliados = afiliados
        self.citas = citas
        self.style_disable = style
        self.ver_todo = Ui_ver_todo()
        self.ver_todo.setupUi(self)
        self.setGeometry(QRect(250, 160, 800, 140+(40*len(self.citas))))
        self.ver_todo.table_todos.setColumnCount(7)
        self.ver_todo.table_todos.setHorizontalHeaderLabels(("Numero de Cita","Plan","Numero de Identificacion","Ciudad de Vacunacion","Lote Asignado","Fecha","Hora"))
        self.ver_todo.table_todos.setGeometry(QRect(30,10, 731, 41+(40*len(self.citas))))
        self.ver_todo.push_regresar.setGeometry(QRect(362,81+(40*len(self.citas)),75,23))
        self.ver_todo.push_regresar.clicked.connect(self.show_menu)

    def fill_tabla(self):
        self.ver_todo.table_todos.setRowCount(len(self.citas))
        row = 0
        for afiliado in self.citas:
            col = 0
            for item in afiliado:
                fill = QTableWidgetItem(str(item))
                fill.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ver_todo.table_todos.setItem(row, col, fill)
                col += 1
            row += 1
        self.ver_todo.table_todos.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def show_menu(self):
        self.hide()
        self.menu = citas_menu(self.afiliados,self.lotes,self.planes, self.citas, self.style_disable)
        self.menu.show()