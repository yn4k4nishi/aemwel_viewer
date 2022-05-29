import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.setting_window import Ui_MainWindow

class SettingWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    setting_win = SettingWindow()
    app.exec_()
