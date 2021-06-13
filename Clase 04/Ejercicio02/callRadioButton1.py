# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 12:00:56 2021

@author: PEDRO JUAN
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoRadioButton1 import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)
        self.show()
    def dispFare(self):
        fare=0
        if self.ui.radioButtonFirstClass.isChecked()==True:
            fare=60
        if self.ui.radioButtonBusinessClass.isChecked()==True:
            fare=30
        if self.ui.radioButtonEconomyClass.isChecked()==True:
            fare=5
        self.ui.labelFare.setText("El precio a pagar es "+str(fare))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())