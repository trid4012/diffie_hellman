# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MITM_window.ui'
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 250, 160, 31))
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
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(610, 250, 160, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.BobProperties = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.BobProperties.setContentsMargins(0, 0, 0, 0)
        self.BobProperties.setObjectName("BobProperties")
        self.B_PKey_input = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.B_PKey_input.setObjectName("B_PKey_input")
        self.BobProperties.addWidget(self.B_PKey_input, 0, 1, 1, 1)
        self.B_PKey_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.B_PKey_label.setObjectName("B_PKey_label")
        self.BobProperties.addWidget(self.B_PKey_label, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 320, 201, 91))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 180, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.G_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.G_input.setObjectName("G_input")
        self.gridLayout.addWidget(self.G_input, 1, 1, 1, 1)
        self.p_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.p_label.setObjectName("p_label")
        self.gridLayout.addWidget(self.p_label, 0, 0, 1, 1)
        self.G_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.G_label.setObjectName("G_label")
        self.gridLayout.addWidget(self.G_label, 1, 0, 1, 1)
        self.p_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.p_input.setObjectName("p_input")
        self.gridLayout.addWidget(self.p_input, 0, 1, 1, 1)
        self.Eve_label = QtWidgets.QLabel(self.centralwidget)
        self.Eve_label.setGeometry(QtCore.QRect(340, 100, 131, 141))
        self.Eve_label.setText("")
        self.Eve_label.setPixmap(QtGui.QPixmap("Image/hacker.png"))
        self.Eve_label.setScaledContents(True)
        self.Eve_label.setObjectName("Eve_label")
        self.Eve_name = QtWidgets.QLabel(self.centralwidget)
        self.Eve_name.setGeometry(QtCore.QRect(380, 80, 49, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Eve_name.setFont(font)
        self.Eve_name.setAlignment(QtCore.Qt.AlignCenter)
        self.Eve_name.setObjectName("Eve_name")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 430, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.E_A_PKey_input = QtWidgets.QLineEdit(self.centralwidget)
        self.E_A_PKey_input.setGeometry(QtCore.QRect(297, 90, 51, 22))
        self.E_A_PKey_input.setObjectName("E_A_PKey_input")
        self.E_A_PKey_label = QtWidgets.QLabel(self.centralwidget)
        self.E_A_PKey_label.setGeometry(QtCore.QRect(170, 90, 121, 22))
        self.E_A_PKey_label.setObjectName("E_A_PKey_label")
        self.E_B_PKey_input = QtWidgets.QLineEdit(self.centralwidget)
        self.E_B_PKey_input.setGeometry(QtCore.QRect(580, 90, 51, 22))
        self.E_B_PKey_input.setObjectName("E_B_PKey_input")
        self.E_B_PKey_label = QtWidgets.QLabel(self.centralwidget)
        self.E_B_PKey_label.setGeometry(QtCore.QRect(455, 90, 121, 22))
        self.E_B_PKey_label.setObjectName("E_B_PKey_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 310, 201, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.logLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.logLayout.setContentsMargins(0, 0, 0, 0)
        self.logLayout.setObjectName("logLayout")
        self.logLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logLabel.setFont(font)
        self.logLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logLabel.setObjectName("logLabel")
        self.logLayout.addWidget(self.logLabel)
        self.Log = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.Log.setObjectName("Log")
        self.logLayout.addWidget(self.Log)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(350, 490, 121, 41))
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
        self.Eve_label.raise_()
        self.Eve_name.raise_()
        self.pushButton.raise_()
        self.E_A_PKey_input.raise_()
        self.E_A_PKey_label.raise_()
        self.E_B_PKey_input.raise_()
        self.E_B_PKey_label.raise_()
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
        self.label.setText(_translate("MainWindow", "Man-in-the-middle Attack"))
        self.Alice_name.setText(_translate("MainWindow", "Alice"))
        self.Bob_name.setText(_translate("MainWindow", "Bob"))
        self.PKey_label.setText(_translate("MainWindow", "Private key:"))
        self.B_PKey_label.setText(_translate("MainWindow", "Private key:"))
        self.groupBox.setTitle(_translate("MainWindow", "Public keys"))
        self.p_label.setText(_translate("MainWindow", "Prime numer p:"))
        self.G_label.setText(_translate("MainWindow", "Generator number g:"))
        self.Eve_name.setText(_translate("MainWindow", "Eve"))
        self.pushButton.setText(_translate("MainWindow", "Start exchange key"))
        self.E_A_PKey_label.setText(_translate("MainWindow", "Alice - Eve private key:"))
        self.E_B_PKey_label.setText(_translate("MainWindow", "Bob - Eve private key:"))
        self.logLabel.setText(_translate("MainWindow", "Log"))
        self.backButton.setText(_translate("MainWindow", "Back to main menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
