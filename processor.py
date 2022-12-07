from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from key_finder import Tonal_Fragment as tg
from generator import Generator as g
import librosa

class Processor:
    """
    This class works with buttons
    """

    def open_file(self, label, btn):
        self.path = (QFileDialog\
                     .getOpenFileName(QDialog(), 'Open Audio File', '/home',
                                'MP3 File (*.mp3);;WAV File (*.wav)'))[0]
        if self.path != "":
            if librosa.get_duration(filename=self.path) < 30:
                g.g_dialog(g, 'Audio file duration must be 30 seconds or more')
            else:
                index = len(self.path) - self.path[::-1].index('/')
                label.setText(self.path[index:-4])
                btn.setEnabled(True)
                btn.setStyleSheet(
"QPushButton{\n"
"    background-color: rgb(27, 33, 37);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton::hover{\n"
"   background-color: black;\n"
"}\n")


    def analyze(self, bpm_lbl: QtWidgets.QLabel, key_lbl: QtWidgets.QLabel):
        y, sr = librosa.load(self.path)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        y_harmonic, _ = librosa.effects.hpss(y)
        processed_data = tg(y_harmonic, sr, tstart=0, tend=30)
        key = processed_data.get_key()
        bpm_lbl.setText(str(int(tempo)))
        if type(key) is tuple:
            key_lbl.setFont(g.g_font(g, 12))
            key_lbl.setText(f"{key[0]}/{key[1]}")
        else:
            key_lbl.setText(key)
        # g.g_adding_suggestion(g)



