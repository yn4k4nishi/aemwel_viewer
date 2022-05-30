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

        # print(i, self.y_props[i].label)

        # set
        self.ui.checkBox_YEnable.setChecked(self.y_props[i].is_enabled)
        self.ui.lineEdit_YLable.setText(self.y_props[i].label)
        self.ui.lineEdit_LineWidth.setText(str(self.y_props[i].lw))
        self.ui.lineEdit_Color.setText(self.y_props[i].color)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('docs/img/icon32x32.png'))
    main_win = MainWindow()
    app.exec_()
