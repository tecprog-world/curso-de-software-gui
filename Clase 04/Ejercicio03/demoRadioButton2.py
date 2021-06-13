# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(243, 300)
        font = QtGui.QFont()
        font.setFamily("HPUser New")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonMedium = QtWidgets.QRadioButton(Dialog)
        self.radioButtonMedium.setObjectName("radioButtonMedium")
        self.verticalLayout.addWidget(self.radioButtonMedium)
        self.radioButtonLarge = QtWidgets.QRadioButton(Dialog)
        self.radioButtonLarge.setObjectName("radioButtonLarge")
        self.verticalLayout.addWidget(self.radioButtonLarge)
        self.radioButtonXL = QtWidgets.QRadioButton(Dialog)
        self.radioButtonXL.setObjectName("radioButtonXL")
        self.verticalLayout.addWidget(self.radioButtonXL)
        self.radioButtonXXL = QtWidgets.QRadioButton(Dialog)
        self.radioButtonXXL.setObjectName("radioButtonXXL")
        self.verticalLayout.addWidget(self.radioButtonXXL)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonDebitCard = QtWidgets.QRadioButton(Dialog)
        self.radioButtonDebitCard.setObjectName("radioButtonDebitCard")
        self.verticalLayout_2.addWidget(self.radioButtonDebitCard)
        self.radioButtonNetBanking = QtWidgets.QRadioButton(Dialog)
        self.radioButtonNetBanking.setObjectName("radioButtonNetBanking")
        self.verticalLayout_2.addWidget(self.radioButtonNetBanking)
        self.radioButtonCashOnDelivery = QtWidgets.QRadioButton(Dialog)
        self.radioButtonCashOnDelivery.setObjectName("radioButtonCashOnDelivery")
        self.verticalLayout_2.addWidget(self.radioButtonCashOnDelivery)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.labelSelected = QtWidgets.QLabel(Dialog)
        self.labelSelected.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.labelSelected.setObjectName("labelSelected")
        self.verticalLayout_3.addWidget(self.labelSelected)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aplicativo"))
        self.label.setText(_translate("Dialog", "Escoje el tamaño de polo"))
        self.radioButtonMedium.setText(_translate("Dialog", "M"))
        self.radioButtonLarge.setText(_translate("Dialog", "L"))
        self.radioButtonXL.setText(_translate("Dialog", "XL"))
        self.radioButtonXXL.setText(_translate("Dialog", "XXL"))
        self.label_2.setText(_translate("Dialog", "Escoje el método de pago"))
        self.radioButtonDebitCard.setText(_translate("Dialog", "Tarjeta de Debito/Credito"))
        self.radioButtonNetBanking.setText(_translate("Dialog", "Banca por Internet"))
        self.radioButtonCashOnDelivery.setText(_translate("Dialog", "Pagar por delivery"))
        self.labelSelected.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

