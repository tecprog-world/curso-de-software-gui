#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:33:02 2021

@author: jhongvp
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())


