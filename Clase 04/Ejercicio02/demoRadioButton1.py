# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 237)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.gridLayout.addWidget(self.radioButtonFirstClass, 1, 0, 1, 1)
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.gridLayout.addWidget(self.radioButtonBusinessClass, 2, 0, 1, 1)
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")
        self.gridLayout.addWidget(self.radioButtonEconomyClass, 3, 0, 1, 1)
        self.labelFare = QtWidgets.QLabel(Dialog)
        self.labelFare.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.labelFare.setObjectName("labelFare")
        self.gridLayout.addWidget(self.labelFare, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PIZZERÍA TW"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ESCOJA PROMOCIÓN DE LA PIZZERÍA</span></p></body></html>"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "02 Pizzas familiares (Americana y Hawaina) s./60.00"))
        self.radioButtonBusinessClass.setText(_translate("Dialog", "02 Pizzas medianas (Peperoni y Hawaina) s./30.00"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "01 Pizza personal (Americana con gaseosa) s./5.00"))
        self.labelFare.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>"))

