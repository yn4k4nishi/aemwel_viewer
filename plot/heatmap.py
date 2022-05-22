import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.axes_grid1 import axes_divider
            

def plot(fig, axes, data, pickup_axis, pickup_value, freq, **kwargs):
    """ヒートマップのプロット
    
    Parameters
    ----------
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
    ax1 = 'xyz'.replace(pickup_axis, '')[0]
    ax2 = 'xyz'.replace(pickup_axis, '')[1]

    _x = np.take(np.array(data[ax1] ), np.where(data[pickup_axis] == pickup_value)[0])
    _y = np.take(np.array(data[ax2] ), np.where(data[pickup_axis] == pickup_value)[0])
    _z = np.take(np.array(data[freq]), np.where(data[pickup_axis] == pickup_value)[0])

    ## remove duplicate elements
    x = np.unique(_x)
    y = np.unique(_y)

    x = np.sort(x)
    y = np.sort(y)

    ## z values
    z = np.empty([x.shape[0], y.shape[0]])

    for i, _ in np.ndenumerate(z):
        i_x, i_y = i
        
        t_x = np.where(_x == x[i_x])[0]
        t_y = np.where(_y == y[i_y])[0]

        t = np.intersect1d(t_x, t_y)[0]

        z[i] = _z[t]

    if 'offset' in kwargs:
        z += kwargs['offset']
        z = (z + 180) % 360 - 180 

    k = {}
    if 'vmax' in kwargs:
        k['vmax'] = kwargs['vmax']
    if 'vmin' in kwargs:
        k['vmin'] = kwargs['vmin']


    im = axes.imshow(z, cmap='jet', **k)

    ## color bar
    divider = axes_divider.make_axes_locatable(axes)
    cax = divider.append_axes("right", size="3%", pad="2%")
    fig.colorbar(im, cax=cax)

    axes.set_aspect('equal')

    return im

if __name__ == "__main__":
    pass

    # file = 'data/xyz_phase.csv'
    # data = load_data(file)

    # fig = plt.figure()
    # axes = fig.add_subplot(111)

    # target_z = 0.0
    # target_freq = '1680000000.0'

    # axes.set_aspect('equal')

    # heatmap = plot(axes, data, target_z, target_freq)
    # fig.colorbar(heatmap)

    # plt.show()
