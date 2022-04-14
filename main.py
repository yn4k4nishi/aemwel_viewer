import sys
import matplotlib
from matplotlib import projections

matplotlib.use('Qt5Agg')

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1 import axes_divider

from ui.main_window import Ui_MainWindow

from plot import *


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, projection=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111, projection=projection)
        super(MplCanvas, self).__init__(self.fig)

        self.axes.set_aspect('equal')
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))



class MainWindow(QMainWindow):

    form = PlotForm.cartesian2D
    data = {}

    def __init__(self, parent=None):
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
        self.ui.actionOpen.triggered.connect(self.loadData)

        self.ui.actionCar2D.triggered.connect(lambda : self.setForm(PlotForm.cartesian2D))
        self.ui.actionPolar.triggered.connect(lambda : self.setForm(PlotForm.polar))
        self.ui.actionHeatmap.triggered.connect(lambda : self.setForm(PlotForm.heatmap))

        ## show this widget
        self.show()
    
    def setForm(self, form):
        print("setForm : {}".format(form))
        self.form = form

    def loadData(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '/home')[0]

        if self.form == PlotForm.cartesian2D:
            self.data = cartesian2D.load_data(file_name)

        if self.form == PlotForm.polar:
            self.data = polar.load_data(file_name)

        if self.form == PlotForm.heatmap:
            self.data = heatmap.load_data(file_name)

    def update(self):

        self.canvas.axes.cla()
        
        if self.form == PlotForm.cartesian2D:
            cartesian2D.plot(self.canvas.axes)

        if self.form == PlotForm.polar:
            # self.canvas.__init__(self, projection='polar')
            polar.plot(self.canvas.axes, self.data, '6200000000.0')

        if self.form == PlotForm.heatmap:

            c = heatmap.plot(self.canvas.axes, self.data, 0, '1680000000.0')
            ## color bar
            divider = axes_divider.make_axes_locatable(self.canvas.axes)
            cax = divider.append_axes("right", size="3%", pad="2%")
            self.canvas.fig.colorbar(c, cax=cax)

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec_()