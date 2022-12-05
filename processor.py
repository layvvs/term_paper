from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import librosa

class Processor:
    def __init__(self):
        self.path = ""

    def open_file(self, label, btn):
        file_open = QDialog()
        self.path = (QFileDialog\
                     .getOpenFileName(file_open, 'Open Audio File', '/home/layv/Desktop',
                                'MP3 File (*.mp3);;WAV File (*.wav)'))[0]
        if self.path != "":
            index = len(self.path) - self.path[::-1].index('/')
            label.setText(self.path[index:-4])
            btn.setEnabled(True)

    def analyse(self, bpm_label, key_label):
        y, sr = librosa.load(self.path)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        bpm_label.setText(str(int(tempo)))
        # font = QtGui.QFont()
        # font.setFamily("Bahnschrift")
        # font.setPointSize(16)
        # dialog = QDialog()
        # dialog.resize(400, 200)
        # d_lbl = QtWidgets.QLabel('Soon', dialog)
        # d_lbl.setAlignment(QtCore.Qt.AlignCenter)
        # d_lbl.setFont(font)
        # d_lbl.move(100, 50)
        # dialog.setWindowTitle("Dialog")
        # dialog.exec_()

