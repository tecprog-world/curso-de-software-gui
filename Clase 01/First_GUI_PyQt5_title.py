# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
gui = QWidget()
gui.setWindowTitle('PyQT5 GUI')
gui.show()
sys.exit(app.exec_())
