import numpy as np


def plot(axes, data, x_axis, y_axes):
    """極座標プロット
    
    Parameters
    ----------
    axes   : :obj:`matplotlib.Axes`
        プロットする軸
    data   : dict
        ファイルから読み込んだデータ
    x_axis : str
        x軸のデータ系列名
    y_axes : str
        y軸のデータ系列名
    """
    
    angle = data[x_axis] / 180 * np.pi
    
    for y_axis in y_axes:
        mag   = data[y_axis]

        axes.plot(angle, mag, label=y_axis)

    axes.axes.set_theta_zero_location('N')
    axes.set_theta_direction(-1)
    axes.set_rlabel_position(0)
    axes.set_xticks(np.pi/180. * np.linspace(0,  360, 12, endpoint=False))
    axes.spines['polar'].set_color('darkgray')
