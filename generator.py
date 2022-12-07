from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Generator:
    """"
    This class generates dialog windows, badges and font
    """

    def g_dialog(self, text='Empty', title='Alert') -> QDialog:
        dialog = QDialog()
        dialog.resize(400, 200)
        d_lbl = QtWidgets.QLabel(text, dialog)
        d_lbl.setFont(self.g_font(self, 12))
        d_lbl.move(0, 75)
        dialog.setWindowTitle(title)
        dialog.exec_()

    def g_font(self, size: int) -> QtGui.QFont:
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(size)
        return font

    def g_adding_suggestion(self):
        ...