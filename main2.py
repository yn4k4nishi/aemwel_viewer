import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.setting_window import Ui_MainWindow

from ui.y_axis import YAxisProperty

import plot
from plot import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # setup combo box
        for c in Color:
            self.ui.comboBox_Color.addItem(c)
        
        for s in LineStyle:
            self.ui.comboBox_LineStyle.addItem(s)

        ###  connect function  ###
        # tab 
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionOpne_in_Browser.triggered.connect(self.help)
        # x axis
        self.ui.comboBox_XAxis.currentIndexChanged.connect(lambda : self.ui.lineEdit_XLable.setText(self.ui.comboBox_XAxis.currentText()))
        # y axis
        self.ui.listWidget_YAxes.itemClicked.connect(lambda : self.ui.groupBox_4.setEnabled(True))
        self.ui.listWidget_YAxes.currentItemChanged.connect(self.selectYAxis)
        ## edit y axis param
        self.ui.checkBox_YEnable.clicked.connect(lambda : self.y_props[self.i_yaxis].setEnable(self.ui.checkBox_YEnable.isChecked()))
        self.ui.lineEdit_YLable.editingFinished.connect(lambda : self.y_props[self.i_yaxis].setLabel(self.ui.lineEdit_YLable.text()))
        self.ui.lineEdit_LineWidth.editingFinished.connect(lambda : self.y_props[self.i_yaxis].setLineWidth(float(self.ui.lineEdit_LineWidth.text())))
        self.ui.comboBox_Color.currentIndexChanged.connect(lambda : self.y_props[self.i_yaxis].setColor(self.ui.comboBox_Color.currentText()))
        self.ui.comboBox_LineStyle.currentIndexChanged.connect(lambda : self.y_props[self.i_yaxis].setStyle(self.ui.comboBox_LineStyle.currentText()))
        # apply
        self.ui.pushButton_Apply.clicked.connect(self.apply)
        ##########################

        self.show()

        self.openFile()

    def openFile(self):
        """ ファイルの読み込み """

        filter = "All Files(*);;csv(*.csv);;Touch Stone(*.s*p)" 
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home', filter=filter)[0]

        if not file_name:
            return

        self.ui.textBrowser_FilePath.setText(file_name)

        self.data = plot.load_data(file_name)

        # clear 
        self.ui.comboBox_XAxis.clear()
        self.ui.listWidget_YAxes.clear()
        self.y_props = []

        # set Title
        self.ui.lineEdit_Title.setText(file_name.split('/')[-1].split('.')[0])

        # set 2D property
        for k in self.data.keys():
            self.ui.comboBox_XAxis.addItem(k)   # X Axis
            self.ui.listWidget_YAxes.addItem(k) # Y Axis

            self.y_props.append(YAxisProperty(k))


    def help(self):
        """ブラウザでドキュメントを表示"""
        url = QUrl("https://yn4k4nishi.github.io/aemwel_viewer/")
        QDesktopServices.openUrl(url)

    def selectYAxis(self):
        self.i_yaxis = self.ui.listWidget_YAxes.currentIndex().row()

        i = self.i_yaxis

        # print(i, self.y_props[i].label, self.y_props[i].color, self.y_props[i].style)

        # set
        self.ui.checkBox_YEnable.setChecked(self.y_props[i].is_enabled)
        self.ui.lineEdit_YLable.setText(self.y_props[i].label)
        self.ui.lineEdit_LineWidth.setText(str(self.y_props[i].lw))
        
        i_color = self.ui.comboBox_Color.findText(self.y_props[i].color)
        self.ui.comboBox_Color.setCurrentIndex(i_color)

        i_style = self.ui.comboBox_LineStyle.findText(self.y_props[i].style)
        self.ui.comboBox_LineStyle.setCurrentIndex(i_style)


    def apply(self):
        # axis
        xaxis  = self.ui.comboBox_XAxis.currentText() 
        xlabel = self.ui.lineEdit_XLable.text()
        # figure
        title     = self.ui.lineEdit_Title.text()
        font_size = self.ui.lineEdit_FontSize.text()
        fig_size  = (float(self.ui.lineEdit_FigSizeX.text()), float(self.ui.lineEdit_FigSizeY.text()))
        legend    = self.ui.checkBox_Legend.isChecked()

        opt = {}
        if self.ui.checkBox_XLim.isChecked():
            opt['xmax'] = float(self.ui.lineEdit_XMax.text())
            opt['xmin'] = float(self.ui.lineEdit_XMin.text())

        if self.ui.checkBox_YLim.isChecked():
            opt['ymax'] = float(self.ui.lineEdit_YMax.text())
            opt['ymin'] = float(self.ui.lineEdit_YMin.text())
        
        if self.ui.checkBox_PolarChart.isChecked():
            opt['projection'] = 'polar'

        plot.plot2D.plot(self.data, xaxis, self.y_props, title, xlabel, font_size, fig_size, legend, **opt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('docs/img/icon32x32.png'))
    main_win = MainWindow()
    app.exec_()
