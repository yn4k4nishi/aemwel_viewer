import csv
from matplotlib import projections
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        reader.__next__()
        reader.__next__()

        header = reader.__next__()

        freqs = header[1:]
    
        values = [np.array([])] * len(header)

        data = dict(zip(header, values))

        for r in reader:
            for i in range(len(header)):
                data[header[i]] = np.append(data[header[i]], float(r[i]))


        return data, freqs

def plot(axes, data, target_freq):
    angle = data['rad'] / 180 * np.pi
    mag   = data[target_freq]

    axes.plot(angle, mag)

    axes.axes.set_theta_zero_location('N')
    axes.set_theta_direction(-1)
    axes.set_rlabel_position(0)
    axes.set_xticks(np.pi/180. * np.linspace(0,  360, 12, endpoint=False))
    axes.spines['polar'].set_color('darkgray')


if __name__ == "__main__":
    file = 'data/radiation_pattern.csv'
    data = load_data(file)

    fig = plt.figure()
    axes = fig.add_subplot(111, projection='polar')

    target_freq = '6200000000.0'

    plot(axes, data, target_freq)

    plt.show()