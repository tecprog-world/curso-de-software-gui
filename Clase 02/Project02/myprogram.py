# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myprogram.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 414)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 20))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEdici_n = QtWidgets.QMenu(self.menubar)
        self.menuEdici_n.setObjectName("menuEdici_n")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionImprimir = QtWidgets.QAction(MainWindow)
        self.actionImprimir.setObjectName("actionImprimir")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCopiar = QtWidgets.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionCortar = QtWidgets.QAction(MainWindow)
        self.actionCortar.setObjectName("actionCortar")
        self.actionPegar = QtWidgets.QAction(MainWindow)
        self.actionPegar.setObjectName("actionPegar")
        self.actionAcerca_del_software = QtWidgets.QAction(MainWindow)
        self.actionAcerca_del_software.setObjectName("actionAcerca_del_software")
        self.actionBuscar_actualizaciones = QtWidgets.QAction(MainWindow)
        self.actionBuscar_actualizaciones.setObjectName("actionBuscar_actualizaciones")
        self.actionDocumentaci_n = QtWidgets.QAction(MainWindow)
        self.actionDocumentaci_n.setObjectName("actionDocumentaci_n")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_como)
        self.menuArchivo.addAction(self.actionImprimir)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEdici_n.addAction(self.actionCopiar)
        self.menuEdici_n.addAction(self.actionCortar)
        self.menuEdici_n.addAction(self.actionPegar)
        self.menuAyuda.addAction(self.actionAcerca_del_software)
        self.menuAyuda.addAction(self.actionBuscar_actualizaciones)
        self.menuAyuda.addAction(self.actionDocumentaci_n)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEdici_n.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MI PROYECTO"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">MI TEXTO</span></p></body></html>"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEdici_n.setTitle(_translate("MainWindow", "Edición"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_como.setText(_translate("MainWindow", "Guardar como"))
        self.actionImprimir.setText(_translate("MainWindow", "Imprimir"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionCopiar.setText(_translate("MainWindow", "Copiar"))
        self.actionCortar.setText(_translate("MainWindow", "Cortar"))
        self.actionPegar.setText(_translate("MainWindow", "Pegar"))
        self.actionAcerca_del_software.setText(_translate("MainWindow", "Acerca del software"))
        self.actionBuscar_actualizaciones.setText(_translate("MainWindow", "Buscar actualizaciones"))
        self.actionDocumentaci_n.setText(_translate("MainWindow", "Documentación"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

