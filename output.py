from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 414)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 311, 71))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(11, 246, 75, 41))
        self.pushButton_10.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(11, 311, 75, 41))
        self.pushButton_2.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(11, 116, 71, 41))
        self.pushButton.setStyleSheet("background-color: rgb(163, 163, 163);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(173, 116, 71, 41))
        self.pushButton_8.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(173, 246, 75, 41))
        self.pushButton_14.setStyleSheet("background: rgb(163, 163, 163)\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(254, 181, 71, 41))
        self.pushButton_7.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(173, 311, 75, 41))
        self.pushButton_9.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(254, 116, 71, 41))
        self.pushButton_3.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(92, 246, 75, 41))
        self.pushButton_11.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(11, 181, 75, 41))
        self.pushButton_5.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(254, 311, 71, 41))
        self.pushButton_4.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(173, 181, 75, 41))
        self.pushButton_6.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(254, 246, 71, 41))
        self.pushButton_15.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(92, 116, 71, 41))
        self.pushButton_12.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(92, 311, 75, 41))
        self.pushButton_16.setStyleSheet("background: rgb(163, 163, 163)")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(92, 181, 75, 41))
        self.pushButton_13.setStyleSheet("background: rgb(163, 163, 163)\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 337, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_10.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "9"))
        self.pushButton_14.setText(_translate("MainWindow", "3"))
        self.pushButton_7.setText(_translate("MainWindow", "*"))
        self.pushButton_9.setText(_translate("MainWindow", "="))
        self.pushButton_3.setText(_translate("MainWindow", "/"))
        self.pushButton_11.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))
        self.pushButton_12.setText(_translate("MainWindow", "8"))
        self.pushButton_16.setText(_translate("MainWindow", "C"))
        self.pushButton_13.setText(_translate("MainWindow", "5"))
