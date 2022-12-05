from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from key_finder import Tonal_Fragment as tg
from generator import Generator as g
import librosa

class Processor:
    """
    This class works with buttons
    """

    def __init__(self):
        self.path = ""

    def open_file(self, label, btn):
        file_open = QDialog()
        self.path = (QFileDialog\
                     .getOpenFileName(file_open, 'Open Audio File', '/home',
                                'MP3 File (*.mp3);;WAV File (*.wav)'))[0]
        if self.path != "":
            if librosa.get_duration(filename=self.path) < 30:
                g.dialog(g, 'Audio file duration should be 30 seconds or more')
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


    def analyse(self, bpm_label, key_label):
        y, sr = librosa.load(self.path)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        bpm_label.setText(str(int(tempo)))


