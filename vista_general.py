# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vista_general.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ver_todo(object):
    def setupUi(self, ver_todo):
        ver_todo.setObjectName("ver_todo")
        ver_todo.resize(800, 600)
        ver_todo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ver_todo)
        self.centralwidget.setObjectName("centralwidget")
        self.table_todos = QtWidgets.QTableWidget(self.centralwidget)
        self.table_todos.setGeometry(QtCore.QRect(30, 10, 731, 471))
        self.table_todos.setRowCount(0)
        self.table_todos.setColumnCount(13)
        self.table_todos.setObjectName("table_todos")
        self.push_regresar = QtWidgets.QPushButton(self.centralwidget)
        self.push_regresar.setGeometry(QtCore.QRect(362, 530, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.push_regresar.setFont(font)
        self.push_regresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.push_regresar.setStyleSheet("color: rgb(63, 81, 181);\n"
"border-style: solid;\n"
"background-color:rgb(255, 255, 255) ;\n"
"border-color:rgb(63, 81, 181);\n"
"border-width: 2px;\n"
"border-radius: 10px;")
        self.push_regresar.setObjectName("push_regresar")
        ver_todo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ver_todo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ver_todo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ver_todo)
        self.statusbar.setObjectName("statusbar")
        ver_todo.setStatusBar(self.statusbar)

        self.retranslateUi(ver_todo)
        QtCore.QMetaObject.connectSlotsByName(ver_todo)

    def retranslateUi(self, ver_todo):
        _translate = QtCore.QCoreApplication.translate
        ver_todo.setWindowTitle(_translate("ver_todo", "Vista General"))
        self.push_regresar.setText(_translate("ver_todo", "Regresar"))
