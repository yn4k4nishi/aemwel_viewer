import csv
import numpy as np
import matplotlib.pyplot as plt


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
    x = np.take(data['x'],         np.where(data['z'] == target_z))
    y = np.take(data['y'],         np.where(data['z'] == target_z))
    z = np.take(data[target_freq], np.where(data['z'] == target_z))

    x_grid, y_grid = np.meshgrid(x, y)
    z_grid = z.reshape(len(x), len(y))
    
    heatmap = plt.pcolormesh(x_grid, y_grid, z_grid, cmap='plasma') 


if __name__ == "__main__":
    file = 'data/xyz_phase.csv'
    data = load_data(file)

    fig = plt.figure()
    axes = fig.add_subplot(111)

    target_z = 0
    target_freq = '500000000.0'

    plot(axes, data, target_z, target_freq)

    plt.show()
