# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:36:08 2021

@author: PEDRO JUAN
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoRadioButton2 import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonMedium.toggled.connect(self.dispSelected)
        self.ui.radioButtonLarge.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)
        self.show()
    def dispSelected(self):
        selected1="";
        selected2=""
        if self.ui.radioButtonMedium.isChecked()==True:
            selected1="Medio"
        if self.ui.radioButtonLarge.isChecked()==True:
            selected1="Largo"
        if self.ui.radioButtonXL.isChecked()==True:
            selected1="Extra Largo"
        if self.ui.radioButtonXXL.isChecked()==True:
            selected1="Extra Extra Largo"
        if self.ui.radioButtonDebitCard.isChecked()==True:
            selected2="Tarjeta Debito/Credito"
        if self.ui.radioButtonNetBanking.isChecked()==True:
            selected2="Banca por Internet"
        if self.ui.radioButtonCashOnDelivery.isChecked()==True:
            selected2="Pagar por Delivery"
        self.ui.labelSelected.setText("Tamaño de polo escogido"+selected1+"\n y el método de pago escogido es " + selected2)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())