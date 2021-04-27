import sys
from PyQt5 import QtWidgets
from myprogram import Ui_MainWindow

class ExitDesignerGUI():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.update_widgets()
        self.widget_actions()
        self.MainWindow.show()
        sys.exit(app.exec_())

    def widget_actions(self):
        self.ui.actionSalir.setStatusTip('Clic para salir de la aplicacion')
        self.ui.actionSalir.triggered.connect(self.close_GUI)

    def close_GUI(self):
        self.MainWindow.close()

    def update_widgets(self):
        self.MainWindow.setWindowTitle('PyQt5 GUI')

if __name__ == "__main__":
    ExitDesignerGUI()












