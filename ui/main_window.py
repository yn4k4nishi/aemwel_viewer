# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 759)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_plot = QtWidgets.QVBoxLayout()
        self.verticalLayout_plot.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_plot.setObjectName("verticalLayout_plot")
        self.horizontalLayout_4.addLayout(self.verticalLayout_plot)
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
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout_4.addWidget(self.pushButton_clear)
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
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.lineEdit_phase_max = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_phase_max.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phase_max.sizePolicy().hasHeightForWidth())
        self.lineEdit_phase_max.setSizePolicy(sizePolicy)
        self.lineEdit_phase_max.setFrame(True)
        self.lineEdit_phase_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_phase_max.setObjectName("lineEdit_phase_max")
        self.gridLayout.addWidget(self.lineEdit_phase_max, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)
        self.lineEdit_phase_min = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_phase_min.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phase_min.sizePolicy().hasHeightForWidth())
        self.lineEdit_phase_min.setSizePolicy(sizePolicy)
        self.lineEdit_phase_min.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_phase_min.setObjectName("lineEdit_phase_min")
        self.gridLayout.addWidget(self.lineEdit_phase_min, 3, 2, 1, 1)
        self.lineEdit_phase_offset = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phase_offset.sizePolicy().hasHeightForWidth())
        self.lineEdit_phase_offset.setSizePolicy(sizePolicy)
        self.lineEdit_phase_offset.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_phase_offset.setObjectName("lineEdit_phase_offset")
        self.gridLayout.addWidget(self.lineEdit_phase_offset, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.checkBox_max = QtWidgets.QCheckBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_max.sizePolicy().hasHeightForWidth())
        self.checkBox_max.setSizePolicy(sizePolicy)
        self.checkBox_max.setAutoFillBackground(False)
        self.checkBox_max.setText("")
        self.checkBox_max.setChecked(False)
        self.checkBox_max.setObjectName("checkBox_max")
        self.gridLayout.addWidget(self.checkBox_max, 2, 0, 1, 1)
        self.checkBox_min = QtWidgets.QCheckBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_min.sizePolicy().hasHeightForWidth())
        self.checkBox_min.setSizePolicy(sizePolicy)
        self.checkBox_min.setText("")
        self.checkBox_min.setChecked(False)
        self.checkBox_min.setObjectName("checkBox_min")
        self.gridLayout.addWidget(self.checkBox_min, 3, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.checkBox_ani = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_ani.setObjectName("checkBox_ani")
        self.verticalLayout_9.addWidget(self.checkBox_ani)
        self.label_phase_data_path = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phase_data_path.sizePolicy().hasHeightForWidth())
        self.label_phase_data_path.setSizePolicy(sizePolicy)
        self.label_phase_data_path.setText("")
        self.label_phase_data_path.setObjectName("label_phase_data_path")
        self.verticalLayout_9.addWidget(self.label_phase_data_path)
        self.pushButton_openPhaseData = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_openPhaseData.setEnabled(False)
        self.pushButton_openPhaseData.setObjectName("pushButton_openPhaseData")
        self.verticalLayout_9.addWidget(self.pushButton_openPhaseData)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_ani_interval = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_ani_interval.setEnabled(False)
        self.lineEdit_ani_interval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_ani_interval.setObjectName("lineEdit_ani_interval")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ani_interval)
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_interval = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_interval.setEnabled(False)
        self.lineEdit_interval.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_interval.setObjectName("lineEdit_interval")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_interval)
        self.verticalLayout_9.addLayout(self.formLayout_2)
        self.pushButton_saveGIF = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_saveGIF.setObjectName("pushButton_saveGIF")
        self.verticalLayout_9.addWidget(self.pushButton_saveGIF)
        self.verticalLayout_5.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.pushButton_apply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.verticalLayout.addWidget(self.pushButton_apply)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setText("")
        self.label_path.setObjectName("label_path")
        self.verticalLayout_10.addWidget(self.label_path)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_10.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 22))
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AEMWEL Viewer"))
        self.groupBox.setTitle(_translate("MainWindow", "X Axis"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Y Aixs"))
        self.pushButton_addAxis.setText(_translate("MainWindow", "Add"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2D"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Plane"))
        self.label.setText(_translate("MainWindow", "cutting plane"))
        self.comboBox_plane.setItemText(0, _translate("MainWindow", "xy"))
        self.comboBox_plane.setItemText(1, _translate("MainWindow", "yz"))
        self.comboBox_plane.setItemText(2, _translate("MainWindow", "zx"))
        self.label_2.setText(_translate("MainWindow", "coordinate"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Freq"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Param"))
        self.label_3.setText(_translate("MainWindow", "Offset"))
        self.lineEdit_phase_max.setText(_translate("MainWindow", "180"))
        self.label_7.setText(_translate("MainWindow", "Min"))
        self.lineEdit_phase_min.setText(_translate("MainWindow", "-180"))
        self.lineEdit_phase_offset.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "Max"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Animation"))
        self.checkBox_ani.setText(_translate("MainWindow", "enable"))
        self.pushButton_openPhaseData.setText(_translate("MainWindow", "Open Phase Data"))
        self.label_6.setText(_translate("MainWindow", "step num"))
        self.lineEdit_ani_interval.setText(_translate("MainWindow", "40"))
        self.label_5.setText(_translate("MainWindow", "interval [ms]"))
        self.lineEdit_interval.setText(_translate("MainWindow", "200"))
        self.pushButton_saveGIF.setText(_translate("MainWindow", "Save as GIF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "3D"))
        self.pushButton_apply.setText(_translate("MainWindow", "Apply"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionCar2D.setText(_translate("MainWindow", "Cartesian 2D"))
        self.actionPolar.setText(_translate("MainWindow", "Polar"))
        self.actionHeatmap.setText(_translate("MainWindow", "Heatmap"))
