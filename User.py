from PyQt5 import QtCore  #Importe de QtCore
from PyQt5.QtCore import QDate, QRect  #Importe de QDate y QRect
from PyQt5 import QtWidgets 
from PyQt5.QtGui import QIntValidator, QPixmap #Importe de QIntValidator y QPixmap
from Afiliados import *
from Lotes import lote

from principal import Ui_principal #Importe de la ventana principal
from afiliadoUi import Ui_afil_win #Importe de la ventana de crear afiliados
from menu_afiliado import Ui_afil_menu #Importe de la ventana del menú de afiliados
from menu_lotes import Ui_menu_lotes #Importe de la ventana del menú de lotes
from crear_lotes import Ui_crear_lote #Importe de la ventana para crear lotes
from edit_lote import Ui_Dialog_edit #Importe de la ventana para editar lotes
from vista_general import Ui_ver_todo #Importe de la ventana para visualizar la tabla completa de lotes
from consulta_desplegable import Ui_Dialog_edit1 #Importe de la ventana para seleccionar el lote a consultar
from consulta_lote import Ui_consultar_lote #Importe de la ventana de consulta individual de lote
from sql import sql #Importe de Lote
import vacuna #Importe de imágen de frasco de vacuna
import sys #Importe de archivo donde se maanejan bases de datos

#Clase de la ventana principal: desde aqui se ejecutan todas las funciones de dicha ventana
class principal_win(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self):
        super().__init__()
        self.afil_menu = afil_menu()
        self.lote_menu = lote_menu()
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
        self.ui.push_lotes.clicked.connect(self.show_lote_menu)

    def show_afil_menu(self):
        self.hide()
        self.afil_menu = afil_menu(self.afiliados, self.style_disable)
        self.afil_menu.show()
    
    def show_citas_menu(self):
        self.hide()
        self.citas_menu = citas_menu(self.afiliados,self.lotes, self.planes, self.citas, self.style_disable)
        self.citas_menu.show()

    def show_lote_menu(self):
        self.hide()
        self.lote_menu.show()

#Clase de ventana de menú de afiliado: allí se selecciona la acción que desea ejecutarse para un afiliado
class afil_menu(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self):
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

    def show_afil(self):
        self.hide()
        self.a_ui.show()

#Clase de ventana de menú de lote: allí se selecciona la acción que desea ejecutarse para un lote
class lote_menu(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self):
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
        
    def show_menu(self):
        self.ui=principal_win()
        self.hide()
        self.ui.show()

    def show_lote(self):
        self.crea_lote=crear_lote()
        self.hide()
        self.crea_lote.show()

    def show_edit(self):
        self.edit_lote=edit_lote(self.tupla)
        self.hide()
        self.edit_lote.show()

    def show_ver_todo(self):
        self.ver_todo=ver_todo(self.tupla)
        self.hide()
        self.ver_todo.show()

    def show_consulta(self):
        self.consultarLote=consul_lote_despl(self.tupla)
        self.hide()
        self.consultarLote.show()    



#Clase afiliado_win: maneja la funcionalidad de crear un afiliado
class afiliado_win(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self):
        super().__init__()
        self.a_ui = Ui_afil_win()
        self.a_ui.setupUi(self)
        self.set_lines()
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
    
    #Método set_line_date(self): ingresa la fecha del widget del calendario en el line edit de fecha
    def set_line_date(self):
        self.a_ui.line_show_date.setText(self.a_ui.calendar_nacimiento.selectedDate().toString("dd/MM/yyyy"))    
    
    #Método set_lines(self): 
    def set_lines(self):
        afil = afiliado("", "", "", "", "", "", "", "", f"{datetime.today().day}/{datetime.today().month}/{datetime.today().year}", "", "", "", "")
        self.a_ui.line_ide.setText(afil.get_ide())
        self.a_ui.line_apellido.setText(afil.get_apellido())
        self.a_ui.line_direccion.setText(afil.get_direccion())
        self.a_ui.line_telefono.setText(afil.get_telefono())
        self.a_ui.line_correo.setText(afil.get_correo())
        self.a_ui.line_ciudad.setText(afil.get_ciudad())
        self.a_ui.calendar_nacimiento.setSelectedDate(QDate.fromString(afil.get_nacimiento(), "dd/MM/yyyy"))
        
    #Método btn_guardar(self): envía la información ingresada en los line edits a la tabla de afiliado
    def btn_guardar(self):
        if self.a_ui.checkBox.isChecked():
            vacunado = "Si"
        else:
            vacunado = "-"
        #Tupla que se envia a la base de datos
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
        print (afilN.to_tuple())


#---------------------------------LOTE-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Clase crear_lote(QtWidgets.QMainWindow): maneja la funcionalidad de crear un lote
class crear_lote(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self):
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

    #Método que comprueba si los campos de no. de lote y cantidad recibida han sido llenados para habilitar o no el botón de guardar
    def comprobar(self):
        if len(self.crea_lote.lineEdit_no_lote.text()) > 0 and len(self.crea_lote.lineEdit_cant_recibida.text()) > 0:
            self.crea_lote.pushButton.setEnabled(True)
            self.crea_lote.pushButton.setStyleSheet("color: rgb(63, 81, 181);border-style: solid;background-color:rgb(255, 255, 255) ;border-color: rgb(63, 81, 181);border-width: 2px;border-radius: 10px;")
        else:
            self.crea_lote.pushButton.setEnabled(False)
            self.crea_lote.pushButton.setStyleSheet("color: rgb(116, 116, 116);border-style: solid;background-color:rgb(255, 255, 255) ;border-color:rgb(116, 116, 116);border-width: 2px;border-radius: 10px;")
        
    #Método para regresar al menú de lote
    def show_lote_menu(self):
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

    #Método para llenar comboBox de fabricante
    def fill_combo(self):
        index = 1
        for x in self.tupla:
            self.crea_lote.comboBox_fabricante.insertItem(index, str(x[0]))
            index += 1
        
    def set_lines_fabricante(self):
        self.crea_lote.lineEdit_fecha_ven.setText(self.crea_lote.calendarWidget_fechav.selectedDate().toString("dd/MM/yyyy"))
        self.carga=self.tupla[self.crea_lote.comboBox_fabricante.currentIndex()]
        self.crea_lote.lineEdit_tipo_vac.setText(self.carga[1])
        self.crea_lote.lineEdit_nodosis.setText(str(self.carga[2]))
        self.crea_lote.lineEdit_temperatura.setText(self.carga[3])
        self.crea_lote.lineEdit_efectividad.setText(self.carga[4])
        self.crea_lote.lineEdit_proteccion.setText(self.carga[5])

    def set_lines(self,carga):
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
        

    def btn_guardar_lote(self):
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

class edit_lote(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self,tupla):
        super().__init__()
        self.tupla=tupla
        self.editLote=Ui_Dialog_edit()
        self.editLote.setupUi(self)
        self.editLote.push_cancelar.clicked.connect(self.show_lote_menu)
        self.editLote.push_aceptar.clicked.connect(self.show_lote)
        self.fill_combo()

    def show_lote_menu(self):
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

    def show_lote(self):
        self.carga=self.tupla[self.editLote.combo_carga.currentIndex()]
        self.crea_lote=crear_lote()
        self.crea_lote.set_lines(self.carga)       
        self.hide()
        self.crea_lote.show()
    
    def fill_combo(self):
        index = 1
        for x in self.tupla:
            self.editLote.combo_carga.insertItem(index, str(x[0]))
            index += 1

class consul_lote_despl(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self,tupla):
        super().__init__()
        self.tupla=tupla
        self.consultarLote=Ui_Dialog_edit1()
        self.consultarLote.setupUi(self)
        self.consultarLote.push_cancelar.clicked.connect(self.show_lote_menu)
        self.consultarLote.push_aceptar.clicked.connect(self.show_lote)
        self.fill_combo()

    def show_lote_menu(self):
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

    def show_lote(self):
        self.carga=self.tupla[self.consultarLote.combo_carga.currentIndex()]
        self.conLote=consul_lote(self.carga)        
        self.hide()
        self.conLote.show()
    
    def fill_combo(self):
        index = 1
        for x in self.tupla:
            self.consultarLote.combo_carga.insertItem(index, str(x[0]))
            index += 1

class consul_lote(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self,tupla):
        super().__init__()
        self.tupla=tupla
        self.conlote=Ui_consultar_lote()
        self.conlote.setupUi(self)
        self.conlote.label_8.setPixmap(QPixmap("vacuna.jpg"))
        self.conlote.pushButton_regre.clicked.connect(self.show_lote)
        self.set_lines(self.tupla)

    def set_lines(self,carga):
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
        
    def show_lote(self):
        self.conLote=lote_menu()        
        self.hide()
        self.conLote.show()
    
    

class ver_todo(QtWidgets.QMainWindow):
    #Método __init__: método principal de la clase
    def __init__(self, carga):
        super().__init__()
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

    def fill_tabla(self):
        self.ver_todo.table_todos.setRowCount(len(self.carga))
        row = 0
        for afiliado in self.carga:
            col = 0
            for item in afiliado:
                fill = QtWidgets.QTableWidgetItem(str(item))
                fill.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ver_todo.table_todos.setItem(row, col, fill)
                col += 1
            row += 1
        self.ver_todo.table_todos.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def show_lote_menu(self):
        self.lote_menu=lote_menu()
        self.hide()
        self.lote_menu.show()

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