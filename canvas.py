# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import itertools
import mysql.connector
from scipy.spatial import distance
from sklearn.cluster import DBSCAN

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.collections import LineCollection
import numpy as np
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.cm import viridis_r
from matplotlib.colors import Normalize, LogNorm
import json

import scipy

try:
    import matplotlib.backends.backend_qtagg as qtbk
    from matplotlib.backends.backend_qtagg import (
        FigureCanvas,
        NavigationToolbar2QT as NavigationToolbar,
    )
except ModuleNotFoundError as e:
    print("Could not import qtagg. Trying qt5agg")

try:
    import matplotlib.backends.backend_qt5agg as qtbk
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas,
        NavigationToolbar2QT as NavigationToolbar,
    )
except ModuleNotFoundError as e:
    print("Could not import qt5agg. Quitting!")
    sys.exit()
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow_db(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(622, 710)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(240, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 450, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 280, 461, 167))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.layoutWidget_2 = QtWidgets.QWidget(self)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 70, 461, 169))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget_2)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_15.setEnabled(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15
        )
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_16.setClearButtonEnabled(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16
        )
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17
        )
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.timeEdit = QtWidgets.QTimeEdit(self.layoutWidget_2)
        self.timeEdit.setObjectName("timeEdit")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.timeEdit)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(230, 640, 161, 28))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(70, 490, 461, 131))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Database inputs"))
        self.label_3.setText(_translate("MainWindow", "Intersection table"))
        self.label_7.setText(_translate("MainWindow", "Delay table"))
        self.label_9.setText(_translate("MainWindow", "Observation id"))
        self.label_10.setText(_translate("MainWindow", "Baseline number"))
        self.label_11.setText(_translate("MainWindow", "Delay"))
        self.label_12.setText(_translate("MainWindow", "Peak Height"))
        self.label_13.setText(_translate("MainWindow", "Peak Width"))
        self.label_19.setText(_translate("MainWindow", "Observation id"))
        self.label_20.setText(_translate("MainWindow", "File name"))
        self.label_21.setText(_translate("MainWindow", "Direction"))
        self.label_22.setText(_translate("MainWindow", "Date"))
        self.label_23.setText(_translate("MainWindow", "Time"))
        self.label_8.setText(_translate("MainWindow", "Observation table"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_2.setText(_translate("MainWindow", "Observation id"))
        self.label_4.setText(_translate("MainWindow", "Labels"))
        self.label_5.setText(_translate("MainWindow", "X_intersection"))
        self.label_6.setText(_translate("MainWindow", "Y_intersection"))
        self.pushButton.clicked.connect(self.insert_in_db)

    def insert_in_db(
        self,
    ):  # works on save_posbutton to connect to mysql db and save the positions there
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password*",  # use password for mysql db
            database="gmrt",
        )
        print(mydb)
        mycursor = mydb.cursor()
        sql = "INSERT INTO observation (obs_id, file_name, direction, date, time) VALUES (%s, %s,%s, %s,%s)"
        val = (
            float(self.lineEdit_15.text()),
            self.lineEdit_16.text(),
            self.lineEdit_17.text(),
            self.dateEdit.text(),
            self.timeEdit.text(),
        )
        mycursor.execute(sql, val)
        sql1 = "INSERT INTO delay (obs_id, baseline_num, delay, peak_height, peak_width) VALUES (%s, %s,%s, %s,%s)"
        val1 = (
            float(self.lineEdit_15.text()),
            self.lineEdit_6.text(),
            self.lineEdit_7.text(),
            self.lineEdit_8.text(),
            self.lineEdit_9.text(),
        )
        mycursor.execute(sql1, val1)
        obj_instance = Ui_MainWindow()
        source = obj_instance.save_pos()
        sql2 = "INSERT INTO intersections (obs_id, labels, x_intersection, y_intersection) VALUES (%s, %s,%s, %s)"
        val2 = (
            float(self.lineEdit_15.text()),
            str(source),
            obj_instance.x,
            obj_instance.y,
        )
        mycursor.execute(sql2, val2)
        mydb.commit()
        self.lineEdit_5.setText((self.lineEdit_15.text()))
        self.lineEdit.setText(self.lineEdit_15.text())
        print(mycursor.rowcount, "record inserted.")


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):  # UI of the window
        super().__init__()
        self.view = FigureCanvas(Figure(figsize=(10, 6)))
        self.view.adjustSize()
        # self.w = None  # No external window yet
        self.toolbar = qtbk.NavigationToolbar2QT(self.view, self)
        MainWindow.addToolBar(self.toolbar)
        self.main_widget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.main_widget.setSizePolicy(sizePolicy)
        canvasSizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        self.view.setSizePolicy(canvasSizePolicy)
        self.toolbar.setSizePolicy(canvasSizePolicy)
        self.setCentralWidget(self.main_widget)

        self.axes = self.view.figure.subplots()

        self.axes.set_aspect("equal", adjustable="datalim")
        self.axes.set_box_aspect(1)

        self.axes.set_xlim([-1e4, 1e4])
        self.axes.set_ylim([-1e4, 1e4])
        i = 0
        self.a = []
        self.print_source = []
        self.SPEED_OF_LIGHT = 2.99792458e8
        self.filepath = ""
        self.sourceList = list()
        self.finalList = list()
        self.hyperbola_list = list()
        self.localList = list()
        self.x = float(0)
        self.y = float(0)
        # self.w = Ui_MainWindow_db()

    def setupUi(self, MainWindow):
        self.file_path = ""
        MainWindow.setObjectName("MainWindow")
        # MainWindow.setFixedSize(1151, 679) incase fixed size is needed
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.gridLayout_3.addWidget(self.view, 0, 0, 3, 1)

        self.gridLayout_3.setRowStretch(2, 0)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        v_widget = QWidget()
        v_widget.setLayout(self.verticalLayout_2)
        v_widget.setFixedWidth(350)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(v_widget, 0, 2, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 2, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)

        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1151, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menusettings = QtWidgets.QMenu(self.menubar)
        self.menusettings.setObjectName("menusettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menusettings.menuAction())

        self.pushButton.clicked.connect(self.load_file)
        # self.pushButton_2.clicked.connect(self.save_pos)
        self.pushButton_2.clicked.connect(self.window_db)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open file"))
        self.label.setText(_translate("MainWindow", "Intersection Positions"))
        self.label_2.setText(_translate("MainWindow", "X (East):"))
        self.label_4.setText(_translate("MainWindow", "Y (North):"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Positions"))
        self.label_8.setText(_translate("MainWindow", "(Upon Selection of a line)"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.pushButton_7.setText(_translate("MainWindow", "Undo"))
        self.pushButton_8.setText(_translate("MainWindow", "Save New File"))
        self.label_3.setText(_translate("MainWindow", "RFI Localization"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menusettings.setTitle(_translate("MainWindow", "settings"))

    def window_db(self):  # <===
        self.w = Ui_MainWindow_db()
        Ui_MainWindow.hide
        self.w.show()

    def plotfile(self, pos_dict, delay_dict):
        norm = Normalize(
            vmin=np.min(delay_dict["amplitude"]), vmax=np.max(delay_dict["amplitude"])
        )

        self.i = 0
        l = len(pos_dict)
        ants_used = []
        unique_ants = np.unique(ants_used)
        for i in unique_ants:  # scatter plot for antennas
            self.axes.scatter(pos_dict[i][0], pos_dict[i][1], color="g", marker="^")

        for i in range(0, l):  # scatter plot for antennas
            self.axes.scatter(pos_dict[i][0], pos_dict[i][1], color="g", marker="^")

        intersections = find_intersections(pos_dict, delay_dict, 1000)
        self.axes.scatter(
            [x for x, y in intersections],
            [y for x, y in intersections],
            color="red",
            marker="*",
            label="Intersections",
        )

        l = len(delay_dict)
        for i in range(0, l):
            baseline = delay_dict["baseline"][i]
            ant2 = (baseline - 65536) % 2048
            ant1 = ((baseline - 65536) - (ant2)) // 2048
            xyp = self.hyperbola(
                delay_dict["delay"][i],
                pos_dict[ant1][0],
                pos_dict[ant1][1],
                pos_dict[ant2][0],
                pos_dict[ant2][1],
                15000,
                1000,
            )  # self,delay_s, x0,x1,y0,y1, range, pts
            self.hyperbola_list.extend(
                [
                    (
                        delay_dict["delay"][i],
                        pos_dict[ant1][0],
                        pos_dict[ant1][1],
                        pos_dict[ant2][0],
                        pos_dict[ant2][1],
                    )
                ]
            )

            # print(self.hyperbola_list)
            strength = delay_dict["amplitude"][i]
            self.axes.plot(
                xyp[0, :], xyp[1, :], alpha=0, picker=5, label=i, pickradius=5
            )
            lwidths = 1 + (xyp[2, :])
            points = np.array([xyp[0, :], xyp[1, :]]).T.reshape(-1, 1, 2)
            segments = np.concatenate([points[:-1], points[1:]], axis=1)

            # code to calculate the segment weights
            segment_weights = np.convolve(xyp[2, :], np.ones(2) / 2, "valid")
            alpha_norm = LogNorm(
                vmin=np.min(1 / segment_weights), vmax=np.max(1 / segment_weights)
            )

            colors = viridis_r(norm(strength * np.ones(len(segments))))
            colors[:, 3] = alpha_norm(1 / segment_weights)

            lc = LineCollection(
                segments, linewidths=lwidths, color=colors, norm=plt.Normalize(0, 10)
            )

            self.axes.add_collection(lc)
        self.view.figure.canvas.draw()

        def on_press(event):
            # for greying out the selected lines
            event.artist.set_color("blue")
            event.artist.set_picker(True)  # cannot be selected again
            self.view.figure.canvas.draw()

        def on_pick(event):
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            self.a.append(event.artist.get_label())
            # print (event.artist.get_label(),"clicked")
            # event.artist.set_visible(not event.artist.get_visible())    (for making selected lines invisible)
            # for greying out the selected lines
            event.artist.set_color("lightgrey")
            event.artist.set_alpha(0.5)
            event.artist.set_picker(False)  # cannot be selected again
            self.view.figure.canvas.draw()

        self.view.figure.canvas.mpl_connect("pick_event", on_pick)
        self.view.figure.canvas.mpl_connect("key_press_event", on_press)

        def groupbylist(event):
            if (self.view.figure.canvas.cursor().shape()) == 0:
                self.print_source = []

                self.i = self.i + 1

                print("source", self.i, "->", self.a)
                self.sourceList.extend(
                    [
                        "source",
                        self.i,
                        "->",
                        self.print_source,
                        "position:",
                        round(event.xdata, 2),
                        round(event.ydata, 2),
                    ]
                )
                self.x = round(event.xdata, 2)
                self.y = round(event.ydata, 2)
                self.localList.append(self.sourceList)
                self.finalList = self.localList
                self.sourceList = []
                self.print_source += self.a
                # print(self.localList)

                print("position:", round(event.xdata, 2), ",", round(event.ydata, 2))
                self.lineEdit_2.insert(str(round(event.xdata, 2)))
                self.lineEdit_4.insert(str(round(event.ydata, 2)))

                self.a.clear()

        self.view.figure.canvas.mpl_connect("button_release_event", groupbylist)

    def save_pos(self):
        # self.insert_in_db()
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle("Save File")
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dialog.setOption(QtWidgets.QFileDialog.DontConfirmOverwrite, True)
        dialog.setNameFilters(["Text files (*.txt)", "Excel sheets (*.xlsx)"])
        dialog.setDefaultSuffix(".txt")
        dialog.exec_()

        if dialog.selectedFiles():
            fileType = (dialog.selectedFiles()[0]).split(".")[-1]

            if fileType == "txt":
                try:
                    file = open(dialog.selectedFiles()[0], "r")
                    writeData = file.read()
                    file.close()
                except FileNotFoundError:
                    writeData = self.finalList

            file = open(dialog.selectedFiles()[0], "w")
            file.write(json.dumps(writeData))
            file.close()
            source_db = self.print_source
            return source_db
        self.print_source.clear()

    def load_file(self):
        options = QtWidgets.QFileDialog.Options()

        options = options | QtWidgets.QFileDialog.DontUseNativeDialog
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Choose File", "", "npz files (*.npz)", options=options
        )
        if self.file_path[0]:
            self.lineEdit.clear()
            self.lineEdit.insert(self.file_path[0])

            # MODIFIED
            fileType = (self.file_path[0]).split(".")[-1]
            if fileType == "npz":
                data = np.load(self.file_path[0])
                print(data.files)
                print(data["delays"])
                print(data["positions"])
                ant2 = (106521 - 65536) % 2048
                ant1 = ((106521 - 65536) - (ant2)) // 2048
                print(ant2, ant1)
                # self.plotfile()
                self.plotfile(data["positions"], data["delays"])
            # print(data_dict["delays"]["baselines"][0])

    def hyperbola(self, delay_s, x0, x1, y0, y1, range, pts):
        """
        Plots a hyperbola with positions p0 = (x0, y0) and p1 = (x1, y1) as the foci.
        The delay is defined in seconds of light travel time such that positive --> closer to p0.
        """
        # x0, y0 = p0  # position in meteres
        # x1, y1 = p1  # position in meters
        speed_of_l = 2.99792458e8
        angle = np.pi - np.arctan2((y1 - y0), (x1 - x0))

        c = np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) / 2
        a = delay_s * speed_of_l / 2  # convert from seconds to meters

        xy = cartesian_hyperbola(c, a, range, pts)

        # shift the focus from (c, 0) to origin.
        xy[0, :] -= c

        # rotate to p1 -> p0 angle.
        rot = np.array(
            [[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]]
        )

        xyp = np.zeros_like(xy)

        xyp[0:2, :] = np.matmul(rot, xy[0:2, :])

        xyp[2, :] = xy[2, :]  # copy weights

        # shift origin to p0
        xyp[0, :] += x0
        xyp[1, :] += y0

        return xyp
        # print(xyp)


def hyperbola(delay_s, x0, x1, y0, y1, range, pts):
    """
    Plots a hyperbola with positions p0 = (x0, y0) and p1 = (x1, y1) as the foci.
    The delay is defined in seconds of light travel time such that positive --> closer to p0.
    """
    # x0, y0 = p0  # position in meteres
    # x1, y1 = p1  # position in meters
    speed_of_l = 2.99792458e8
    angle = np.pi - np.arctan2((y1 - y0), (x1 - x0))

    c = np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) / 2
    a = delay_s * speed_of_l / 2  # convert from seconds to meters

    xy = cartesian_hyperbola(c, a, range, pts)

    # shift the focus from (c, 0) to origin.
    xy[0, :] -= c

    # rotate to p1 -> p0 angle.
    rot = np.array([[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]])

    xyp = np.zeros_like(xy)

    xyp[0:2, :] = np.matmul(rot, xy[0:2, :])

    xyp[2, :] = xy[2, :]  # copy weights

    # shift origin to p0
    xyp[0, :] += x0
    xyp[1, :] += y0

    return xyp


def cartesian_hyperbola(c, a, range, pts):
    """
    Returns a hyperbola around the focus at (c,0). The other focus is at (-c,0)
    """
    y = np.linspace(-range, range, pts, endpoint=True)
    b = np.sqrt(abs(c**2 - a**2))
    x = a * np.sqrt(1 + y**2 / b**2)
    d1 = np.sqrt(y**2 + (x - c) ** 2)  # distance from one focus
    d2 = np.sqrt(y**2 + (x + c) ** 2)  # distance from other focus
    scaling_factor = 25e6  # assume a typical distance scale of 5000m
    w = (d1 * d2) / scaling_factor
    # w=scaling_factor/(d1*d2)

    return np.vstack([x, y, w])
    # print(xyp)


def find_intersections(
    positions, delays, range_pts
):  # trial function for finding approximate rfi sources
    intersections = []
    for i in range(len(delays)):
        baseline_number1 = delays["baseline"][i]
        ant2_1 = (baseline_number1 - 65536) % 2048
        ant1_1 = ((baseline_number1 - 65536) - (ant2_1)) // 2048
        x0, y0, z0 = positions[ant1_1]
        x1, y1, z1 = positions[ant2_1]
        delay_s = delays["delay"][i]
        hyperbola1 = hyperbola(delay_s, x0, x1, y0, y1, 15000, 1000)
        for j in range(i + 1, len(delays)):
            baseline_number2 = delays["baseline"][j]
            ant2_2 = (baseline_number2 - 65536) % 2048
            ant1_2 = ((baseline_number2 - 65536) - (ant2_2)) // 2048
            # if ant1_2 == ant1_1 or ant2_2 == ant2_1 or ant2_2 == ant1_1 or ant1_2 == ant2_1:
            #     continue
            x0, y0, z0 = positions[ant1_2]
            x1, y1, z1 = positions[ant2_2]
            delay_s = delays["delay"][i]
            # print(delay_s)
            hyperbola2 = hyperbola(delay_s, x0, x1, y0, y1, 15000, 1000)
            dists = distance.cdist(hyperbola1[:2].T, hyperbola2[:2].T)

            min_dist_idx = np.unravel_index(np.argmin(dists), dists.shape)
            if dists[min_dist_idx] < 10:
                intersections.append(
                    (
                        (
                            hyperbola1[:2].T[min_dist_idx[0]]
                            + hyperbola2[:2].T[min_dist_idx[0]]
                        )
                        / 2
                    ).tolist()
                )
    intersections = np.array(intersections)
    print((intersections))

    clustering = DBSCAN(eps=range_pts).fit(intersections)
    RFI_sources = []
    for label in set(clustering.labels_):
        if label == -1:
            continue
        cluster_points = intersections[clustering.labels_ == label]
        RFI_sources.append(cluster_points.mean(axis=0).tolist())
    return intersections


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
