from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import library

class Generator:
    """"
    This class generates dialog windows, badges and font
    """

    def g_allert_dialog(self, text='Empty',) -> QDialog:
        dialog = QDialog()
        dialog.setObjectName("Dialog")
        dialog.setWindowTitle('Alert')
        dialog.resize(400, 200)
        dialog.setMinimumSize(QtCore.QSize(400, 200))
        dialog.setMaximumSize(QtCore.QSize(400, 200))
        dialog.setStyleSheet("#alert_frame, #okay_frame{\n"
                             "    border-radius: 15px;\n"
                             "\n"
                             "}")
        okay_frame = QtWidgets.QFrame(dialog)
        okay_frame.setGeometry(QtCore.QRect(0, 110, 401, 91))
        okay_frame.setStyleSheet("QPushButton{\n"
                                      "    color: white;\n"
                                      "    background-color: rgb(27, 33, 37);\n"
                                      "    border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::hover, #menu_frame QPushButton::hover{\n"
                                      "    background-color: black;\n"
                                      "}")
        okay_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        okay_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        okay_frame.setObjectName("okay_frame")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(okay_frame)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okay_btn = QtWidgets.QPushButton(okay_frame)
        self.okay_btn.setMinimumSize(QtCore.QSize(180, 40))
        self.okay_btn.setMaximumSize(QtCore.QSize(400, 40))
        self.okay_btn.setObjectName("okay_btn")
        self.okay_btn.setText("Okay")
        self.okay_btn.setFont(self.g_font(self, 16))
        horizontalLayout_2.addWidget(self.okay_btn)
        alert_frame = QtWidgets.QFrame(dialog)
        alert_frame.setGeometry(QtCore.QRect(0, 0, 401, 111))
        alert_frame.setStyleSheet("")
        alert_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        alert_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        alert_frame.setObjectName("alert_frame")
        horizontalLayout = QtWidgets.QHBoxLayout(alert_frame)
        horizontalLayout.setObjectName("horizontalLayout")
        alert_lbl = QtWidgets.QLabel(alert_frame)
        alert_lbl.setStyleSheet("color: white;\n"
                                     "background-color: rgb(27, 33, 37);\n"
                                     "border-radius: 15px;")
        alert_lbl.setAlignment(QtCore.Qt.AlignCenter)
        alert_lbl.setObjectName("alert_lbl")
        alert_lbl.setText(text)
        alert_lbl.setFont(self.g_font(self, 12))
        horizontalLayout.addWidget(alert_lbl)
        dialog.exec_()

    def g_font(self, size: int) -> QtGui.QFont:
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(size)
        return font

    def g_adding_suggestion(self, track_name: str) -> QDialog:
        dialog = QDialog()
        dialog.setObjectName("Dialog")
        dialog.setWindowTitle('Adding')
        dialog.resize(400, 200)
        dialog.setMinimumSize(QtCore.QSize(400, 200))
        dialog.setMaximumSize(QtCore.QSize(400, 200))
        dialog.setStyleSheet("#button_frame, #info_frame{\n"
                             "    border-radius: 15px;\n"
                             "}")
        button_frame = QtWidgets.QFrame(dialog)
        button_frame.setGeometry(QtCore.QRect(0, 100, 401, 101))
        button_frame.setStyleSheet("QPushButton{\n"
                                        "    color: white;\n"
                                        "    background-color: rgb(27, 33, 37);\n"
                                        "    border-radius: 15px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::hover, #menu_frame QPushButton::hover{\n"
                                        "    background-color: black;\n"
                                        "}")
        button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        button_frame.setObjectName("button_frame")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(button_frame)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_btn = QtWidgets.QPushButton(button_frame)
        self.add_btn.setMinimumSize(QtCore.QSize(188, 40))
        self.add_btn.setMaximumSize(QtCore.QSize(188, 40))
        self.add_btn.setObjectName("self.add_btn")
        self.add_btn.setText('Add to library')
        self.add_btn.setFont(self.g_font(self, 16))
        horizontalLayout_2.addWidget(self.add_btn)
        self.cancel_btn = QtWidgets.QPushButton(button_frame)
        self.cancel_btn.setMinimumSize(QtCore.QSize(188, 40))
        self.cancel_btn.setMaximumSize(QtCore.QSize(188, 40))
        self.cancel_btn.setObjectName("self.cancel_btn")
        self.cancel_btn.setText('Cancel')
        self.cancel_btn.setFont(self.g_font(self, 16))
        horizontalLayout_2.addWidget(self.cancel_btn)
        info_frame = QtWidgets.QFrame(dialog)
        info_frame.setGeometry(QtCore.QRect(0, 10, 401, 101))
        info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        info_frame.setObjectName("info_frame")
        verticalLayout = QtWidgets.QVBoxLayout(info_frame)
        verticalLayout.setObjectName("verticalLayout")
        frame = QtWidgets.QFrame(info_frame)
        frame.setStyleSheet("color: white;\n"
                                 "background-color: rgb(27, 33, 37);\n"
                                 "border-radius: 15px;")
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame")
        name_label_image = QtWidgets.QLabel(frame)
        name_label_image.setGeometry(QtCore.QRect(10, 10, 100, 65))
        name_label_image.setFont(self.g_font(self, 16))
        name_label_image.setText("")
        name_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/name.png"))
        name_label_image.setScaledContents(True)
        name_label_image.setObjectName("name_label_image")
        name_label = QtWidgets.QLabel(frame)
        name_label.setGeometry(QtCore.QRect(120, 10, 251, 65))
        name_label.setFont(self.g_font(self, 16))
        name_label.setAlignment(QtCore.Qt.AlignCenter)
        name_label.setObjectName("name_label")
        name_label.setText(track_name)
        verticalLayout.addWidget(frame)
        dialog.exec_()

    def connections(self):
        ...
