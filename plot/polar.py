import numpy as np


def plot(axes, data, x_axis, y_axes, **kwargs):
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
    ymin   : float (option)
        y軸の最小値
    ymax   : float (option)
        y軸の最大値
    """
    
    angle = data[x_axis] / 180 * np.pi
    
    for y_axis in y_axes:
        mag   = data[y_axis] 

        if 'max_line' in kwargs:
            _i = np.argmax(mag)
            axes.axvline(angle[_i], linestyle="--")
            axes.text(angle[_i], mag[_i] + 5, "{:.2f} deg".format(angle[_i]*180/np.pi))

        axes.plot(angle, mag, label=y_axis, lw=3)

    axes.axes.set_theta_zero_location('N')
    axes.set_theta_direction(-1)
    axes.set_rlabel_position(0)
    axes.set_xticks(np.pi/180. * np.linspace(0,  360, 12, endpoint=False))
    axes.spines['polar'].set_color('darkgray')

    if 'ymax' in kwargs:
        axes.set_ylim([kwargs['ymin'], kwargs['ymax']])
