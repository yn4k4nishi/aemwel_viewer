from operator import ne
from plot import cartesian2D
from plot import polar
from plot import heatmap

from enum import Enum

import csv
import numpy as np

import skrf as rf


class PlotForm(Enum):
    cartesian2D = 1
    polar       = 2
    heatmap     = 3
        
def load_data(file_name):

    if file_name.endswith('.csv'):
        with open(file_name, 'r') as f:
            reader = csv.reader(f)

            header = reader.__next__()
            while '!' in header[0]: ## skip comment
                header = reader.__next__()
        
            values = [np.array([])] * len(header)

            data = dict(zip(header, values))

            for r in reader:
                for i in range(len(header)):
                    data[header[i]] = np.append(data[header[i]], float(r[i]))

            return data
    
    elif file_name.endswith('.s2p') or file_name.endswith('.s4p'):
        net = rf.Network(file_name)

        data = dict()

        data['freq_GHz'] = net.frequency.f / 1e9

        for i in range(net.s.shape[1]):
            for j in range(net.s.shape[2]):
                key = 'S{}{}_db'.format(i+1, j+1)
                data[key] = net.s_db[:, i, j]

                key = 'S{}{}_deg'.format(i+1, j+1)
                data[key] = net.s_deg[:, i, j]

        return data