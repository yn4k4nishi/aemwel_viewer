# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_plot = QtWidgets.QVBoxLayout()
        self.verticalLayout_plot.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_plot.setObjectName("verticalLayout_plot")
        self.horizontalLayout.addLayout(self.verticalLayout_plot)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_x = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_x.sizePolicy().hasHeightForWidth())
        self.comboBox_x.setSizePolicy(sizePolicy)
        self.comboBox_x.setObjectName("comboBox_x")
        self.verticalLayout_3.addWidget(self.comboBox_x)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget_axes = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_axes.setObjectName("listWidget_axes")
        self.verticalLayout_4.addWidget(self.listWidget_axes)
        self.comboBox_add = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_add.setObjectName("comboBox_add")
        self.verticalLayout_4.addWidget(self.comboBox_add)
        self.pushButton_addAxis = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_addAxis.setObjectName("pushButton_addAxis")
        self.verticalLayout_4.addWidget(self.pushButton_addAxis)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox_plane = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_plane.setObjectName("comboBox_plane")
        self.comboBox_plane.addItem("")
        self.comboBox_plane.addItem("")
        self.comboBox_plane.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_plane)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_cutting = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_cutting.setObjectName("comboBox_cutting")
        self.horizontalLayout_3.addWidget(self.comboBox_cutting)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox_freq = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_freq.setObjectName("comboBox_freq")
        self.verticalLayout_7.addWidget(self.comboBox_freq)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.pushButton_apply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.verticalLayout.addWidget(self.pushButton_apply)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCar2D = QtWidgets.QAction(MainWindow)
        self.actionCar2D.setObjectName("actionCar2D")
        self.actionPolar = QtWidgets.QAction(MainWindow)
        self.actionPolar.setObjectName("actionPolar")
        self.actionHeatmap = QtWidgets.QAction(MainWindow)
        self.actionHeatmap.setObjectName("actionHeatmap")
        self.menuFile.addAction(self.actionOpen)
        self.menuFormat.addAction(self.actionCar2D)
        self.menuFormat.addAction(self.actionPolar)
        self.menuFormat.addAction(self.actionHeatmap)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AEMWEL Viewer"))
        self.groupBox.setTitle(_translate("MainWindow", "X Axis"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Y Aixs"))
        self.pushButton_addAxis.setText(_translate("MainWindow", "Add Plot Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2D"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Plane"))
        self.label.setText(_translate("MainWindow", "cutting plane"))
        self.comboBox_plane.setItemText(0, _translate("MainWindow", "xy"))
        self.comboBox_plane.setItemText(1, _translate("MainWindow", "yz"))
        self.comboBox_plane.setItemText(2, _translate("MainWindow", "zx"))
        self.label_2.setText(_translate("MainWindow", "coordinate"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Freq"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "3D"))
        self.pushButton_apply.setText(_translate("MainWindow", "Apply"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCar2D.setText(_translate("MainWindow", "Cartesian 2D"))
        self.actionPolar.setText(_translate("MainWindow", "Polar"))
        self.actionHeatmap.setText(_translate("MainWindow", "Heatmap"))
