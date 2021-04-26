#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:47:25 2021

@author: jhongvp
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Mi ventana PyQt5 GUI')
        self.resize(400,300)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())