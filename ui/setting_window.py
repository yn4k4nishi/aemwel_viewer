# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/setting_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_XAxis = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_XAxis.setObjectName("comboBox_XAxis")
        self.verticalLayout_3.addWidget(self.comboBox_XAxis)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.lineEdit_XLable = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_XLable.setObjectName("lineEdit_XLable")
        self.horizontalLayout_2.addWidget(self.lineEdit_XLable)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget_YAxes = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_YAxes.sizePolicy().hasHeightForWidth())
        self.listWidget_YAxes.setSizePolicy(sizePolicy)
        self.listWidget_YAxes.setObjectName("listWidget_YAxes")
        self.verticalLayout_4.addWidget(self.listWidget_YAxes)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_YLable = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_YLable.setObjectName("lineEdit_YLable")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_YLable)
        self.lineEdit_LineWidth = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_LineWidth.setObjectName("lineEdit_LineWidth")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_LineWidth)
        self.comboBox_LineStyle = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_LineStyle.setObjectName("comboBox_LineStyle")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_LineStyle)
        self.checkBox_YEnable = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_YEnable.setChecked(False)
        self.checkBox_YEnable.setTristate(False)
        self.checkBox_YEnable.setObjectName("checkBox_YEnable")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_YEnable)
        self.comboBox_Color = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_Color.setObjectName("comboBox_Color")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBox_Color)
        self.verticalLayout_7.addLayout(self.formLayout)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_Title = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Title.setObjectName("lineEdit_Title")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Title)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_FontSize = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_FontSize.setObjectName("lineEdit_FontSize")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_FontSize)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setIndent(12)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_FigSizeX = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_FigSizeX.setObjectName("lineEdit_FigSizeX")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_FigSizeX)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setIndent(12)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_FigSizeY = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_FigSizeY.setObjectName("lineEdit_FigSizeY")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_FigSizeY)
        self.checkBox_XLim = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_XLim.setObjectName("checkBox_XLim")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_XLim)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setIndent(8)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_XMax = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_XMax.setObjectName("lineEdit_XMax")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_XMax)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setIndent(8)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_XMin = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_XMin.setObjectName("lineEdit_XMin")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_XMin)
        self.checkBox_YLim = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_YLim.setObjectName("checkBox_YLim")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.checkBox_YLim)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setIndent(8)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_YMax = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_YMax.setObjectName("lineEdit_YMax")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_YMax)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setIndent(8)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_YMin = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_YMin.setObjectName("lineEdit_YMin")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_YMin)
        self.checkBox_Legend = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_Legend.setChecked(True)
        self.checkBox_Legend.setObjectName("checkBox_Legend")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.checkBox_Legend)
        self.checkBox_PolarChart = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_PolarChart.setObjectName("checkBox_PolarChart")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.checkBox_PolarChart)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.textBrowser_FilePath = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_FilePath.setObjectName("textBrowser_FilePath")
        self.verticalLayout_6.addWidget(self.textBrowser_FilePath)
        self.comboBox_Plot = QtWidgets.QComboBox(self.tab)
        self.comboBox_Plot.setObjectName("comboBox_Plot")
        self.comboBox_Plot.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_Plot)
        self.pushButton_Apply = QtWidgets.QPushButton(self.tab)
        self.pushButton_Apply.setObjectName("pushButton_Apply")
        self.verticalLayout_6.addWidget(self.pushButton_Apply)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpne_in_Browser = QtWidgets.QAction(MainWindow)
        self.actionOpne_in_Browser.setObjectName("actionOpne_in_Browser")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionOpne_in_Browser)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AEMWEL Viewer"))
        self.groupBox.setTitle(_translate("MainWindow", "X Axis"))
        self.label_14.setText(_translate("MainWindow", "Label"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Y Axis"))
        self.label_2.setText(_translate("MainWindow", "Line width"))
        self.label_3.setText(_translate("MainWindow", "Color"))
        self.label.setText(_translate("MainWindow", "Label"))
        self.label_4.setText(_translate("MainWindow", "Line Style"))
        self.lineEdit_LineWidth.setText(_translate("MainWindow", "3"))
        self.checkBox_YEnable.setText(_translate("MainWindow", "enable"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Propoerty"))
        self.label_5.setText(_translate("MainWindow", "Title"))
        self.label_10.setText(_translate("MainWindow", "Font Size"))
        self.lineEdit_FontSize.setText(_translate("MainWindow", "18"))
        self.label_11.setText(_translate("MainWindow", "Figure Size"))
        self.label_12.setText(_translate("MainWindow", "x"))
        self.lineEdit_FigSizeX.setText(_translate("MainWindow", "12"))
        self.label_13.setText(_translate("MainWindow", "y"))
        self.lineEdit_FigSizeY.setText(_translate("MainWindow", "8"))
        self.checkBox_XLim.setText(_translate("MainWindow", "x lim"))
        self.label_6.setText(_translate("MainWindow", "max"))
        self.lineEdit_XMax.setText(_translate("MainWindow", "1"))
        self.label_7.setText(_translate("MainWindow", "min"))
        self.lineEdit_XMin.setText(_translate("MainWindow", "10"))
        self.checkBox_YLim.setText(_translate("MainWindow", "y lim"))
        self.label_8.setText(_translate("MainWindow", "max"))
        self.lineEdit_YMax.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "min"))
        self.lineEdit_YMin.setText(_translate("MainWindow", "-30"))
        self.checkBox_Legend.setText(_translate("MainWindow", "Legend"))
        self.checkBox_PolarChart.setText(_translate("MainWindow", "Polar Chart"))
        self.comboBox_Plot.setItemText(0, _translate("MainWindow", "<New>"))
        self.pushButton_Apply.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "3D"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpne_in_Browser.setText(_translate("MainWindow", "Open in Browser"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
