import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


def animate(fig, axes, data_mag, data_phase, pickup_axis, pickup_value, freq, **kwargs):
    """プロットのアニメーション
    
    Parameters
    ----------
    fig          : :obj:`matplotlib.Figure`
        プロットする図
    axes         : :obj:`matplotlib.Axes`
        プロットする軸
    data         : dict
        ファイルから読み込んだデータ
    pickup_axis  : str
        断面をとる軸
    pickup_value : float
        断面をとる軸の値
    freq         : str
        使用する周波数を示すデータ系列名
    offset       : float
        位相勾配を見るときの位相のオフセット

    Returns
    -------
    :obj:`matplotlib.collections.QuadMesh`
    """

    ## pickup axis
    ax1 = 'xyz'.replace(pickup_axis, '')[0]
    ax2 = 'xyz'.replace(pickup_axis, '')[1]

    _x    = np.take(np.array(data_mag[ax1] ),   np.where(data_mag[pickup_axis]   == pickup_value)[0])
    _y    = np.take(np.array(data_mag[ax2] ),   np.where(data_mag[pickup_axis]   == pickup_value)[0])
    _z_mg = np.take(np.array(data_mag[freq]),   np.where(data_mag[pickup_axis]   == pickup_value)[0])
    _z_ph = np.take(np.array(data_phase[freq]), np.where(data_phase[pickup_axis] == pickup_value)[0])
    
    ## remove duplicate elements
    x = np.unique(_x)
    y = np.unique(_y)

    x = np.sort(x)
    y = np.sort(y)

    ## Z value
    z_mg = np.empty([x.shape[0], y.shape[0]])
    z_ph = np.empty([x.shape[0], y.shape[0]])

    for i, _ in np.ndenumerate(z_mg):
        i_x, i_y = i
        
        t_x = np.where(_x == x[i_x])[0]
        t_y = np.where(_y == y[i_y])[0]

        t = np.intersect1d(t_x, t_y)[0]

        z_mg[i] = _z_mg[t]
        z_ph[i] = _z_ph[t] / 180 * np.pi
    
    z = z_mg * np.sin(z_ph)

    im = axes.imshow(z)


    pass


if __name__ == "__main__":
    from __init__ import load_data

    file_mag   = "/home/yn4k4nishi/Downloads/20220509/1v/Trc5.csv"
    file_phase = "/home/yn4k4nishi/Downloads/20220509/1v/Trc7.csv"
    
    data_mag   = load_data(file_mag)
    data_phase = load_data(file_phase)

    freq = "1.68GHz"

    fig, ax = plt.subplots()

    animate(fig, ax, data_mag, data_phase, 'z', 0, freq)

    plt.show()

