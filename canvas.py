# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import groupby
from re import A
import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph as pg
import matplotlib.pyplot as plt

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = FigureCanvas(Figure(figsize=(5, 3)))
        self.axes = self.view.figure.subplots()
        i=0
        
        
        
    def setupUi(self, MainWindow):
        self.file_path=""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
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
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 2, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 0, 1, 1)
        # self.view = QtWidgets.QGraphicsView(self.centralwidget)
        self.gridLayout_3.addWidget(self.view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        # self.graphicsView_2.setSizePolicy(sizePolicy)
        # self.graphicsView_2.setObjectName("graphicsView_2")
        # self.graphicsView_2 = pg.PlotWidget()
        self.gridLayout_3.addWidget(self.view, 0, 0, 1, 1)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1036, 26))
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
        self.pushButton_2.clicked.connect(self.save_pos)
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
        
        
      
    def plotfile(self):
        self.file1 = open('input.txt', 'w')
        x1=[0,0,1]
        y1=[0,1,0]
        x = np.linspace(0, 10, 100)
        
        self.i=0
        
        
        global a
        x1=[0,0,1]
        y1=[0,1,0]
        self.axes.plot(0*x, 0 * x + x, picker=5, label="a",pickradius=10)
        self.axes.plot(1*x, 1 * x + x, picker=5, label="b", pickradius=10)
        self.axes.plot(2*x, x + x, picker=5, label="c",pickradius=10)
        self.axes.plot(x*x, 0 * x + x, picker=5, label="d", pickradius=10)
        self.axes.plot(x + x, picker=5, label="e", pickradius=10)
        self.axes.plot(x, picker=5, label="f", pickradius=10)
        self.axes.plot(x, 0 * x + x, picker=5, label="g", pickradius=10) 
        self.axes.scatter(x1,y1)
        a=[]      
        
               
    
        def on_pick(event):
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
    
            # print (event.artist.get_label(),"clicked")
            # event.artist.set_visible(not event.artist.get_visible())    (for making selected lines invisible)
            event.artist.set_color("grey") #for greying out the selected lines
            event.artist.set_picker(False) #cannot be selected again
            self.view.figure.canvas.draw()
            

        self.view.figure.canvas.mpl_connect('pick_event', on_pick)
        
        
        
        def add_evt(event):
            a.append(event.artist.get_label())
    # print(a)
    
        def groupbylist(event): 
            global i 
            global x_cord
            global y_cord
            x_cord=round(event.xdata,2)
            y_cord=round(event.ydata,2)
            self.i=self.i+1
            print ("source",self.i,"->",a)
            print("position:",round(event.xdata,2),",", round(event.ydata,2))
            self.lineEdit_2.insert(str(round(event.xdata,2)))
            self.lineEdit_4.insert(str(round(event.ydata,2)))
            a.clear()
                
        
        self.view.figure.canvas.mpl_connect('pick_event',add_evt)
        self.view.figure.canvas.mpl_connect('button_release_event',groupbylist)
    def save_pos(self):
        # self.file1.write("source",self.i,"->",a, "position:",x_cord,",", y_cord)
        self.file1.write("source ")
        self.file1.write(str(self.i))
        self.file1.write(" ")
        self.file1.write(str(a))
        self.file1.write("position: ")
        self.file1.write(str(x_cord))
        self.file1.write(" ")
        self.file1.write(str( y_cord))
        self.file1.close()
        
        
        
        
    def load_file(self):
        options = QtWidgets.QFileDialog.Options()
        self.plotfile()
        options = options | QtWidgets.QFileDialog.DontUseNativeDialog
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Choose File", "",
            "Json files (*.json)",
            options=options)
        if self.file_path[0]:
            self.graphicsView.clear()
            self.fileLineEdit.clear()
            self.fileLineEdit.insert(self.file_path[0])

            # MODIFIED
            fileType = (self.file_path[0]).split(".")[-1]
            if fileType == "json":
                self.read_data_textfile(self.file_path[0])
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())










# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# from matplotlib.lines import Line2D
# from tkinter import messagebox

# # graph pick event
# def pickLine2D(event):
#     print('pick evnet')
#     global lines
#     artist = event.artist
#     if isinstance(artist, Line2D):
#         if artist in lines:
#             idx = lines.index(artist)
#             print(f'line idx : {idx}')

# # close window
# def _windowDestroy(root):
#     root.quit()
#     root.destroy()

# root = tk.Tk()
# root.geometry('700x500')
# root.title('graph window')
# root.protocol('WM_DELETE_WINDOW', lambda root=root: _windowDestroy(root))

# f = tk.Frame(root)
# f.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# # data of graph
# N = 2
# M = 10
# x = np.arange(M)
# np.random.seed(seed=0)
# lines = []

# # set graph
# fig = plt.figure(figsize=(4, 4))
# cvs = FigureCanvasTkAgg(fig, f)
# toolbar = NavigationToolbar2Tk(cvs, f)
# cvs.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# # set lien2D
# ax = fig.add_subplot(111)
# for i in range(N):
#     _y = np.random.rand(M)
#     line = Line2D(x, _y, picker=True, pickradius=10)
#     lines.append(line)
#     ax.add_line(line)
# ax.set_xlim((-0.5, M + 0.5))
# ax.set_ylim((0, 1.5))

# fig.canvas.mpl_connect('pick_event', pickLine2D)

# root.mainloop()