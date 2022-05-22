import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.axes_grid1 import axes_divider


def animate(fig, axes, data_mag, data_phase, pickup_axis, pickup_value, freq, nstep, interval, **kwargs):
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
    :obj:`matplotlib.image.AxesImage`
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
    
    k = {}
    if 'vmax' in kwargs:
        k['vmax'] = kwargs['vmax']
    if 'vmin' in kwargs:
        k['vmin'] = kwargs['vmin']

    z = z_mg * np.sin(z_ph)
    im0 = axes.imshow(z, cmap='jet', **k)

    ## color bar
    divider = axes_divider.make_axes_locatable(axes)
    cax = divider.append_axes("right", size="3%", pad="2%")
    fig.colorbar(im0, cax=cax)

    ims = []
    for theta in np.linspace(-np.pi, np.pi, nstep, endpoint=False):
        z = z_mg * np.sin(z_ph + theta)
        im = axes.imshow(z, cmap='jet', animated=True, **k)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=interval, repeat_delay=0)

    axes.set_aspect('equal')

    return ani



if __name__ == "__main__":
    from __init__ import load_data

    file_mag   = "/home/yn4k4nishi/Downloads/20220509/1v/Trc5.csv"
    file_phase = "/home/yn4k4nishi/Downloads/20220509/1v/Trc7.csv"
    
    data_mag   = load_data(file_mag)
    data_phase = load_data(file_phase)

    freq = "1.68GHz"

    fig, ax = plt.subplots()

    ani = animate(fig, ax, data_mag, data_phase, 'z', 0, freq, nstep=20, interval=200)

    plt.show()

