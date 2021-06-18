# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openbtn = QtWidgets.QPushButton(self.centralwidget)
        self.openbtn.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.openbtn.setFont(font)
        self.openbtn.setObjectName("openbtn")
        self.beginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.beginbtn.setGeometry(QtCore.QRect(230, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.beginbtn.setFont(font)
        self.beginbtn.setObjectName("beginbtn")
        self.recordbtn = QtWidgets.QPushButton(self.centralwidget)
        self.recordbtn.setGeometry(QtCore.QRect(120, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.recordbtn.setFont(font)
        self.recordbtn.setObjectName("recordbtn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 50, 1181, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.image_out = QtWidgets.QLabel(self.frame)
        self.image_out.setGeometry(QtCore.QRect(30, 50, 400, 400))
        self.image_out.setText("")
        self.image_out.setObjectName("image_out")
        self.data_out = QtWidgets.QLabel(self.frame)
        self.data_out.setGeometry(QtCore.QRect(480, 50, 651, 400))
        self.data_out.setText("")
        self.data_out.setObjectName("data_out")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
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
        self.openbtn.setText(_translate("MainWindow", "Open"))
        self.beginbtn.setText(_translate("MainWindow", "Begin"))
        self.recordbtn.setText(_translate("MainWindow", "Record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
