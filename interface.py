import resources_fin

from PyQt5 import QtCore, QtGui, QtWidgets
from processor import Processor as p


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 600)
        MainWindow.setMinimumSize(QtCore.QSize(822, 600))
        MainWindow.setMaximumSize(QtCore.QSize(822, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons_new/icons_new/analysis (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{\n"
"    font-family: Bahnschrift;\n"
"    color: white;\n"
"    border: nine;\n"
"}\n"
"\n"
"#info_frame{\n"
"    background-color: rgb(27, 33, 37);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#stackedWidget{\n"
"    border: 2px solid  black;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#frame{\n"
"    border: 2px solid  black;\n"
"    border-radius: 15px;\n"
"}\n"
"#frame_2{\n"
"    border: 2px solid  black;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#menu_frame QPushButton{\n"
"    background-color: rgb(27, 33, 37);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#analyse_frame_btns QPushButton{\n"
"    background-color: rgb(27, 33, 37);\n"
"    border-radius: 15px;\n"
"}\n"
"#analyse_frame_btns QPushButton::hover, #menu_frame QPushButton::hover{\n"
"   background-color: black;\n"
"}\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setMouseTracking(False)
        self.frame.setTabletTracking(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images_fin/images_final/bpkey.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_3)
        self.menu_frame = QtWidgets.QFrame(self.frame)
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.go_to_analyses_btn = QtWidgets.QPushButton(self.menu_frame)
        self.go_to_analyses_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.go_to_analyses_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.go_to_analyses_btn.setFont(font)
        self.go_to_analyses_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons_fin/icons_final/analysis (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_to_analyses_btn.setIcon(icon1)
        self.go_to_analyses_btn.setObjectName("go_to_analyses_btn")
        self.verticalLayout_2.addWidget(self.go_to_analyses_btn)
        self.go_to_library_btn = QtWidgets.QPushButton(self.menu_frame)
        self.go_to_library_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.go_to_library_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.go_to_library_btn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons_fin/icons_final/library-books.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_to_library_btn.setIcon(icon2)
        self.go_to_library_btn.setObjectName("go_to_library_btn")
        self.verticalLayout_2.addWidget(self.go_to_library_btn)
        self.verticalLayout.addWidget(self.menu_frame)
        self.size_grip_left_1 = QtWidgets.QFrame(self.frame)
        self.size_grip_left_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip_left_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip_left_1.setObjectName("size_grip_left_1")
        self.verticalLayout.addWidget(self.size_grip_left_1)
        self.size_grip_left_2 = QtWidgets.QFrame(self.frame)
        self.size_grip_left_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip_left_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip_left_2.setObjectName("size_grip_left_2")
        self.verticalLayout.addWidget(self.size_grip_left_2)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName("stackedWidget")
        self.analyse_page = QtWidgets.QWidget()
        self.analyse_page.setObjectName("analyse_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.analyse_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.analyse_page)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.analyse_label = QtWidgets.QLabel(self.frame_7)
        self.analyse_label.setText("")
        self.analyse_label.setPixmap(QtGui.QPixmap(":/images_fin/images_final/analyse.png"))
        self.analyse_label.setScaledContents(True)
        self.analyse_label.setObjectName("analyse_label")
        self.verticalLayout_7.addWidget(self.analyse_label)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.analyse_frame = QtWidgets.QFrame(self.analyse_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyse_frame.sizePolicy().hasHeightForWidth())
        self.analyse_frame.setSizePolicy(sizePolicy)
        self.analyse_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analyse_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyse_frame.setObjectName("analyse_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.analyse_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.analyse_frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.note_label_image = QtWidgets.QLabel(self.frame_9)
        self.note_label_image.setMinimumSize(QtCore.QSize(218, 218))
        self.note_label_image.setMaximumSize(QtCore.QSize(218, 218))
        self.note_label_image.setText("")
        self.note_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/note.png"))
        self.note_label_image.setScaledContents(True)
        self.note_label_image.setObjectName("note_label_image")
        self.verticalLayout_8.addWidget(self.note_label_image)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.info_frame = QtWidgets.QFrame(self.analyse_frame)
        self.info_frame.setMinimumSize(QtCore.QSize(218, 218))
        self.info_frame.setMaximumSize(QtCore.QSize(218, 218))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.info_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.key_label_image = QtWidgets.QLabel(self.info_frame)
        self.key_label_image.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.key_label_image.setFont(font)
        self.key_label_image.setText("")
        self.key_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/key.png"))
        self.key_label_image.setScaledContents(True)
        self.key_label_image.setObjectName("key_label_image")
        self.gridLayout.addWidget(self.key_label_image, 2, 0, 1, 1)
        self.name_label_image = QtWidgets.QLabel(self.info_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.name_label_image.setFont(font)
        self.name_label_image.setText("")
        self.name_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/name.png"))
        self.name_label_image.setScaledContents(True)
        self.name_label_image.setObjectName("name_label_image")
        self.gridLayout.addWidget(self.name_label_image, 0, 0, 1, 1)
        self.bpm_label_image = QtWidgets.QLabel(self.info_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.bpm_label_image.setFont(font)
        self.bpm_label_image.setText("")
        self.bpm_label_image.setPixmap(QtGui.QPixmap(":/images_fin/images_final/bpm.png"))
        self.bpm_label_image.setScaledContents(True)
        self.bpm_label_image.setObjectName("bpm_label_image")
        self.gridLayout.addWidget(self.bpm_label_image, 1, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(self.info_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 1, 1, 1)
        self.bpm_label = QtWidgets.QLabel(self.info_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.bpm_label.setFont(font)
        self.bpm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bpm_label.setObjectName("bpm_label")
        self.gridLayout.addWidget(self.bpm_label, 1, 1, 1, 1)
        self.key_label = QtWidgets.QLabel(self.info_frame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.key_label.setFont(font)
        self.key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label.setObjectName("key_label")
        self.gridLayout.addWidget(self.key_label, 2, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.info_frame)
        self.verticalLayout_6.addWidget(self.analyse_frame)
        self.analyse_frame_btns = QtWidgets.QFrame(self.analyse_page)
        self.analyse_frame_btns.setMinimumSize(QtCore.QSize(0, 60))
        self.analyse_frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analyse_frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analyse_frame_btns.setObjectName("analyse_frame_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.analyse_frame_btns)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_file_btn = QtWidgets.QPushButton(self.analyse_frame_btns)
        self.open_file_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.open_file_btn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons_fin/icons_final/upload-folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_file_btn.setIcon(icon3)
        self.open_file_btn.setObjectName("open_file_btn")
        self.horizontalLayout_3.addWidget(self.open_file_btn)
        self.analyse_btn = QtWidgets.QPushButton(self.analyse_frame_btns)
        self.analyse_btn.setEnabled(False)
        self.analyse_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.analyse_btn.setStyleSheet("background-color: grey;")
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        self.analyse_btn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons_fin/icons_final/setting.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analyse_btn.setIcon(icon4)
        self.analyse_btn.setObjectName("analyse_btn")
        self.horizontalLayout_3.addWidget(self.analyse_btn)
        self.verticalLayout_6.addWidget(self.analyse_frame_btns)
        self.stackedWidget.addWidget(self.analyse_page)
        self.library_page = QtWidgets.QWidget()
        self.library_page.setObjectName("library_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.library_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.library_page)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.library_label = QtWidgets.QLabel(self.frame_5)
        self.library_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(22)
        self.library_label.setFont(font)
        self.library_label.setText("")
        self.library_label.setPixmap(QtGui.QPixmap(":/images_fin/images_final/library.png"))
        self.library_label.setScaledContents(True)
        self.library_label.setObjectName("library_label")
        self.verticalLayout_5.addWidget(self.library_label, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignTop)
        self.frame_6 = QtWidgets.QFrame(self.library_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.library_page)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.size_grip_right_1 = QtWidgets.QFrame(self.frame_2)
        self.size_grip_right_1.setMinimumSize(QtCore.QSize(0, 135))
        self.size_grip_right_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip_right_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip_right_1.setObjectName("size_grip_right_1")
        self.verticalLayout_3.addWidget(self.size_grip_right_1)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.go_to_analyses_btn.setText(_translate("MainWindow", "Analyse Audio"))
        self.go_to_library_btn.setText(_translate("MainWindow", "Your Library"))
        self.name_label.setText(_translate("MainWindow", "Unknown"))
        self.bpm_label.setText(_translate("MainWindow", "Unknown"))
        self.key_label.setText(_translate("MainWindow", "Unknown"))
        self.open_file_btn.setText(_translate("MainWindow", "Open Audio File"))
        self.analyse_btn.setText(_translate("MainWindow", "Analyse"))

    def connections(self):
            self.open_file_btn.clicked.connect(lambda: p.open_file(p, self.name_label, self.analyse_btn))
            self.go_to_analyses_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
            self.go_to_library_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
            self.analyse_btn.clicked.connect(lambda: p.analyse(p, self.bpm_label, self.key_label))