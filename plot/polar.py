from cProfile import label
import csv
from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt


def plot(axes, data, x_axis, y_axes):
    
    angle = data[x_axis] / 180 * np.pi
    
    for y_axis in y_axes:
        mag   = data[y_axis]

        axes.plot(angle, mag, label=y_axis)

    axes.axes.set_theta_zero_location('N')
    axes.set_theta_direction(-1)
    axes.set_rlabel_position(0)
    axes.set_xticks(np.pi/180. * np.linspace(0,  360, 12, endpoint=False))
    axes.spines['polar'].set_color('darkgray')


if __name__ == "__main__":
    pass

    # file = 'data/radiation_pattern.csv'
    # data = load_data(file)

    # fig = plt.figure()
    # axes = fig.add_subplot(111, projection='polar')

    # target_freq = '6200000000.0'

    # plot(axes, data, target_freq)

    # plt.show()