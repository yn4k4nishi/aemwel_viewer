from matplotlib.pyplot import axis
import numpy as np


def plot(axes, data, x_axis, y_axes):
    """2次元直交座標のプロット
    
    Parameters
    ----------
    axes : :obj:`matplotlib.Axes`
        プロットする軸
    data : dict
        ファイルから読み込んだデータ
    x_axis : str
        x軸に使用するデータ系列名
    y_axes : list of str
        y軸に使用するデータ系列名のリスト
    """
    
    axes.set_xlabel(x_axis)

    xmin = min(data[x_axis])
    xmax = max(data[x_axis])

    axes.set_xlim([xmin, xmax])

    for y_axis in y_axes:
        axes.plot(data[x_axis], data[y_axis], label=y_axis, linewidth=3)