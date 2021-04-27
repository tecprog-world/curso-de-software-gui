#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:33:02 2021

@author: jhongvp
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('PyQT5 GUI')
        self.resize(200,300)
        self.add_widgets()

    def add_widgets(self):
        self.statusBar().showMessage('Esta es mi barra de estado que contiene texto')

        menubar = self.menuBar()
        file_menu = menubar.addMenu('Archivo')

        new_action = QAction('Nuevo', self)
        file_menu.addAction(new_action)

        new_action.setStatusTip('Nuevo archivo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
