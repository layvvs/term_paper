from PyQt5 import QtWidgets
from interface import Ui_MainWindow
import library

db = library.Library()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.connections()
    MainWindow.show()
    sys.exit(app.exec_())