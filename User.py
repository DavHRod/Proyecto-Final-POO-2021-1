#--------- Importaciones PyQt5 -------------------------------------------------------------------------------
from PyQt5.QtCore import QDate, QRect, QRegularExpression #Importación QDate, QRect, QRegularExpression
from PyQt5.QtGui import QIntValidator, QPixmap #Importación QIntValidator, QPixmap
from PyQt5 import QtCore #Importación QtCore
from PyQt5 import QtWidgets #Importación QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem #Importación QTableWidgetItem
from PyQt5 import QtWidgets #Importación QtWidgets

#--------- Importaciones ventanas ----------------------------------------------------------------------------

from principal import Ui_principal#Importe de ventana del menú principal

from menu_afiliado import Ui_afil_menu #Importe de la ventana del menú de afiliados
from menu_lotes import Ui_menu_lotes #Importe de la ventana del menú de lotes
from afiliadoUi import Ui_afil_win #Importe de la ventana para crear afiliados
from edit_afil import Ui_Dialog_edit #Importe de la ventana para editar afiliados
from view_afiliado import Ui_view_afiliado #Importe de la ventana para consultar afiliados 
from crear_lotes import Ui_crear_lote #Importe de la ventana para crear lotes
from edit_lote import Ui_Dialog_edit #Importe de la ventana para editar lotes
from consulta_desplegable import Ui_Dialog_edit1 #Importe de la ventana para seleccionar el lote a consultar
from consulta_lote import Ui_consultar_lote #Importe de la ventana de consulta individual de lote
from vista_general import Ui_ver_todo #Importe de la ventana de consulta general de lote
import vacuna #Importe de imágen de frasco de vacuna
from MenuPlanes import * #Importe de la ventana del menú de planes
from CrearPlan import * #Importe de la ventana para crear planes
from citasUi import Ui_citas #Importe de la ventana para crear citas
from menu_citas import Ui_menu_citas #Importe de la ventana del menú de citas

#----------- Importación de modulos -------------------------------------------------------------------------------------------------------
from Afiliados import * #Importe módulo Afiliados 
from Lotes import * #Importe módulo Lotes
from Citas import citas #Importe módulo Citas
from sql import sql #Modulo que maneja base de datos
import sys

#----------- Clase ventana principal --------------------------------------------------------------------------------------------------------------
class principal_win(QtWidgets.QMainWindow): #Clase ventana principal
    def __init__(self): #Método principal de la clase
        super().__init__()
        self.ui = Ui_principal()
        self.ui.setupUi(self)
        self.sql = sql()
        self.afiliados = self.sql.cargar_tabla("Afiliados")
        self.lotes = self.sql.cargar_tabla("Lotes")
        self.planes = self.sql.cargar_tabla("Planes")
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"

        if len(self.afiliados) <= 0 or len(self.lotes) <= 0 or len(self.planes) <= 0:
            self.ui.push_citas.setEnabled(False)
            self.ui.push_citas.setStyleSheet(self.style_disable)
        else:
            self.ui.push_citas.setEnabled(True)
        self.ui.push_afiliados.clicked.connect(self.show_afil_menu)
        self.ui.push_lotes.clicked.connect(self.show_lote_menu)
        self.ui.push_planes.clicked.connect(self.show_planes_menu)
        self.ui.push_citas.clicked.connect(self.show_citas_menu)
        self.ui.push_salir.clicked.connect(self.salir)
        
    def show_afil_menu(self): #Método que muestra el menú de afiliados
        self.hide()
        self.afil_menu = afil_menu()
        self.afil_menu.show()
    
    def show_lote_menu(self):  #Método que muestra el menú de lotes
        self.hide()
        self.lote_menu = lote_menu()
        self.lote_menu.show()

    def show_planes_menu(self):  #Método que muestra el menú de planes
        self.hide()
        self.planes_menu = planes_menu()
        self.planes_menu.show()

    def show_citas_menu(self):  #Método que muestra el menú de citas
        self.hide()
        self.citas_menu = citas_menu()
        self.citas_menu.show()
    
    def salir(self): #Método para cierre del programa
        exit()

#--------------- Módulo Afiliados ----------------------------------------------------------------------------------------------------------------

class afil_menu(QtWidgets.QMainWindow): #Clase para abrir menú de afiliados
    def __init__(self): #Método principal de la clase
        super().__init__()
        self.sql = sql()
        self.afiliados = self.sql.cargar_tabla("Afiliados")
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
        self.a_menu = Ui_afil_menu()
        self.a_menu.setupUi(self)
        
        if len(self.afiliados) == 0:
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
    
    def show_afil(self): #Método para mostrar la ventana de crear un nuevo afiliado
        self.hide()
        self.a_ui = afiliado_win(self.afiliados)
        self.a_ui.show()

    def show_edit(self): #Método para mostrar la ventana de editar afiliado
        self.hide()
        self.a_edit = afil_edit("Afiliado")
        self.a_edit.show()
    
    def show_consulta(self): #Método para mostrar la ventana de consulta individual de afiliado
        self.hide()
        self.a_edit = afil_edit("Consultar")
        self.a_edit.show()

    def show_ver(self): #Método para mostrar la ventana de consulta general de afiliados
        self.hide()
        self.a_ver = afiliado_ver_todo(self.afiliados, self.style_disable,"")
        self.a_ver.fill_tabla()
        self.a_ver.show()

    def show_principal(self): #Método para retornar a la ventana principal
        self.hide()
        self.principal = principal_win()
        self.principal.show()
    

class afil_edit(QtWidgets.QMainWindow): #Clase que abre la ventana para editar afiliado
    def __init__(self, tipo): #Método principal de la clase
        super().__init__()
        self.a_edit = Ui_Dialog_edit()
        self.a_edit.setupUi(self)
        self.sql = sql()
        self.tupla = self.sql.cargar_tabla("Afiliados")
        self.lotes = self.sql.cargar_tabla("Lotes")
        self.planes = self.sql.cargar_tabla("Planes")
        self.citas = self.sql.cargar_tabla("Citas")
        self.tipo = tipo
        if self.tipo == "Consultar":
            self.a_edit.label.setText("Seleccione el Afiliado a Consultar")
            self.a_edit.push_aceptar.setText("Consultar")
        elif self.tipo == "Planes":
            self.tupla= self.planes
            self.a_edit.label.setText("Seleccione el Lote a Consultar")
            self.a_edit.push_aceptar.setText("Consultar")
        elif self.tipo == "Citas":
            self.tupla = self.citas
            self.a_edit.label.setText("Seleccione la Citas a Consultar")
            self.a_edit.push_aceptar.setText("Consultar")
        self.fill_combo()

        self.a_edit.push_aceptar.clicked.connect(self.show_vista)
        self.a_edit.push_cancelar.clicked.connect(self.show_menu)
    
    def show_vista(self): #Método que muestra una determinada ventana dependiento del tipo que se le envie
        self.hide()
        if self.tipo == "Afiliado":
            self.a_ui = afiliado_win(self.tupla)
            self.a_ui.set_lines(self.tupla[self.a_edit.combo_carga.currentIndex()])
            self.a_ui.show()
        elif self.tipo == "Consultar":
            self.a_consultar = afiliado_ver(self.tupla, "Afiliado")
            self.a_consultar.setWindowTitle("Consultar Afiliado")
            self.a_consultar.set_lines(self.tupla[self.a_edit.combo_carga.currentIndex()])
            self.a_consultar.show()
        elif self.tipo == "Citas":
            self.a_consultar = afiliado_ver(self.citas,"Citas")
            self.a_consultar.setWindowTitle("Consultar Cita")
            self.a_consultar.set_lines(self.citas[self.a_edit.combo_carga.currentIndex()])
            self.a_consultar.show()
        elif self.tipo == "Planes":
            self.a_consultar = afiliado_ver(self.tupla, "Planes")
            self.a_consultar.setWindowTitle("Consultar Plan")
            self.a_consultar.set_lines(self.tupla[self.a_edit.combo_carga.currentIndex()])
            self.a_consultar.show()

    def fill_combo(self): #Método para llenar comboBox
        index = 1
        if self.tipo == "Citas":
            for x in self.tupla:
                self.a_edit.combo_carga.insertItem(index, str(x[2]))
                index += 1
        else:
            for x in self.tupla:
                self.a_edit.combo_carga.insertItem(index, str(x[0]))
                index += 1

    def show_menu(self): #Método para regresar al menú de afiliados
        self.hide()
        if self.tipo == "Planes":
            self.menu = planes_menu()
        elif self.tipo == "Citas":
            self.menu = citas_menu()
        else:
            self.menu = afil_menu()
        self.menu.show()
        
class afiliado_ver(QtWidgets.QMainWindow): #Clase para consultar de manera individual
    def __init__(self, carga, tipo): #Método principal de la clase
        super().__init__()
        self.consultar = Ui_view_afiliado()
        self.consultar.setupUi(self)
        self.tipo = tipo
        self.tupla = carga
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
        self.consultar.push_regresar.clicked.connect(self.show_menu)

    def set_lines(self,carga): #Método para llenar lineEdit con información de las tablas
        if self.tipo == "Afiliado":
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
        elif self.tipo == "Citas":
            self.limite = 0
            self.consultar.label.setText("CONSULTAR CITA")
            self.consultar.line_correo.setGeometry(QRect(220,330,151,20))
            self.consultar.line_telefono.setGeometry(QRect(410,330,151,20))
            self.consultar.label_correo.setGeometry(QRect(220,310,151,20))
            self.consultar.label_telefono.setGeometry(QRect(410,310,151,20))
            cita = citas(carga[0],carga[1],carga[2],carga[3],carga[4],carga[5],carga[6])
            self.consultar.label_ide.setText("Numero De Cita")
            self.consultar.line_ide.setText(str(cita.get_numero()))
            self.consultar.label_plan.setText("Plan Asignado")
            self.consultar.line_plan.setText(str(cita.get_id_plan()))
            self.consultar.label_nombre.setText("Numero De Identificación")
            self.consultar.line_nombre.setText(str(cita.get_ide()))
            self.consultar.label_apellido.setText("Ciudad De Cita")
            self.consultar.line_apellido.setText(str(cita.get_ciudad()))
            self.consultar.label_direccion.setText("Lote Asignado")
            self.consultar.line_direccion.setText(str(cita.get_lote()))
            self.consultar.label_correo.setText("Fecha De Cita")
            self.consultar.line_correo.setText(str(cita.get_fecha()))
            self.consultar.label_telefono.setText("Hora De Cita")
            self.consultar.line_telefono.setText(str(cita.get_hora()))
            self.consultar.label_ciudad.hide()
            self.consultar.line_ciudad.hide()
            self.consultar.label_nacimiento.hide()
            self.consultar.line_nacimiento.hide()
            self.consultar.label_edad.hide()
            self.consultar.line_edad.hide()
            self.consultar.label_afiliacion.hide()
            self.consultar.line_afiliacion.hide()
            self.consultar.label_vacunacion.hide()
            self.consultar.line_vacunado.hide()
            self.consultar.label_desafil.hide()
            self.consultar.line_desafiliacion.hide()
        elif self.tipo == "Planes":
            self.limite = 0
            self.consultar.label.setText("CONSULTAR PLANES")
            self.consultar.line_nombre.setGeometry(QRect(220,260,151,20))
            self.consultar.line_apellido.setGeometry(QRect(410,260,151,20))
            self.consultar.label_nombre.setGeometry(QRect(220,240,151,20))
            self.consultar.label_apellido.setGeometry(QRect(410,240,151,20))
            self.consultar.label_ide.setText("ID")
            self.consultar.line_ide.setText(str(carga[0]))
            self.consultar.label_plan.setText("Edad Mínima")
            self.consultar.line_plan.setText(str(carga[1]))
            self.consultar.label_nombre.setText("Edad Máxima")
            self.consultar.line_nombre.setText(str(carga[2]))
            self.consultar.label_apellido.setText("Fecha De Inicio")
            self.consultar.line_apellido.setText(str(carga[3]))
            self.consultar.label_direccion.hide()
            self.consultar.line_direccion.hide()
            self.consultar.label_correo.hide()
            self.consultar.line_correo.hide()
            self.consultar.label_telefono.hide()
            self.consultar.line_telefono.hide()
            self.consultar.label_ciudad.hide()
            self.consultar.line_ciudad.hide()
            self.consultar.label_nacimiento.hide()
            self.consultar.line_nacimiento.hide()
            self.consultar.label_edad.hide()
            self.consultar.line_edad.hide()
            self.consultar.label_afiliacion.hide()
            self.consultar.line_afiliacion.hide()
            self.consultar.label_vacunacion.hide()
            self.consultar.line_vacunado.hide()
            self.consultar.label_desafil.hide()
            self.consultar.line_desafiliacion.hide()

    def show_menu(self): #Método para regresar al menú de afiliados
        self.hide()
        if self.tipo == "Planes":
            self.menu = planes_menu()
        elif self.tipo == "Citas":
            self.menu = citas_menu()
        else:
            self.menu = afil_menu()
        self.menu.show()

class afiliado_ver_todo(QtWidgets.QMainWindow): #Método para consulta general de una tabla
    def __init__(self, carga, style, tipo): #Método principal de la clase
        super().__init__()
        self.ver_todo = Ui_ver_todo()
        self.ver_todo.setupUi(self)
        self.carga = carga
        self.style_disable = style
        self.tipo = tipo
        self.setGeometry(QRect(270, 160, 800, 160+(40*len(carga))))
        self.ver_todo.table_todos.setHorizontalHeaderLabels(("N° ID","Plan","Nombre","Apellido","Direccion","Telefono","Correo","Ciudad de Residencia","Nacimiento","Edad","Fecha de Afiliacion","Fecha de Desafiliacion","Vacunado"))
        if self.tipo == "Citas":
            self.ver_todo.table_todos.setHorizontalHeaderLabels(("N° Cita","Plan","N° de Identificación","Ciudad de Vacunación","Lote","Fecha de Cita", "Hora de Cita"))
            self.ver_todo.table_todos.setColumnCount(7)
        elif self.tipo == "Planes":
            self.ver_todo.table_todos.setHorizontalHeaderLabels(("ID","Edad Mínima","Edad Máxima","Fecha de Inicio"))
            self.ver_todo.table_todos.setColumnCount(4)
        self.fill_tabla()
        self.ver_todo.table_todos.setGeometry(QRect(30,10, 731, 41+(40*len(carga))))
        self.ver_todo.push_regresar.setGeometry(QRect(362,81+(40*len(carga)),75,23))
        self.ver_todo.push_regresar.clicked.connect(self.show_menu)

    def fill_tabla(self): #Método para llenar la tabla de consulta general
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

    def show_menu(self): #Método para regresar al menú de afiliados
        self.hide()
        if self.tipo == "Planes":
            self.menu = planes_menu()
        elif self.tipo == "Citas":
            self.menu = citas_menu()
        else:
            self.menu = afil_menu()
        self.menu.show()

class afiliado_win(QtWidgets.QMainWindow): #Clase para abrir la ventana de crear afiliado
    def __init__(self, carga): #Método principal de la clase
        super().__init__()
        self.limite = 6
        self.carga = carga
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
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
    
    def campos_comprobacion(self): #Método para comprobar la información que se ingres en los campos de id, telefono y correo
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

    def set_enable(self): #Método para habilitar o deshabilitar el botón de guardar segun comprobaciones de campo
        if self.campos_comprobacion():
            self.a_ui.push_guardar.setEnabled(self.campos_comprobacion())
            self.a_ui.push_guardar.setStyleSheet("color: rgb(63, 81, 181);border-style: solid;background-color:rgb(255, 255, 255) ;border-color: rgb(63, 81, 181);border-width: 2px;border-radius: 10px;")
        else:
            self.a_ui.push_guardar.setEnabled(self.campos_comprobacion())
            self.a_ui.push_guardar.setStyleSheet(self.style_disable)

    def set_line_date(self): #Método para mostrar fecha del widget de fecha
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))    
    
    def set_lines(self,carga ): #Método para llenar los campos a editar 
        self.limite = 0
        self.a_ui.label_ide.destroy()
        self.a_ui.check_desafiliado.show()
        self.a_ui.checkBox.setGeometry(QRect(500,340,81,31))
        self.a_ui.label.setText("EDITAR AFILIADO")
        self.afil = afiliado(carga[0], carga[1], carga[2], carga[3], carga[4], carga[5], carga[6], carga[7], carga[8], carga[9], carga[10], carga[11], carga[12])
        self.a_ui.line_ide.setText(str(self.afil.get_ide()))
        self.a_ui.line_ide.setReadOnly(True)
        self.a_ui.line_nombre.setText(self.afil.get_nombre())
        self.a_ui.line_apellido.setText(self.afil.get_apellido())
        self.a_ui.line_direccion.setText(self.afil.get_direccion())
        self.a_ui.line_telefono.setText(str(self.afil.get_telefono()))
        self.a_ui.line_correo.setText(self.afil.get_correo())
        self.a_ui.line_ciudad.setText(self.afil.get_ciudad())
        if self.afil.get_vacunado() == "Si":
            self.a_ui.checkBox.setChecked(True)
        if self.afil.get_desafiliacion() != "-":
            self.a_ui.check_desafiliado.setChecked(True)
        self.a_ui.calendar_nacimiento.setSelectedDate(QDate.fromString(self.afil.get_nacimiento(), "dd/MM/yyyy"))
        
    def btn_guardar(self): #Método para guardar la información de afiliado en la tabla        
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

        try:
            if self.afil.get_vacunado() == "-"and self.afil.get_desafiliacion() == "-" and self.a_ui.checkBox.isChecked():
                afilN.vacunar()
        except:
            pass
        afilN.calcular_plan()
        afilN.set_afiliado()
        self.show_menu()

    def show_menu(self): #Método para regresar al menú de afiliados
        self.hide()
        self.menu = afil_menu()
        self.menu.show()

#-------------- Módulo Lotes ---------------------------------------------------------------------------------------------------------------------------

class lote_menu(QtWidgets.QMainWindow): #Clase de ventana de menú de lote: allí se selecciona la acción que desea ejecutarse para un lote    
    def __init__(self): #Método principal de la clase
        super().__init__()        
        self.lot_menul = Ui_menu_lotes()
        self.lot_menul.setupUi(self)
        self.lot_menul.push_crear_lote.clicked.connect(self.show_lote)
        self.lot_menul.push_editar_lote.clicked.connect(self.show_edit)
        self.lot_menul.push_consulta_general.clicked.connect(self.show_ver_todo)
        self.lot_menul.push_consultar_lote.clicked.connect(self.show_consulta)
        self.lot_menul.push_regresar.clicked.connect(self.show_menu)
        self.sql=sql()
        self.tupla=self.sql.cargar_tabla("Lotes")
        
    def show_menu(self): #Método para regresar a la ventana pricipal
        self.ui=principal_win()
        self.hide()
        self.ui.show()

    def show_lote(self): #Método para abrir la ventana para crear un lote
        self.crea_lote=crear_lote()
        self.hide()
        self.crea_lote.show()

    def show_edit(self): #Método para abrir la ventana para editar un lote
        self.edit_lote=edit_lote(self.tupla)
        self.hide()
        self.edit_lote.show()

    def show_ver_todo(self): #Método para abrir la ventana para consultar la tabla de lotes
        self.ver_todo=ver_todo(self.tupla)
        self.hide()
        self.ver_todo.show()

    def show_consulta(self): #Método para abrir la ventana para seleccionar el lote a consultar
        self.consultarLote=consul_lote_despl(self.tupla)
        self.hide()
        self.consultarLote.show()   
         
class crear_lote(QtWidgets.QMainWindow): #Clase crear_lote(QtWidgets.QMainWindow): maneja la funcionalidad de crear un lote
    def __init__(self): #Método principal de la clase
        super().__init__()
        self.crea_lote=Ui_crear_lote()
        self.crea_lote.setupUi(self)
        self.crea_lote.label_8.setPixmap(QPixmap("vacuna.jpg"))
        self.crea_lote.pushButton.setStyleSheet("color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;")
        self.entero=QIntValidator()
        self.crea_lote.lineEdit_no_lote.setValidator(self.entero)
        self.crea_lote.pushButton.setEnabled(False)
        self.crea_lote.lineEdit_cant_recibida.setValidator(self.entero)
        self.crea_lote.pushButton.clicked.connect(self.btn_guardar_lote)
        self.crea_lote.pushButton_regre.clicked.connect(self.show_lote_menu)
        self.crea_lote.calendarWidget_fechav.setMinimumDate(QDate.currentDate())
        self.crea_lote.calendarWidget_fechav.selectionChanged.connect(self.set_lines_fabricante)
        self.tupla=[("Sinovac","Virus Desactivado",2,"2°","50%","No se sabe","vacuna_sinovac.jpg"),
            ("Pfizer","ARN",2,"-80°","95%","No se sabe","vacuna_pfizer.jpg"),
            ("Moderna","ARN",2,"-25°","94.5%","90 Dias","vacuna_moderna.jpg"),
            ("SputnikV","Vector Viral",2,"-18°","92%","150 Dias","vacuna_sputnikv.jpg"),
            ("AstraZeneca","Vector Viral",2,"2°","62%","No se sabe","vacuna_astrazeneca.jpg"),
            ("Sinopharm","Vector Viral",2,"2°","79.3%","No se sabe","vacuna_sinopharm.jpg"),
            ("Covaxim","Virus Desactivado",2,"2°","78%","No se sabe","vacuna_covaxin.jpg")]
        self.fill_combo()
        self.set_lines_fabricante()
        self.crea_lote.comboBox_fabricante.currentIndexChanged.connect(self.set_lines_fabricante)
        self.crea_lote.lineEdit_no_lote.textChanged.connect(self.comprobar)
        self.crea_lote.lineEdit_cant_recibida.textChanged.connect(self.comprobar)

    def comprobar(self): #Método que comprueba si los campos de no. de lote y cantidad recibida han sido llenados para habilitar o no el botón de guardar
        if len(self.crea_lote.lineEdit_no_lote.text()) > 0 and len(self.crea_lote.lineEdit_cant_recibida.text()) > 0:
            self.crea_lote.pushButton.setEnabled(True)
            self.crea_lote.pushButton.setStyleSheet("color: rgb(63, 81, 181);border-style: solid;background-color:rgb(255, 255, 255) ;border-color: rgb(63, 81, 181);border-width: 2px;border-radius: 10px;")
        else:
            self.crea_lote.pushButton.setEnabled(False)
            self.crea_lote.pushButton.setStyleSheet("color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;")
            
    def show_lote_menu(self): #Método para regresar al menú de lote
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

    def fill_combo(self): #Método para llenar comboBox de fabricante
        index = 1
        for x in self.tupla:
            self.crea_lote.comboBox_fabricante.insertItem(index, str(x[0]))
            index += 1
        
    def set_lines_fabricante(self): #Método para que llenen los datos de la vacuna cuando se seleccione el fabricante
        self.crea_lote.lineEdit_fecha_ven.setText(self.crea_lote.calendarWidget_fechav.selectedDate().toString("dd/MM/yyyy"))
        self.carga=self.tupla[self.crea_lote.comboBox_fabricante.currentIndex()]
        self.crea_lote.lineEdit_tipo_vac.setText(self.carga[1])
        self.crea_lote.lineEdit_nodosis.setText(str(self.carga[2]))
        self.crea_lote.lineEdit_temperatura.setText(self.carga[3])
        self.crea_lote.lineEdit_efectividad.setText(self.carga[4])
        self.crea_lote.lineEdit_proteccion.setText(self.carga[5])

    def set_lines(self,carga): #Método para llenar los campos que se van a editar según el número de lote seleccionado
        self.crea_lote.lineEdit_Titulo.setText("Editar Lote")
        self.carga2=carga
        self.crea_lote.lineEdit_no_lote.setReadOnly(True)
        self.crea_lote.lineEdit_no_lote.setText(str(self.carga2[0]))
        self.crea_lote.lineEdit_cant_recibida.setText(str(self.carga2[3]))
        self.crea_lote.lineEdit_fecha_ven.setText(self.carga2[11])
        self.crea_lote.calendarWidget_fechav.setSelectedDate(QDate.fromString(self.carga2[10],"dd/MM/yyyy"))
        self.crea_lote.lineEdit_fecha_ven.setText(self.crea_lote.calendarWidget_fechav.selectedDate().toString("dd/MM/yyyy"))
        index=0
        while self.crea_lote.comboBox_fabricante.itemText(index) != self.carga2[1]:            
            index+=1
        self.crea_lote.comboBox_fabricante.setCurrentIndex(index)
        

    def btn_guardar_lote(self): #Método para guardar información del lote creado o editado
        datosl = {"idlote":int(self.crea_lote.lineEdit_no_lote.text()), 
            "fabricante":self.carga[0],
            "tipo_vacuna":self.carga[1],
            "cant_recibida":int(self.crea_lote.lineEdit_cant_recibida.text()),
            "cant_asignada":0,
            "cant_usada":0,
            "dosis":self.carga[2],
            "temperatura":self.carga[3],
            "efectividad":self.carga[4],
            "proteccion":self.carga[5],
            "fecha_vencimiento":self.crea_lote.lineEdit_fecha_ven.text(),
            "imagen":" "}

        lote_nuevo= lote(datosl["idlote"],
            datosl["fabricante"],
            datosl["tipo_vacuna"],
            datosl["cant_recibida"],
            datosl["cant_asignada"],
            datosl["cant_usada"],
            datosl["dosis"],
            datosl["temperatura"],
            datosl["efectividad"],
            datosl["proteccion"],
            datosl["fecha_vencimiento"],
            datosl["imagen"])
        lote_nuevo.set_lote()
        self.show_lote_menu()

class edit_lote(QtWidgets.QMainWindow): #Clase que abre la ventana seleccionar el lote a editar
    def __init__(self,tupla): #Método principal de la clase
        super().__init__()
        self.tupla=tupla
        self.editLote=Ui_Dialog_edit()
        self.editLote.setupUi(self)
        self.editLote.push_cancelar.clicked.connect(self.show_lote_menu)
        self.editLote.push_aceptar.clicked.connect(self.show_lote)
        self.fill_combo()

    def show_lote_menu(self): #Método para retornar al menú de lote
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

    def show_lote(self): #Método para abrir la ventana para editar un lote
        self.carga=self.tupla[self.editLote.combo_carga.currentIndex()]
        self.crea_lote=crear_lote()
        self.crea_lote.set_lines(self.carga)       
        self.hide()
        self.crea_lote.show()
    
    def fill_combo(self): #Método para rellenar comboBox para seleccionar el lote a editar
        index = 1
        for x in self.tupla:
            self.editLote.combo_carga.insertItem(index, str(x[0]))
            index += 1

class consul_lote_despl(QtWidgets.QMainWindow): #Método para abrir la ventana de selección de lote a consultar
    def __init__(self,tupla): #Método principal de la clase
        super().__init__()
        self.tupla=tupla
        self.consultarLote=Ui_Dialog_edit1()
        self.consultarLote.setupUi(self)
        self.consultarLote.push_cancelar.clicked.connect(self.show_lote_menu)
        self.consultarLote.push_aceptar.clicked.connect(self.show_lote)
        self.fill_combo()

    def show_lote_menu(self): #Método para retornar al menú de lote
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

    def show_lote(self): #Método para abrir la ventan de consulta individual de lote
        self.carga=self.tupla[self.consultarLote.combo_carga.currentIndex()]
        self.conLote=consul_lote(self.carga)        
        self.hide()
        self.conLote.show()
    
    def fill_combo(self): #Método para rellenar comboBox para seleccionar el lote a consultar
        index = 1
        for x in self.tupla:
            self.consultarLote.combo_carga.insertItem(index, str(x[0]))
            index += 1

class consul_lote(QtWidgets.QMainWindow): #Clase para abrir la ventana de consulta individual de lote
    def __init__(self,tupla): #Método principal de la clase
        super().__init__()
        self.tupla=tupla
        self.conlote=Ui_consultar_lote()
        self.conlote.setupUi(self)
        self.conlote.label_8.setPixmap(QPixmap("vacuna.jpg"))
        self.conlote.pushButton_regre.clicked.connect(self.show_lote)
        self.set_lines(self.tupla)

    def set_lines(self,carga): #Método para llenar los lineEdit para la consulta individual de lote
        self.carga3=carga
        self.conlote.lineEdit_no_lote.setText(str(self.carga3[0]))
        self.conlote.lineEdit_fabricante.setText(str(self.carga3[1]))
        self.conlote.lineEdit_tipo_vac.setText(str(self.carga3[2]))
        self.conlote.lineEdit_cant_recibida.setText(str(self.carga3[3]))
        self.conlote.lineEdit_nodosis.setText(str(self.carga3[6]))
        self.conlote.lineEdit_temperatura.setText(str(self.carga3[7]))        
        self.conlote.lineEdit_efectividad.setText(str(self.carga3[8]))
        self.conlote.lineEdit_proteccion.setText(str(self.carga3[9]))
        self.conlote.lineEdit_fecha_ven.setText(self.carga3[10])
        
    def show_lote(self): #Método para retornar al menú de lotes
        self.conLote=lote_menu()        
        self.hide()
        self.conLote.show()

class ver_todo(QtWidgets.QMainWindow): #Clase para consultar de manera general los lotes existentes
    def __init__(self, carga): #Método principal de la clase
        super().__init__()
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
        self.ver_todo = Ui_ver_todo()
        self.ver_todo.setupUi(self)  
        self.ver_todo.table_todos.setColumnCount(12)      
        self.setGeometry(QRect(270, 160, 800, 160+(40*len(carga))))
        self.ver_todo.table_todos.setHorizontalHeaderLabels(("ID Lote","Fabricante","Tipo de Vacuna","Cantidad Recibida","Cantidad Asignada","Cantidad Usada","No. Dosis","Temperatura","Efectividad","Tiempo de Protección","Fecha de Vencimiento", "Imagen"))
        self.carga = carga
        self.fill_tabla()
        self.ver_todo.table_todos.setGeometry(QRect(30,10, 731, 41+(40*len(carga))))
        self.ver_todo.push_regresar.setGeometry(QRect(362,81+(40*len(carga)),75,23))
        self.ver_todo.push_regresar.clicked.connect(self.show_lote_menu)

    def fill_tabla(self): #Método para llenar tabla para de consulta general en lotes
        self.ver_todo.table_todos.setRowCount(len(self.carga))
        row = 0
        for lote in self.carga:
            col = 0
            for item in lote:
                fill = QtWidgets.QTableWidgetItem(str(item))
                fill.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ver_todo.table_todos.setItem(row, col, fill)
                col += 1
            row += 1
        self.ver_todo.table_todos.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def show_lote_menu(self): #Método para regresar al menú de lotes
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

    def show_menu(self): #Método para mostar la ventana del menú de afiliados
        self.hide()
        self.menu = afil_menu(self.carga, self.style_disable)
        self.menu.show()

#--------------- Módulo Planes --------------------------------------------------------------------------------------------------------------------------

class planes_menu(QtWidgets.QMainWindow): #Clase para abrir la ventana de menu de planes
    def __init__(self): #Método principal de la clase
        super().__init__()
        self.sql = sql()
        self.planes = self.sql.cargar_tabla("Planes")
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
        self.ui_menuplanes = Ui_MenuPlanesWindow()
        self.ui_menuplanes.setupUi(self)
        if len(self.planes) <= 0:
            self.ui_menuplanes.pushButton_ConsultarPlan.setEnabled(False)
            self.ui_menuplanes.pushButton_ConsultarPlan.setStyleSheet(self.style_disable)
            self.ui_menuplanes.pushButton_all.setEnabled(False)
            self.ui_menuplanes.pushButton_all.setStyleSheet(self.style_disable)
        self.ui_menuplanes.pushButton_CrearPlan.clicked.connect(self.show_plan)
        self.ui_menuplanes.pushButton_ConsultarPlan.clicked.connect(self.show_consultar)
        self.ui_menuplanes.pushButton_all.clicked.connect(self.show_all)
        self.ui_menuplanes.pushButton_Regresar.clicked.connect(self.show_principal)

    def show_plan(self): #Método para mostrar la ventana de crear un nuevo plan
        self.hide()
        self.planes_crear = planes_crear()
        self.planes_crear.show()

    def show_consultar(self): #Método para mostrar la ventana de consulta individual de planes
        self.hide()
        self.carga = sql()
        self.carga = self.carga.cargar_tabla("Planes")
        self.consultar = afil_edit("Planes")
        self.consultar.show()

    def show_all(self): #Método para mostrar la ventana de consulta general de planes
        self.hide()
        self.carga = sql()
        self.carga = self.carga.cargar_tabla("Planes")
        self.all = afiliado_ver_todo(self.carga,"","Planes")
        self.all.show()

    def show_principal(self): #Método para regresar a la ventana pricipal
        self.hide()
        self.principal = principal_win()
        self.principal.show()


class planes_crear(QtWidgets.QMainWindow): #Clase para crear un plan de vacunación
    def __init__(self): #Método principal de la clase
        super().__init__()
        self.tabla = sql()
        self.tabla = self.tabla.cargar_tabla("Planes")
        self.ui_crearPlan = Ui_CrearPlanWindow()
        self.ui_crearPlan.setupUi(self)
        if len(self.tabla) > 0:
            self.mins = []
            self.maxs = []
            for plan in self.tabla:
                self.mins.append(plan[1])
                self.maxs.append(plan[2])
            self.rangos = []
            for edades in range(len(self.mins)):
                self.rangos.append(range(self.mins[edades], self.maxs[edades]+1))
        self.set_line_date()
        self.comprobar()
        self.ui_crearPlan.calendar_fechaInicio.setMinimumDate(QDate.currentDate())
        self.ui_crearPlan.calendar_fechaInicio.selectionChanged.connect(self.set_line_date)
        self.ui_crearPlan.pushButton_Regresar.clicked.connect(self.show_menu)
        self.ui_crearPlan.spinBox_Min.valueChanged.connect(self.comprobar)
        self.ui_crearPlan.spinBox_Max.valueChanged.connect(self.comprobar)
        self.ui_crearPlan.pushButton_Guardar.clicked.connect(self.btn_guardar)
        self.sql = sql()

    def comprobar(self): #Método para comprobar que no haya cruce entre la edad mínima y la edad máxima al crear un pla
        if (self.ui_crearPlan.spinBox_Min.value() + 1) >= self.ui_crearPlan.spinBox_Max.value():
            self.ui_crearPlan.spinBox_Max.setValue(self.ui_crearPlan.spinBox_Min.value()+1)
        self.ui_crearPlan.spinBox_Max.setMinimum(self.ui_crearPlan.spinBox_Min.value()+1)
        
    def set_line_date(self): #Método para mostrar fecha del widget de fecha
        self.ui_crearPlan.lineEdit_FechaInicio.setText(self.ui_crearPlan.calendar_fechaInicio.selectedDate().toString("dd/MM/yyyy"))

    def comprobar_cruce(self): #Método para comprobar que no hayan cruces entre las edades de los planes
        self.cruce = False
        if not (len(self.tabla) <= 0):
            rango_in = range(self.ui_crearPlan.spinBox_Min.value(), self.ui_crearPlan.spinBox_Max.value() + 1)
            for existente in self.rangos:
                for x in rango_in:
                    if x in existente:
                        self.cruce = True
                        return existente
                if self.cruce == True:
                    break
        
    def btn_guardar(self): #Método para guardar información del plan creado o editado
        self.tabla = self.sql.cargar_tabla("Planes")
        self.rango_err = self.comprobar_cruce()
        if not self.cruce:
            id = len(self.tabla) + 1
            datos = { 
                "ID": id,
                "Edad_Min":int(self.ui_crearPlan.spinBox_Min.text()),
                "Edad_Max":int(self.ui_crearPlan.spinBox_Max.text()),
                "Fecha_Inicio":self.ui_crearPlan.lineEdit_FechaInicio.text(),
                }

            PlanN = plan(datos["ID"],
                datos["Edad_Min"],
                datos["Edad_Max"],
                datos["Fecha_Inicio"]
                )
            PlanN.set_plan()
            PlanN.calcular()
            self.show_menu()
        else:
            self.ui_crearPlan.label_error.setText("La Edad Presenta Cruce " + str(self.rango_err))
            
    def show_menu(self): #Método para regresar al menú de planes
        self.hide()
        self.planes_menu = planes_menu()
        self.planes_menu.show()

#----------------- Módulo de citas ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class citas_menu(QtWidgets.QMainWindow): #Clase para abrir la ventana del menu de citas
    def __init__(self): #Método principal de la clase
        super().__init__()
        self.sql = sql()
        self.afiliados = self.sql.cargar_tabla("Afiliados")
        self.lotes = self.sql.cargar_tabla("Lotes")
        self.planes = self.sql.cargar_tabla("Planes")
        self.citas = self.sql.cargar_tabla("Citas")
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
        self.menu = Ui_menu_citas()
        self.menu.setupUi(self)
        self.menu.push_calcular.clicked.connect(self.show_calcular)
        self.menu.push_regresar.clicked.connect(self.show_principal)
        self.menu.push_ver.clicked.connect(self.show_ver_todo)
        self.menu.push_consultar.clicked.connect(self.show_consultar)
        if len(self.citas) <= 0:
            self.menu.push_ver.setEnabled(False)
            self.menu.push_ver.setStyleSheet(self.style_disable)
            self.menu.push_consultar.setEnabled(False)
            self.menu.push_consultar.setStyleSheet(self.style_disable)
        else:
            self.menu.push_ver.setEnabled(True)
            self.menu.push_consultar.setEnabled(True)

    def show_calcular(self): #Método para abrir la ventana para calcular citas 
        self.hide()
        self.menu = citas_calcular()
        self.menu.show()
    
    def show_ver_todo(self): #Método para abrir la ventana para consultar la tabla de citas
        self.hide()
        self.citas = self.sql.cargar_tabla("Citas")
        self.ver_todo = afiliado_ver_todo(self.citas,self.style_disable, "Citas")
        self.ver_todo.fill_tabla()
        self.ver_todo.show()
    
    def show_consultar(self): #Método para abrir la ventana para seleccionar la cita a consultar
        self.hide()
        self.consultar = afil_edit("Citas")
        self.consultar.show()

    def show_principal(self): #Método para regresar a la ventana pricipal
        self.hide()
        self.principal = principal_win()
        self.principal.show()

class citas_calcular(QtWidgets.QMainWindow): #Clase para calcular citas
    def __init__(self): #Método principal de la clase
        super().__init__()
        self.sql = sql()
        self.afiliados = self.sql.cargar_tabla("Afiliados")
        self.lotes = self.sql.cargar_tabla("Lotes")
        self.planes = self.sql.cargar_tabla("Planes")
        self.style_disable = "color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;"
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

    def campos_comprobar(self): #Método para comprobar la fecha en el line_show_date
        self.set_line_date()
        if datetime.strptime(self.calcular.line_show_date.text(),"%d/%m/%Y %H:%M") < datetime.today():
            self.calcular.push_calcular.setEnabled(False)
            self.calcular.label_date.show()
            self.calcular.push_calcular.setStyleSheet(self.style_disable)
        else:
            self.calcular.push_calcular.setEnabled(True)
            self.calcular.label_date.hide()
            self.calcular.push_calcular.setStyleSheet("color: rgb(63, 81, 181);border-style: solid;background-color:rgb(255, 255, 255) ;border-color: rgb(63, 81, 181);border-width: 2px;border-radius: 10px;")
        
    def set_line_date(self): #Método para mostar la fecha del calendarWidget en el lineEdit
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

    def btn_calcular(self): #Método para calcular citas
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
                        cita.asignada()
                        pass
                    else:
                        self.minuto = str(int(self.minuto) + int("30"))
                        if int(self.minuto) == 60:
                            self.minuto = "00"
                            self.hora = str(int(self.hora) +int("01"))
                    numero += 1
            prioridad += 1
        self.show_menu()
        
    def show_menu(self): #Método para regresar al menú de citas
        self.hide()
        self.sql = sql()
        self.menu = citas_menu()
        self.menu.show()
