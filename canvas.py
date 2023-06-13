# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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

try:
    import matplotlib.backends.backend_qtagg as qtbk
    from matplotlib.backends.backend_qtagg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
except ModuleNotFoundError as e:
    print("Could not import qtagg. Trying qt5agg")

try:
    import matplotlib.backends.backend_qt5agg as qtbk
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
except ModuleNotFoundError as e:
    print("Could not import qt5agg. Quitting!")
    sys.exit()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = FigureCanvas(Figure(figsize=(8, 5.5)))
        
        self.toolbar=qtbk.NavigationToolbar2QT(self.view,self)
        MainWindow.addToolBar(self.toolbar)
        self.axes = self.view.figure.subplots()
        self.axes.set_aspect('equal')
        self.axes.set_box_aspect(1)
        self.axes.set_xlim([-1E4,1E4])
        self.axes.set_ylim([-1E4,1E4])
        i=0
        self.a=[]
        self.print_source=[]
        self.SPEED_OF_LIGHT = 2.99792458e8
        self.filepath=""
        self.sourceList=list()
        self.finalList=list()
        
        self.localList=list()
        
        
    def setupUi(self, MainWindow):
        self.file_path=""
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1151, 679)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        self.gridLayout_3.addWidget(self.view, 0, 0, 3, 1, alignment=QtCore.Qt.AlignLeft)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
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
        # self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        # self.graphicsView_2.setSizePolicy(sizePolicy)
        # self.graphicsView_2.setObjectName("graphicsView_2")
        # self.gridLayout_3.addWidget(self.graphicsView_2, 0, 0, 1, 1)
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
        
        
    def plotfile(self, pos_dict,delay_dict):
        norm = Normalize(vmin=np.min(delay_dict['amplitude']), vmax=np.max(delay_dict['amplitude']))
        
        self.i=0
        l=len(pos_dict)
        
        for i in range(0,l):   #scatter plot for antennas
            self.axes.scatter(pos_dict[i][0], pos_dict[i][1], color='g', marker='^')
            
        l = len(delay_dict)
        for i in range(0,l):
            baseline=delay_dict['baseline'][i]
            ant2=(baseline - 65536) % 2048
            ant1 = ((baseline - 65536) - (ant2 ))//2048 
            xyp=self.hyperbola(delay_dict['delay'][i],
                               pos_dict[ant1][0],
                               pos_dict[ant1][1],
                               pos_dict[ant2][0],
                               pos_dict[ant2][1],
                               15000,1000) #self,delay_s, x0,x1,y0,y1, range, pts
            strength = delay_dict['amplitude'][i]
            self.axes.plot(xyp[0, :],xyp[1, :], alpha=0,picker=5, label=i,pickradius=5)
            lwidths=1+(xyp[2,:])
            points = np.array([xyp[0,:],xyp[1,:]]).T.reshape(-1, 1, 2)
            segments = np.concatenate([points[:-1], points[1:]], axis=1)

            #code to calculate the segment weights 
            segment_weights = np.convolve(xyp[2,:], np.ones(2)/2, 'valid')
            alpha_norm = LogNorm(vmin=np.min(1/segment_weights), vmax=np.max(1/segment_weights))
            
            colors = viridis_r(norm(strength*np.ones(len(segments))))
            colors[:,3] = alpha_norm(1/segment_weights)

            lc = LineCollection(segments, linewidths=lwidths,color=colors,norm=plt.Normalize(0, 10))

            self.axes.add_collection(lc)
            # self.axes.scatter(xyp[0, :],xyp[1, :], s=(xyp[2,:])**0.5, c=viridis_r(norm(strength)), linestyle='solid',picker=5, label=i,pickradius=5)
        self.view.figure.canvas.draw()     
         
        def on_press(event):
            event.artist.set_color("blue") #for greying out the selected lines
            event.artist.set_picker(True) #cannot be selected again
            self.view.figure.canvas.draw()

               
        
        def on_pick(event):
            
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            self.a.append(event.artist.get_label())
            # print (event.artist.get_label(),"clicked")
            # event.artist.set_visible(not event.artist.get_visible())    (for making selected lines invisible)
            event.artist.set_color("lightgrey") #for greying out the selected lines
            event.artist.set_alpha(0.5)
            event.artist.set_picker(False) #cannot be selected again
            self.view.figure.canvas.draw()
        
       
            
                

        self.view.figure.canvas.mpl_connect('pick_event', on_pick)  
        self.view.figure.canvas.mpl_connect('key_press_event', on_press)      
        
        
        # def add_evt(event):
        #     self.a.append(event.artist.get_label())
    # print(a)
        def groupbylist(event): 
            if (self.view.figure.canvas.cursor().shape())==0:
                
                self.print_source=[]
                
                self.i=self.i+1
                
                print ("source",self.i,"->",self.a)
                self.sourceList.extend(["source",self.i,"->",self.print_source,"position:",round(event.xdata,2), round(event.ydata,2)])
                
                self.localList.append(self.sourceList)
                self.finalList=self.localList
                self.sourceList=[]
                self.print_source+=(self.a)
                # print(self.localList)
                
                print("position:",round(event.xdata,2),",", round(event.ydata,2))
                self.lineEdit_2.insert(str(round(event.xdata,2)))
                self.lineEdit_4.insert(str(round(event.ydata,2)))
                
                self.a.clear()
        # self.view.figure.canvas.mpl_connect('pick_event',add_evt)
        self.view.figure.canvas.mpl_connect('button_release_event',groupbylist)
    

    
    def save_pos(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setWindowTitle("Save File")
        dialog.setViewMode(QtWidgets.QFileDialog.Detail)
        dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        dialog.setOption(QtWidgets.QFileDialog.DontConfirmOverwrite, True)
        dialog.setNameFilters(
                ["Text files (*.txt)", "Excel sheets (*.xlsx)"])
        dialog.setDefaultSuffix(".txt")
        dialog.exec_()
        
        if dialog.selectedFiles():
                
                fileType = (dialog.selectedFiles()[0]).split(".")[-1]
                
                if fileType == "txt":
                    try:
                        file = open(dialog.selectedFiles()[0], 'r')
                        writeData = file.read()
                        file.close()
                    except FileNotFoundError:
                        
                        writeData = self.finalList
                file = open(dialog.selectedFiles()[0], 'w')
                file.write(json.dumps(writeData))
                file.close()
        self.print_source.clear()
        
        
        
        
    def load_file(self):
        options = QtWidgets.QFileDialog.Options()
        
        options = options | QtWidgets.QFileDialog.DontUseNativeDialog
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Choose File", "",
            "npz files (*.npz)",
            options=options)
        if self.file_path[0]:
            self.lineEdit.clear()
            self.lineEdit.insert(self.file_path[0])

            # MODIFIED
            fileType = (self.file_path[0]).split(".")[-1]
            if fileType == "npz":
                data = np.load(self.file_path[0])
                print(data.files)
                # print(data['delays'][0:10])
                # print(data['positions'][0])
                
                # print(data_dict["positions"])
                # print(data_dict["delay"])
                # self.plotfile()
                self.plotfile(data["positions"],data["delays"])
            # print(data_dict["delays"]["baselines"][0])
            
            
    def hyperbola(self,delay_s, x0,x1,y0,y1, range, pts):
        """
        Plots a hyperbola with positions p0 = (x0, y0) and p1 = (x1, y1) as the foci.
        The delay is defined in seconds of light travel time such that positive --> closer to p0.
        """
        # x0, y0 = p0  # position in meteres
        # x1, y1 = p1  # position in meters
        speed_of_l=2.99792458e8
        angle = np.pi - np.arctan2((y1 - y0), (x1 - x0))

        c = np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2) / 2
        a = delay_s *speed_of_l/ 2  # convert from seconds to meters

        xy = cartesian_hyperbola(c, a, range, pts)

        # shift the focus from (c, 0) to origin.
        xy[0, :] -= c

        # rotate to p1 -> p0 angle.
        rot = np.array([[np.cos(angle), np.sin(angle)], [-np.sin(angle), np.cos(angle)]])

        xyp = np.zeros_like(xy)

        xyp[0:2,:] = np.matmul(rot, xy[0:2,:])

        xyp[2,:] = xy[2,:] # copy weights

        # shift origin to p0
        xyp[0, :] += x0
        xyp[1, :] += y0

        return xyp
        # print(xyp)
        


def cartesian_hyperbola(c, a, range, pts):
    """
    Returns a hyperbola around the focus at (c,0). The other focus is at (-c,0)
    """
    y = np.linspace(-range, range, pts, endpoint=True)
    b = np.sqrt(abs(c ** 2 - a ** 2))
    x = a * np.sqrt(1 + y ** 2 / b ** 2)
    d1 = np.sqrt(y**2+(x-c)**2) # distance from one focus
    d2 = np.sqrt(y**2+(x+c)**2) # distance from other focus
    scaling_factor = 25E6 # assume a typical distance scale of 5000m
    w = (d1*d2)/scaling_factor
    # w=scaling_factor/(d1*d2)
    return np.vstack([x, y, w])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


