import pygame
from PyQt5 import QtCore, QtWidgets
from tkinter import Tk
from tkinter.filedialog import askopenfilename




class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Play = QtWidgets.QPushButton(Dialog)
        self.Play.setGeometry(QtCore.QRect(160, 50, 75, 23))
        self.Play.setObjectName("Play")
        self.Play.clicked.connect(self.Playmusic)

        self.Stop = QtWidgets.QPushButton(Dialog)
        self.Stop.setGeometry(QtCore.QRect(160, 110, 75, 23))
        self.Stop.setObjectName("Stop")
        self.Stop.clicked.connect(self.Stopmusic)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 101, 21))
        self.label.setObjectName("label")


        self.Pause = QtWidgets.QPushButton(Dialog)
        self.Pause.setGeometry(QtCore.QRect(160, 80, 75, 23))
        self.Pause.setObjectName("Pause")
        self.Pause.clicked.connect(self.Pausemusic)

        self.Unpause = QtWidgets.QPushButton(Dialog)
        self.Unpause.setGeometry(QtCore.QRect(60, 80, 75, 23))
        self.Unpause.setObjectName("Pause")
        self.Unpause.clicked.connect(self.Unpausemusic)

        self.Openf = QtWidgets.QPushButton(Dialog)
        self.Openf.setGeometry(QtCore.QRect(260, 80, 75, 23))
        self.Openf.setObjectName("Openfile")
        self.Openf.clicked.connect(self.Openfile)


        self.Mute = QtWidgets.QPushButton(Dialog)
        self.Mute.setGeometry(QtCore.QRect(10, 220, 75, 23))
        self.Mute.setObjectName("Mute")
        self.Mute.clicked.connect(self.Set_mute)

        self.twentyfive = QtWidgets.QPushButton(Dialog)
        self.twentyfive.setGeometry(QtCore.QRect(90, 220, 35, 23))
        self.twentyfive.setObjectName("25%")
        self.twentyfive.clicked.connect(self.Set_twentyfive)

        self.fifty = QtWidgets.QPushButton(Dialog)
        self.fifty.setGeometry(QtCore.QRect(130, 220, 35, 23))
        self.fifty.setObjectName("50%")
        self.fifty.clicked.connect(self.Set_fifty)

        self.seventyfive = QtWidgets.QPushButton(Dialog)
        self.seventyfive.setGeometry(QtCore.QRect(170, 220, 35, 23))
        self.seventyfive.setObjectName("75%")
        self.seventyfive.clicked.connect(self.Set_Seventyfive)

        self.onehundred = QtWidgets.QPushButton(Dialog)
        self.onehundred.setGeometry(QtCore.QRect(210, 220, 35, 23))
        self.onehundred.setObjectName("100%")
        self.onehundred.clicked.connect(self.Set_onehundred)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MP3"))
        self.Play.setText(_translate("Dialog", "Play"))
        self.Stop.setText(_translate("Dialog", "Stop"))
        self.label.setText(_translate("Dialog", "MP3 PLAYER"))
        self.Pause.setText(_translate("Dialog", "Pause"))
        self.Mute.setText(_translate("Dialog", "Mute"))
        self.Unpause.setText(_translate("Dialog", "Unpause"))
        self.twentyfive.setText(_translate("Dialog", "25%"))
        self.fifty.setText(_translate("Dialog", "50%"))
        self.seventyfive.setText(_translate("Dialog", "75%"))
        self.onehundred.setText(_translate("Dialog", "100%"))
        self.Openf.setText(_translate("Dialog", "Open File"))

    def Openfile(self):
        Tk().withdraw()
        global filename
        filename = askopenfilename()
        print(filename)

    def Playmusic(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def Stopmusic(self):
        pygame.mixer.music.stop()

    def Pausemusic(self):
        pygame.mixer.music.pause()

    def Unpausemusic(self):
        pygame.mixer.music.unpause()

    def Set_mute(self):
        pygame.mixer.music.set_volume(0)

    def Set_twentyfive(self):
        pygame.mixer.music.set_volume(0.25)

    def Set_fifty(self):
        pygame.mixer.music.set_volume(0.50)

    def Set_Seventyfive(self):
        pygame.mixer.music.set_volume(0.75)

    def Set_onehundred(self):
        pygame.mixer.music.set_volume(100)



_name_ = "_main_"

if _name_ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditText = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(EditText)
    EditText.show()
    sys.exit(app.exec_())
