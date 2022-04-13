import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from ui.main_window import Ui_MainWindow


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## setup matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        toolbar = NavigationToolbar(self.canvas, self)

        self.ui.verticalLayout_plot.addWidget(self.canvas)
        self.ui.verticalLayout_plot.addWidget(toolbar)

        ## connect ui and function
        self.ui.pushButton_apply.clicked.connect(self.plot)

        ## show this widget
        self.show()
    
    def plot(self, data):
        self.canvas.axes.cla()
        self.canvas.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec_()