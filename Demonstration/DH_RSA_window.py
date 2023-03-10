# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DH_RSA_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Alice_image = QtWidgets.QLabel(self.centralwidget)
        self.Alice_image.setGeometry(QtCore.QRect(30, 100, 141, 141))
        self.Alice_image.setText("")
        self.Alice_image.setPixmap(QtGui.QPixmap("Image/coding (1).png"))
        self.Alice_image.setScaledContents(True)
        self.Alice_image.setObjectName("Alice_image")
        self.Bob_image = QtWidgets.QLabel(self.centralwidget)
        self.Bob_image.setGeometry(QtCore.QRect(620, 100, 141, 141))
        self.Bob_image.setText("")
        self.Bob_image.setPixmap(QtGui.QPixmap("Image/coding.png"))
        self.Bob_image.setScaledContents(True)
        self.Bob_image.setObjectName("Bob_image")
        self.message_image = QtWidgets.QLabel(self.centralwidget)
        self.message_image.setGeometry(QtCore.QRect(150, 190, 41, 41))
        self.message_image.setText("")
        self.message_image.setPixmap(QtGui.QPixmap("Image/envelope.png"))
        self.message_image.setScaledContents(True)
        self.message_image.setObjectName("message_image")
        self.Alice_name = QtWidgets.QLabel(self.centralwidget)
        self.Alice_name.setGeometry(QtCore.QRect(70, 80, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Alice_name.setFont(font)
        self.Alice_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Alice_name.setObjectName("Alice_name")
        self.Bob_name = QtWidgets.QLabel(self.centralwidget)
        self.Bob_name.setGeometry(QtCore.QRect(660, 80, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Bob_name.setFont(font)
        self.Bob_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Bob_name.setObjectName("Bob_name")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 250, 172, 52))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.AliceProperties = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.AliceProperties.setContentsMargins(0, 0, 0, 0)
        self.AliceProperties.setObjectName("AliceProperties")
        self.PKey_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.PKey_label.setObjectName("PKey_label")
        self.AliceProperties.addWidget(self.PKey_label, 0, 0, 1, 1)
        self.A_PKey_input = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.A_PKey_input.setObjectName("A_PKey_input")
        self.AliceProperties.addWidget(self.A_PKey_input, 0, 1, 1, 1)
        self.A_number_e = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.A_number_e.setObjectName("A_number_e")
        self.AliceProperties.addWidget(self.A_number_e, 1, 0, 1, 1)
        self.Number_e = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.Number_e.setObjectName("Number_e")
        self.AliceProperties.addWidget(self.Number_e, 1, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(610, 250, 172, 52))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.BobProperties = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.BobProperties.setContentsMargins(0, 0, 0, 0)
        self.BobProperties.setObjectName("BobProperties")
        self.B_PKey_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.B_PKey_label.setObjectName("B_PKey_label")
        self.BobProperties.addWidget(self.B_PKey_label, 0, 0, 1, 1)
        self.B_PKey_input = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.B_PKey_input.setObjectName("B_PKey_input")
        self.BobProperties.addWidget(self.B_PKey_input, 0, 1, 1, 1)
        self.B_number_e = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.B_number_e.setObjectName("B_number_e")
        self.BobProperties.addWidget(self.B_number_e, 1, 0, 1, 1)
        self.Number_e_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Number_e_2.setObjectName("Number_e_2")
        self.BobProperties.addWidget(self.Number_e_2, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 320, 201, 141))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 180, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Q_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Q_label.setObjectName("Q_label")
        self.gridLayout.addWidget(self.Q_label, 1, 0, 1, 1)
        self.P_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.P_input.setObjectName("P_input")
        self.gridLayout.addWidget(self.P_input, 0, 1, 1, 1)
        self.X_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.X_input.setObjectName("X_input")
        self.gridLayout.addWidget(self.X_input, 2, 1, 1, 1)
        self.G_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.G_input.setObjectName("G_input")
        self.gridLayout.addWidget(self.G_input, 3, 1, 1, 1)
        self.G_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.G_label.setObjectName("G_label")
        self.gridLayout.addWidget(self.G_label, 3, 0, 1, 1)
        self.Q_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Q_input.setObjectName("Q_input")
        self.gridLayout.addWidget(self.Q_input, 1, 1, 1, 1)
        self.X_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.X_label.setObjectName("X_label")
        self.gridLayout.addWidget(self.X_label, 2, 0, 1, 1)
        self.P_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.P_label.setObjectName("P_label")
        self.gridLayout.addWidget(self.P_label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 470, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 320, 201, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.logLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.logLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logLayout_2.setObjectName("logLayout_2")
        self.logLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logLabel_2.setFont(font)
        self.logLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.logLabel_2.setObjectName("logLabel_2")
        self.logLayout_2.addWidget(self.logLabel_2)
        self.Log_2 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.Log_2.setObjectName("Log_2")
        self.logLayout_2.addWidget(self.Log_2)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(620, 470, 121, 41))
        self.backButton.setObjectName("backButton")
        self.message_image.raise_()
        self.label.raise_()
        self.Alice_image.raise_()
        self.Bob_image.raise_()
        self.Alice_name.raise_()
        self.Bob_name.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.verticalLayoutWidget.raise_()
        self.backButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Diffie-Hellman Integrated RSA"))
        self.Alice_name.setText(_translate("MainWindow", "Alice"))
        self.Bob_name.setText(_translate("MainWindow", "Bob"))
        self.PKey_label.setText(_translate("MainWindow", "Private key:"))
        self.A_number_e.setText(_translate("MainWindow", "Random number e:"))
        self.B_PKey_label.setText(_translate("MainWindow", "Private key:"))
        self.B_number_e.setText(_translate("MainWindow", "Random number e:"))
        self.groupBox.setTitle(_translate("MainWindow", "Public keys"))
        self.Q_label.setText(_translate("MainWindow", "Prime number q:"))
        self.G_label.setText(_translate("MainWindow", "Generator number g:"))
        self.X_label.setText(_translate("MainWindow", "Prime numer X:"))
        self.P_label.setText(_translate("MainWindow", "Prime number p:"))
        self.pushButton.setText(_translate("MainWindow", "Start exchange key"))
        self.logLabel_2.setText(_translate("MainWindow", "Log"))
        self.backButton.setText(_translate("MainWindow", "Back to main menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
