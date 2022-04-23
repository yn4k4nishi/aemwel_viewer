from plot import cartesian2D
from plot import heatmap
from plot import polar

from enum import Enum

import csv
import numpy as np
import skrf as rf

from PyQt5.QtCore import *
from PyQt5.QtGui import *



class PlotForm(Enum):
    """プロットの形式"""

    cartesian2D = 1
    """2次元の直交座標"""

    polar       = 2
    """2次元の極座標"""
    
    heatmap     = 3
    """ヒートマップ"""
        
def load_data(file_name, signal=None):
    """データの読み込み
    
    Parameters
    ----------
    file_name : str 
        データを読み込むファイル

    Returns
    -------
    dict
        Keyにデータ系列の名前を持ち, numpy.arrayとしてデータを持つ

    Examples
    --------
        >>> data = load_data(file)
        >>> print(data['x'])
        [     0.      1.      2. ... 98. 99. 100.]
    """

    n = 0

    ## CSV
    if file_name.endswith('.csv'):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)

            header = reader.__next__()
            while '!' in header[0]: ## skip comment
                header = reader.__next__()
        
            values = [np.array([])] * len(header)

            data = dict(zip(header, values))

            if signal is not None:
                n_max = len(header)



            for r in reader:
                for i in range(len(header)):
                    data[header[i]] = np.append(data[header[i]], float(r[i]))
                
                if signal is not None:
                    signal.emit(n/n_max * 100)
                    n += 1

            return data
    
    ## Touch Stone
    elif file_name.endswith('.s2p') or file_name.endswith('.s4p'):
        net = rf.Network(file_name)

        data = dict()

        data['freq_GHz'] = net.frequency.f / 1e9

        for i in range(net.s.shape[1]):
            for j in range(net.s.shape[2]):
                key = 'S{}{}_db'.format(i+1, j+1)
                data[key] = net.s_db[:, i, j]

                key = 'S{}{}_deg'.format(i+1, j+1)
                data[key] = net.s_deg[:, i, j]

        return data

class LoadThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

    def run(self):
        self.data = load_data(self.file, self.progress)

    def setFilename(self, file):
        self.file = file

    def getData(self):
        return self.data

