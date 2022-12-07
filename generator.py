from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Generator:
    """"
    This class generates dialog windows and badges
    """
    def qdialog(self, text='Empty', alert='Alert') -> QDialog:
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        dialog = QDialog()
        dialog.resize(400, 200)
        d_lbl = QtWidgets.QLabel(text, dialog)
        d_lbl.setFont(font)
        d_lbl.move(0, 75)
        dialog.setWindowTitle(alert)
        dialog.exec_()