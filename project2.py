# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SessionUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.true_counter = QtWidgets.QLabel(self.centralwidget)
        self.true_counter.setGeometry(QtCore.QRect(10, 380, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.true_counter.setFont(font)
        self.true_counter.setStyleSheet("background-color: rgb(0, 188, 0);\n"
"color: rgb(0, 0, 227);")
        self.true_counter.setScaledContents(False)
        self.true_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.true_counter.setObjectName("true_counter")
        self.false_counter = QtWidgets.QLabel(self.centralwidget)
        self.false_counter.setGeometry(QtCore.QRect(250, 380, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.false_counter.setFont(font)
        self.false_counter.setStyleSheet("background-color: rgb(203, 0, 0);\n"
"color: rgb(227, 227, 227);")
        self.false_counter.setScaledContents(False)
        self.false_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.false_counter.setObjectName("false_counter")
        self.answer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.answer_btn.setGeometry(QtCore.QRect(240, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.answer_btn.setFont(font)
        self.answer_btn.setObjectName("answer_btn")
        self.instr_lbl = QtWidgets.QLabel(self.centralwidget)
        self.instr_lbl.setGeometry(QtCore.QRect(30, 80, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.instr_lbl.setFont(font)
        self.instr_lbl.setObjectName("instr_lbl")
        self.question_lbl = QtWidgets.QLabel(self.centralwidget)
        self.question_lbl.setGeometry(QtCore.QRect(30, 120, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.question_lbl.setFont(font)
        self.question_lbl.setObjectName("question_lbl")
        self.finish_btn = QtWidgets.QPushButton(self.centralwidget)
        self.finish_btn.setGeometry(QtCore.QRect(150, 380, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.finish_btn.setFont(font)
        self.finish_btn.setObjectName("finish_btn")
        self.error_lbl = QtWidgets.QLabel(self.centralwidget)
        self.error_lbl.setGeometry(QtCore.QRect(30, 250, 351, 31))
        font = QtGui.QFont()
        font.setFamily("NovemberPro-Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error_lbl.setFont(font)
        self.error_lbl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.error_lbl.setStyleSheet("color: rgb(255, 0, 0);")
        self.error_lbl.setText("")
        self.error_lbl.setObjectName("error_lbl")
        self.answer_field = QtWidgets.QLineEdit(self.centralwidget)
        self.answer_field.setGeometry(QtCore.QRect(22, 180, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(15)
        self.answer_field.setFont(font)
        self.answer_field.setObjectName("answer_field")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
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
        self.true_counter.setText(_translate("MainWindow", "ПРАВИЛЬНЫХ ОТВЕТОВ: 0"))
        self.false_counter.setText(_translate("MainWindow", "НЕПРАВИЛЬНЫХ ОТВЕТОВ: 0"))
        self.answer_btn.setText(_translate("MainWindow", "Ок"))
        self.instr_lbl.setText(_translate("MainWindow", "Напишите вторую формуглагола:"))
        self.question_lbl.setText(_translate("MainWindow", "<слово>"))

