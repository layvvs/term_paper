from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from key_finder import Tonal_Fragment as tg
import librosa
import generator

class Processor:
    """
    This class works with buttons
    """

    def open_file(self, name_label: QtWidgets.QLabel, bpm_label: QtWidgets.QLabel, key_label: QtWidgets.QLabel, btn: QtWidgets.QPushButton):
        self.btn = btn
        self.name_label = name_label
        self.bpm_label = bpm_label
        self.key_label = key_label

        g = generator.Generator()
        self.path = (QFileDialog\
                     .getOpenFileName(QDialog(), 'Open Audio File', '/home',
                                'MP3 File (*.mp3);;WAV File (*.wav)'))[0]
        if self.path != "":
            if librosa.get_duration(filename=self.path) < 30:
                g.g_allert_dialog('Audio file duration must be 30 seconds or more')
            else:
                self.bpm_label.setText("Unknown")
                self.key_label.setText("Unknown")
                self.key_label.setFont(g.g_font(16))
                index = len(self.path) - self.path[::-1].index('/')
                self.name = self.path[index:-4]
                self.name_label.setText(self.name)
                btn.setEnabled(True)
            btn.setStyleSheet(
                "QPushButton{\n"
                "    background-color: rgb(27, 33, 37);\n"
                "    border-radius: 15px;\n"
                "}\n"
                "QPushButton::hover{\n"
                "   background-color: black;\n"
                "}\n")


    def analyze(self):
        g = generator.Generator()
        y, sr = librosa.load(self.path)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        y_harmonic, _ = librosa.effects.hpss(y)
        processed_data = tg(y_harmonic, sr, tstart=0, tend=30)
        key = processed_data.get_key()
        tempo = str(int(tempo))
        self.bpm_label.setText(tempo)
        if type(key) is tuple:
            self.key_label.setFont(g.g_font(12))
            key = f"{key[0]}/{key[1]}"
            self.key_label.setText(key)
        else:
            self.key_label.setText(key)
        g.g_adding_suggestion_dialog(self.name, tempo, key)
        self.btn.setStyleSheet(
            "QPushButton{\n"
            "    background-color: grey;\n"
            "}\n")
        self.btn.setEnabled(False)




