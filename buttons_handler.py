from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from generator import Generator
from processor import Processor

class ButtonsHandler:
    """
    This class works with buttons
    """
    def __init__(self, name_label: QtWidgets.QLabel, bpm_label: QtWidgets.QLabel, key_label: QtWidgets.QLabel, btn: QtWidgets.QPushButton):
        self.btn = btn
        self.name_label = name_label
        self.bpm_label = bpm_label
        self.key_label = key_label
        self.g = Generator()
        self.p = Processor()

    def btn_switch(self, enable: bool):
        if enable:
            self.btn.setStyleSheet(
                "QPushButton{\n"
                "    background-color: rgb(27, 33, 37);\n"
                "    border-radius: 15px;\n"
                "}\n"
                "QPushButton::hover{\n"
                "   background-color: black;\n"
                "}\n")
            self.btn.setEnabled(True)
        else:
            self.btn.setStyleSheet(
                "QPushButton{\n"
                "    background-color: grey;\n"
                "}\n")
            self.btn.setEnabled(False)

    def get_name(self):
        index = len(self.path) - self.path[::-1].index('/')
        return self.path[index:-4]

    def open_file(self):
        self.path = (QFileDialog\
                     .getOpenFileName(QDialog(), 'Open Audio File', '/home',
                                'MP3 File (*.mp3);;WAV File (*.wav)'))[0]
        if self.path != "":
            if not self.p.audio_valid(self.path):
                self.g.g_allert_dialog('Audio file duration must be 30 seconds or more')
            else:
                self.bpm_label.setText("Unknown")
                self.key_label.setText("Unknown")
                self.key_label.setFont(self.g.g_font(16))
                self.name_label.setText(self.get_name())
                self.btn_switch(True)

    def analyze(self):
        self.p.load_audio()
        tempo = self.p.bpm_finder()
        key = self.p.key_finder()
        self.bpm_label.setText(tempo)
        if type(key) is tuple:
            self.key_label.setFont(self.g.g_font(12))
            key = f"{key[0]}/{key[1]}"
            self.key_label.setText(key)
        else:
            self.key_label.setText(key)
        self.g.g_adding_suggestion_dialog(self.get_name(), tempo, key)
        self.btn_switch(False)





