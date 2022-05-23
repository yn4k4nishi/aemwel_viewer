"""Main Module

"""

import sys
import matplotlib
try:
    matplotlib.use('Qt5Agg')
except:
    pass

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

        matplotlib.rcParams["font.size"] = 18


class MainWindow(QMainWindow):
    """Qt メインウィンドウ"""

    form = PlotForm.cartesian2D
    """:obj: `plot.PlotFrom` プロットの形式"""

    data = {}
    """dict プロットに使うデータ"""

    data2 = {}
    """dict アニメーション等に使うデータ"""


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

        self.ui.checkBox_max.clicked.connect(lambda : self.ui.lineEdit_phase_max.setDisabled(not self.ui.checkBox_max.isChecked()))
        self.ui.checkBox_min.clicked.connect(lambda : self.ui.lineEdit_phase_min.setDisabled(not self.ui.checkBox_min.isChecked()))

        self.ui.checkBox_ani.clicked.connect(lambda : self.ui.pushButton_openPhaseData.setEnabled(self.ui.checkBox_ani.isChecked()))
        self.ui.checkBox_ani.clicked.connect(lambda : self.ui.lineEdit_interval.setEnabled(self.ui.checkBox_ani.isChecked()))
        self.ui.checkBox_ani.clicked.connect(lambda : self.ui.lineEdit_ani_interval.setEnabled(self.ui.checkBox_ani.isChecked()))

        self.ui.pushButton_openPhaseData.clicked.connect(self.loadPhaseData)
        self.ui.pushButton_saveGIF.clicked.connect(self.saveGIF)

        self.ui.pushButton_openPortData.clicked.connect(self.loadPortData)

        self.ui.actionOpen_in_Browser.triggered.connect(self.help)

        self.ui.checkBox_anchor.clicked.connect(lambda : self.ui.lineEdit_anchor_x.setDisabled(not self.ui.checkBox_anchor.isChecked()))
        self.ui.checkBox_anchor.clicked.connect(lambda : self.ui.lineEdit_anchor_y.setDisabled(not self.ui.checkBox_anchor.isChecked()))

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

        self.data = plot.load_data(file_name)

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


    def loadPhaseData(self):
        """位相データの読み込み
        
        アニメーション用の位相データの読み込み
        """
        filter = "All Files(*);;csv(*.csv);;Touch Stone(*.s*p)" 
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home', filter=filter)[0]

        if not file_name:
            return

        self.ui.label_phase_data_path.setText(file_name)

        self.data2 = plot.load_data(file_name)
    
    def loadPortData(self):
        """ポートのデータの読み込み

        分散曲線のため、ポート成分のみのデータを読み込む
        """
        filter = "Touch Stone(*.s*p)" 
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home', filter=filter)[0]

        if not file_name:
            return
        
        self.ui.label_portData.setText(file_name)

        self.data2 = plot.load_data(file_name)


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
            if self.ui.tabWidget.currentIndex() == 0:
                arg = {}
                if self.ui.checkBox_lim.isChecked():
                    arg['ymax'] = float(self.ui.lineEdit_ymax_2.text())
                    arg['ymin'] = float(self.ui.lineEdit_ymin_2.text())

                cartesian2D.plot(self.canvas.axes, self.data, x_axis, y_axes, **arg)

            if self.ui.tabWidget.currentIndex() == 2:
                ncell = int(self.ui.lineEdit_ncell.text())
                lcell = float(self.ui.lineEdit_cell_len.text())
                m1    = int(self.ui.lineEdit_m1.text())
                m2    = int(self.ui.lineEdit_m2.text())

                arg = {}
                if self.ui.checkBox_xlim.isChecked():
                    arg['xmax'] = float(self.ui.lineEdit_xmax.text())
                    arg['xmin'] = float(self.ui.lineEdit_xmin.text())
                if self.ui.checkBox_ylim.isChecked():
                    arg['ymax'] = float(self.ui.lineEdit_ymax.text())
                    arg['ymin'] = float(self.ui.lineEdit_ymin.text())

                dispersion.plot(self.canvas.axes, self.data, self.data2, ncell, lcell, m1, m2, **arg)

            # self.canvas.fig.legend()

        if self.form == PlotForm.polar:
            self.canvas.axes = self.canvas.fig.add_subplot(111, projection='polar')

            arg = {}
            if self.ui.checkBox_lim.isChecked():
                arg['ymax'] = float(self.ui.lineEdit_ymax_2.text())
                arg['ymin'] = float(self.ui.lineEdit_ymin_2.text())

            polar.plot(self.canvas.axes, self.data, x_axis, y_axes, **arg)
            self.canvas.fig.legend(bbox_to_anchor=(1, 0), loc='lower right')

        if self.form == PlotForm.heatmap:
            self.canvas.axes = self.canvas.fig.add_subplot(111)

            plane        = self.ui.comboBox_plane.currentText()
            pickup_axis  = 'xyz'.replace(plane[0], '').replace(plane[1], '')
            pickup_value = float(self.ui.comboBox_cutting.currentText())
            freq         = self.ui.comboBox_freq.currentText()

            nstep    = int(self.ui.lineEdit_ani_interval.text())
            interval = int(self.ui.lineEdit_interval.text())

            arg = dict()
            arg['offset'] = float(self.ui.lineEdit_phase_offset.text())
            
            if self.ui.checkBox_max.isChecked():
                arg['vmax'] = float(self.ui.lineEdit_phase_max.text())

            if self.ui.checkBox_min.isChecked():
                arg['vmin'] = float(self.ui.lineEdit_phase_min.text())
            
            if self.ui.checkBox_anchor.isChecked():
                arg['anchor_x'] = float(self.ui.lineEdit_anchor_x.text())
                arg['anchor_y'] = float(self.ui.lineEdit_anchor_y.text())

            if self.ui.checkBox_nomalize_phase.isChecked():
                arg['nomalize_phase'] = True

            if not self.ui.checkBox_ani.isChecked():
                c = heatmap.plot(self.canvas.fig, self.canvas.axes, self.data, pickup_axis, pickup_value, freq, **arg)
            
            else:
                if len(self.data.keys()) == len(self.data2.keys()):
                    self.ani = animation.animate(self.canvas.fig, self.canvas.axes, self.data, self.data2, pickup_axis, pickup_value, freq, nstep, interval, **arg)

        self.canvas.draw()

    def saveGIF(self):
        """アニメーションをGIF形式で保存"""
        gif_file = QFileDialog.getSaveFileName(self, 'Save as GIF', '/home/animation.gif')[0]
        
        if not gif_file:
            return

        self.ani.save(gif_file, writer="imagemagick")

    def help(self):
        """ブラウザでドキュメントを表示"""
        url = QUrl("https://yn4k4nishi.github.io/aemwel_viewer/")
        QDesktopServices.openUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('docs/img/icon32x32.png'))
    w = MainWindow()
    app.exec_()