"""Main Module

"""
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1 import axes_divider

from ui.main_window import Ui_MainWindow

import plot
from plot import *


class MplCanvas(FigureCanvasQTAgg):
    """PyQt5にMatplotlibを埋め込むためのクラス

    Attributes
    ----------
    fig : :obj: `matplotlib.Figure`
        matplotlib.figure object
    axes : :obj: `matplotlib.Axes`
    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """初期化
        
        Parameters
        ----------
        parent : :obj:Qt Parent
        width  : int 図の幅
        height : int 図の高さ
        dpi    : int dots per inch
        """
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

        self.axes.set_aspect('equal')
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))


class MainWindow(QMainWindow):
    """Qt メインウィンドウ"""

    form = PlotForm.cartesian2D
    """:obj: `plot.PlotFrom` プロットの形式"""

    data = {}
    """dict プロットに使うデータ"""


    def __init__(self, parent=None):
        """初期化
        
        Parameters
        ----------
        parent : :obj: Qt parent

        Attributes
        ----------
        ui      : :obj:`Ui_MainWindow`
        canvas  : :obj:`MplCanvas`
        toolbar : :obj:`FigureCanvasQTAgg`, `NavigationToolbar2QT`
        """
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## setup matplotlib
        self.canvas = MplCanvas(self)

        toolbar = NavigationToolbar(self.canvas, self)

        self.ui.verticalLayout_plot.addWidget(self.canvas)
        self.ui.verticalLayout_plot.addWidget(toolbar)

        ## setup menubar
        self.ui.actionCar2D.setCheckable(True)
        self.ui.actionPolar.setCheckable(True)
        self.ui.actionHeatmap.setCheckable(True)

        self.ui.form_group = QActionGroup(self)
        self.ui.form_group.addAction(self.ui.actionCar2D)
        self.ui.form_group.addAction(self.ui.actionPolar)
        self.ui.form_group.addAction(self.ui.actionHeatmap)
        
        self.ui.actionCar2D.setChecked(True)


        ## connect ui and function
        self.ui.pushButton_apply.clicked.connect(self.update)
        self.ui.pushButton_clear.clicked.connect(self.ui.listWidget_axes.clear)
        self.ui.actionOpen.triggered.connect(self.loadData)

        self.ui.actionCar2D.triggered.connect(lambda : self.setForm(PlotForm.cartesian2D))
        self.ui.actionPolar.triggered.connect(lambda : self.setForm(PlotForm.polar))
        self.ui.actionHeatmap.triggered.connect(lambda : self.setForm(PlotForm.heatmap))


        self.ui.actionCar2D.triggered.connect(lambda : self.ui.tabWidget.setCurrentIndex(0))
        self.ui.actionPolar.triggered.connect(lambda : self.ui.tabWidget.setCurrentIndex(0))
        self.ui.actionHeatmap.triggered.connect(lambda : self.ui.tabWidget.setCurrentIndex(1))

        self.ui.pushButton_addAxis.clicked.connect(self.addAxis)
        self.ui.comboBox_plane.activated.connect(self.set3dProperty)

        ## show this widget
        self.show()
    
    def setForm(self, form):
        """プロット形式の設定
        
        Parameters
        ----------
        form : :obj:`plot.PlotForm`
            プロットの形式
        """
        print("setForm : {}".format(form))
        self.form = form

    def loadData(self):
        """データの読み込み
        
        ファイルダイアログを開き読み込むファイルを指定する
        読み込んだファイルを元にComboBoxを設定する
        """

        filter = "All Files(*);;csv(*.csv);;Touch Stone(*.s*p)" 
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home', filter=filter)[0]

        if not file_name:
            return
        
        self.ui.label_path.setText(file_name)
        
        self.thread = LoadThread(self)
        self.thread.setFilename(file_name)
        self.thread.progress.connect(self.ui.progressBar.setValue)

        self.thread.start()

        while self.thread.isRunning():
            pass

        self.data = self.thread.getData()

        # self.data = plot.load_data(file_name)

        if self.form == PlotForm.heatmap:
            self.set3dProperty()

        self.ui.comboBox_x.clear()
        self.ui.comboBox_add.clear()
        self.ui.comboBox_freq.clear()

        for k in self.data.keys():
            self.ui.comboBox_x.addItem(k)

            if k in ['angle[rad]', 'x', 'y', 'z']:
                continue

            self.ui.comboBox_add.addItem(k)
            self.ui.comboBox_freq.addItem(k)


    def addAxis(self):
        """プロットする軸(データ系列)の追加"""
        self.ui.listWidget_axes.addItem(self.ui.comboBox_add.currentText())

    def set3dProperty(self):
        """3Dのプロパティの設定"""
        plane = self.ui.comboBox_plane.currentText()
        pickup_axis = 'xyz'.replace(plane[0], '').replace(plane[1], '')

        self.ui.comboBox_cutting.clear()
        for p in np.unique(self.data[pickup_axis]):
            self.ui.comboBox_cutting.addItem(str(p))

    def update(self):
        """プロットの更新"""

        x_axis = self.ui.comboBox_x.currentText()
        y_axes = [self.ui.listWidget_axes.item(i).text() for i in range(self.ui.listWidget_axes.count())]


        # self.canvas.axes.cla()
        self.canvas.fig.clf()
        
        if self.form == PlotForm.cartesian2D:
            self.canvas.axes = self.canvas.fig.add_subplot(111)
            cartesian2D.plot(self.canvas.axes, self.data, x_axis, y_axes)
            self.canvas.fig.legend()

        if self.form == PlotForm.polar:
            self.canvas.axes = self.canvas.fig.add_subplot(111, projection='polar')
            polar.plot(self.canvas.axes, self.data, x_axis, y_axes)
            self.canvas.fig.legend()

        if self.form == PlotForm.heatmap:
            self.canvas.axes = self.canvas.fig.add_subplot(111)

            plane = self.ui.comboBox_plane.currentText()
            pickup_axis = 'xyz'.replace(plane[0], '').replace(plane[1], '')
            pickup_value = float(self.ui.comboBox_cutting.currentText())
            freq = self.ui.comboBox_freq.currentText()

            arg = dict()
            arg['offset'] = float(self.ui.lineEdit_phase_offset.text())
            arg['vmax']   = float(self.ui.lineEdit_phase_max.text())
            arg['vmin']   = float(self.ui.lineEdit_phase_min.text())

            c = heatmap.plot(self.canvas.axes, self.data, pickup_axis, pickup_value, freq, **arg)
            
            ## color bar
            divider = axes_divider.make_axes_locatable(self.canvas.axes)
            cax = divider.append_axes("right", size="3%", pad="2%")
            self.canvas.fig.colorbar(c, cax=cax)

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec_()