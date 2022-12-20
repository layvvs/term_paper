from PyQt5.QtWidgets import QDialog
import resources_fin
from PyQt5 import QtCore, QtGui, QtWidgets
from library import Library


class Generator:
    """"
    This class generates dialog windows, badges and font
    """
    def __init__(self):
        self.db = Library()

    def g_allert_dialog(self, text='Empty',) -> QtWidgets.QDialog:
        dialog = QtWidgets.QDialog()
        dialog.setObjectName("dialog")
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
        okay_btn = QtWidgets.QPushButton(okay_frame)
        okay_btn.setMinimumSize(QtCore.QSize(180, 40))
        okay_btn.setMaximumSize(QtCore.QSize(400, 40))
        okay_btn.setObjectName("okay_btn")
        okay_btn.setText("Okay")
        okay_btn.setFont(self.g_font(16))
        horizontalLayout_2.addWidget(okay_btn)
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
        alert_lbl.setFont(self.g_font(12))
        horizontalLayout.addWidget(alert_lbl)
        okay_btn.clicked.connect(dialog.close)
        dialog.exec_()

    def g_font(self, size: int) -> QtGui.QFont:
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(size)
        return font

    def g_adding_suggestion_dialog(self, track_name: str, track_bpm: str, track_key: str) -> QtWidgets.QDialog:
        dialog = QtWidgets.QDialog()
        dialog.setObjectName("dialog")
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
        add_btn = QtWidgets.QPushButton(button_frame)
        add_btn.setMinimumSize(QtCore.QSize(188, 40))
        add_btn.setMaximumSize(QtCore.QSize(188, 40))
        add_btn.setObjectName("add_btn")
        add_btn.setText('Add to library')
        add_btn.setFont(self.g_font(16))
        horizontalLayout_2.addWidget(add_btn)
        cancel_btn = QtWidgets.QPushButton(button_frame)
        cancel_btn.setMinimumSize(QtCore.QSize(188, 40))
        cancel_btn.setMaximumSize(QtCore.QSize(188, 40))
        cancel_btn.setObjectName("cancel_btn")
        cancel_btn.setText('Cancel')
        cancel_btn.setFont(self.g_font(16))
        horizontalLayout_2.addWidget(cancel_btn)
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
        name_label_image.setFont(self.g_font(16))
        name_label_image.setText("")
        name_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/name.png"))
        name_label_image.setScaledContents(True)
        name_label_image.setObjectName("name_label_image")
        name_label = QtWidgets.QLabel(frame)
        name_label.setGeometry(QtCore.QRect(120, 10, 251, 65))
        name_label.setFont(self.g_font(16))
        name_label.setAlignment(QtCore.Qt.AlignCenter)
        name_label.setObjectName("name_label")
        name_label.setText(track_name)
        verticalLayout.addWidget(frame)
        cancel_btn.clicked.connect(dialog.close)
        add_btn.clicked.connect(lambda: self.db.add(track_name, track_bpm, track_key))
        add_btn.clicked.connect(dialog.close)
        dialog.exec_()

    def g_badge(self, info: tuple) -> QtWidgets:
        info_frame = QtWidgets.QFrame()
        info_frame.setGeometry(QtCore.QRect(0, 0, 401, 151))
        info_frame.setMinimumSize(QtCore.QSize(401, 151))
        info_frame.setMaximumSize(QtCore.QSize(401, 151))
        info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        info_frame.setObjectName("info_frame")
        verticalLayout = QtWidgets.QVBoxLayout(info_frame)
        verticalLayout.setObjectName("verticalLayout")
        labels_frame = QtWidgets.QFrame(info_frame)
        labels_frame.setStyleSheet("color: white;\n"
                                        "background-color: rgb(27, 33, 37);\n"
                                        "border-radius: 15px;")
        info_frame.setStyleSheet("color: white;\n"
                                        "background-color: white;\n"
                                        "border-radius: 15px;")
        labels_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        labels_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        labels_frame.setObjectName("labels_frame")
        name_label_image = QtWidgets.QLabel(labels_frame)
        name_label_image.setGeometry(QtCore.QRect(10, 10, 100, 65))
        name_label_image.setFont(self.g_font(16))
        name_label_image.setText("")
        name_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/name.png"))
        name_label_image.setScaledContents(True)
        name_label_image.setObjectName("name_label_image")
        name_label = QtWidgets.QLabel(labels_frame)
        name_label.setGeometry(QtCore.QRect(120, 10, 251, 65))
        name_label.setFont(self.g_font(16))
        name_label.setAlignment(QtCore.Qt.AlignCenter)
        name_label.setObjectName("name_label")
        name_label.setText(info[1])
        verticalLayout.addWidget(labels_frame)
        show_btn = QtWidgets.QPushButton(info_frame)
        show_btn.setMinimumSize(QtCore.QSize(382, 40))
        show_btn.setMaximumSize(QtCore.QSize(382, 40))
        show_btn.setText('Show')
        show_btn.setFont(self.g_font(16))
        show_btn.setStyleSheet("QPushButton{\n"
                                    "    color: white;\n"
                                    "    background-color: rgb(27, 33, 37);\n"
                                    "    border-radius: 15px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::hover, #menu_frame QPushButton::hover{\n"
                                    "    background-color: black;\n"
                                    "}\n"
                                    "")
        show_btn.setObjectName("show_btn")
        verticalLayout.addWidget(show_btn)
        show_btn.clicked.connect(lambda: self.g_show_dialog(info, info_frame))
        return info_frame


    def g_show_dialog(self, info: tuple, frame):
        dialog = QtWidgets.QDialog()
        dialog.setObjectName("show_dialog")
        dialog.resize(400, 300)
        dialog.setWindowTitle('More Info')
        dialog.setMinimumSize(QtCore.QSize(400, 300))
        dialog.setMaximumSize(QtCore.QSize(400, 300))
        dialog.setStyleSheet("#image_frame, #label_frame{\n"
                             "    border-color: gb(27, 33, 37);\n"
                             "    border-radius: 15px;\n"
                             "}")
        btn_frame = QtWidgets.QFrame(dialog)
        btn_frame.setGeometry(QtCore.QRect(0, 220, 401, 81))
        btn_frame.setStyleSheet("QPushButton{\n"
                                     "    color: white;\n"
                                     "    background-color: rgb(27, 33, 37);\n"
                                     "    border-radius: 15px;\n"
                                     "    font-family: Bahnschrift;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::hover, #menu_frame QPushButton::hover{\n"
                                     "    background-color: black;\n"
                                     "}")
        btn_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        btn_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        btn_frame.setObjectName("btn_frame")
        horizontalLayout = QtWidgets.QHBoxLayout(btn_frame)
        horizontalLayout.setObjectName("horizontalLayout")
        close_btn = QtWidgets.QPushButton(btn_frame)
        close_btn.setMinimumSize(QtCore.QSize(188, 40))
        close_btn.setMaximumSize(QtCore.QSize(188, 40))
        close_btn.setObjectName("close_btn")
        close_btn.setFont(self.g_font(16))
        close_btn.setText('Close')
        horizontalLayout.addWidget(close_btn)
        remove_btn = QtWidgets.QPushButton(btn_frame)
        remove_btn.setMinimumSize(QtCore.QSize(188, 40))
        remove_btn.setMaximumSize(QtCore.QSize(188, 40))
        remove_btn.setObjectName("remove_btn")
        remove_btn.setFont(self.g_font(16))
        remove_btn.setText('Remove')
        horizontalLayout.addWidget(remove_btn)
        info_frame = QtWidgets.QFrame(dialog)
        info_frame.setGeometry(QtCore.QRect(0, 0, 401, 221))
        info_frame.setStyleSheet("#info_frame{\n"
                                      "    border: 2px solid  black;\n"
                                      "    background-color: rgb(27, 33, 37);\n"
                                      "}")
        info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        info_frame.setObjectName("info_frame")
        image_frame = QtWidgets.QFrame(info_frame)
        image_frame.setGeometry(QtCore.QRect(0, 0, 117, 221))
        image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        image_frame.setObjectName("image_frame")
        verticalLayout = QtWidgets.QVBoxLayout(image_frame)
        verticalLayout.setObjectName("verticalLayout")
        name_label_image = QtWidgets.QLabel(image_frame)
        name_label_image.setText("")
        name_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/name.png"))
        name_label_image.setScaledContents(True)
        name_label_image.setObjectName("name_label_image")
        verticalLayout.addWidget(name_label_image)
        key_label_image = QtWidgets.QLabel(image_frame)
        key_label_image.setMinimumSize(QtCore.QSize(0, 0))
        key_label_image.setText("")
        key_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/key.png"))
        key_label_image.setScaledContents(True)
        key_label_image.setObjectName("key_label_image")
        verticalLayout.addWidget(key_label_image)
        bpm_label_image = QtWidgets.QLabel(image_frame)
        bpm_label_image.setText("")
        bpm_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/bpm.png"))
        bpm_label_image.setScaledContents(True)
        bpm_label_image.setObjectName("bpm_label_image")
        verticalLayout.addWidget(bpm_label_image)
        label_frame = QtWidgets.QFrame(info_frame)
        label_frame.setGeometry(QtCore.QRect(120, 0, 281, 221))
        label_frame.setStyleSheet("color: white;\n"
                                       "")
        label_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        label_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        label_frame.setObjectName("label_frame")
        verticalLayout_2 = QtWidgets.QVBoxLayout(label_frame)
        verticalLayout_2.setObjectName("verticalLayout_2")
        label = QtWidgets.QLabel(label_frame)
        label.setObjectName("label")
        label.setFont(self.g_font(16))
        label.setText(info[1])
        verticalLayout_2.addWidget(label)
        label_2 = QtWidgets.QLabel(label_frame)
        label_2.setObjectName("label_2")
        label_2.setFont(self.g_font(16))
        label_2.setText(info[3])
        verticalLayout_2.addWidget(label_2)
        label_3 = QtWidgets.QLabel(label_frame)
        label_3.setObjectName("label_3")
        label_3.setFont(self.g_font(16))
        label_3.setText(info[2])
        verticalLayout_2.addWidget(label_3)
        close_btn.clicked.connect(dialog.close)
        remove_btn.clicked.connect(lambda: self.db.remove(info[0]))
        remove_btn.clicked.connect(frame.deleteLater)
        remove_btn.clicked.connect(dialog.close)
        dialog.exec_()

