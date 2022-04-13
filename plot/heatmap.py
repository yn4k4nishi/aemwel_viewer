import csv
from termios import VMIN
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def load_data(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        reader.__next__()
        reader.__next__()

        header = reader.__next__()
    
        values = [[]] * len(header)

        data = dict(zip(header, values))

        for r in reader:
            for i in range(len(header)):
                data[header[i]].append( float(r[i]) )

        return data

            

def plot(axes, data, target_z, target_freq):
    x = np.take(np.array(data['x']        ), np.where(np.array(data['z']) == target_z)[0])
    y = np.take(np.array(data['y']        ), np.where(np.array(data['z']) == target_z)[0])
    z = np.take(np.array(data[target_freq]), np.where(np.array(data['z']) == target_z)[0])

    # heatmap = axes.pcolormesh(x, y, z, cmap='jet')
    

if __name__ == "__main__":
    file = 'data/xyz_phase.csv'
    data = load_data(file)

    fig = plt.figure()
    axes = fig.add_subplot(111)

    target_z = 0.0
    target_freq = '1680000000.0'

    plot(axes, data, target_z, target_freq)

    # plt.show()
