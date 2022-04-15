import csv
import numpy as np
import matplotlib.pyplot as plt
            

def plot(axes, data, target_z, target_freq):
    _x = np.take(np.array(data['x']        ), np.where(data['z'] == target_z)[0])
    _y = np.take(np.array(data['y']        ), np.where(data['z'] == target_z)[0])
    _z = np.take(np.array(data[target_freq]), np.where(data['z'] == target_z)[0])

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

    ## create mesh
    # x_step = x[1] - x[0]
    # y_step = y[1] - y[0]

    # x_grid = np.append(x, x[-1]+x_step)
    # y_grid = np.append(y, y[-1]+y_step)

    # x_grid -= x_step/2
    # y_grid -= y_step/2

    z_max = np.max(z)
    z_min = np.min(z)

    # heatmap = axes.pcolormesh( x_grid,y_grid,  z.T, cmap='jet', shading='flat', vmin=z_min, vmax=z_max, clip_on=True)
    heatmap = axes.pcolormesh( x, y,  z.T, cmap='jet', shading='nearest', vmin=z_min, vmax=z_max, clip_on=True)
    
    axes.set_aspect('equal')

    return heatmap

if __name__ == "__main__":
    file = 'data/xyz_phase.csv'
    data = load_data(file)

    fig = plt.figure()
    axes = fig.add_subplot(111)

    target_z = 0.0
    target_freq = '1680000000.0'

    axes.set_aspect('equal')

    heatmap = plot(axes, data, target_z, target_freq)
    fig.colorbar(heatmap)

    plt.show()
