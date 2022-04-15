from plot import cartesian2D
from plot import polar
from plot import heatmap

from enum import Enum

import csv
import numpy as np


class PlotForm(Enum):
    cartesian2D = 1
    polar       = 2
    heatmap     = 3
        
def load_data(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        reader.__next__()
        reader.__next__()

        header = reader.__next__()
    
        values = [np.array([])] * len(header)

        data = dict(zip(header, values))

        for r in reader:
            for i in range(len(header)):
                data[header[i]] = np.append(data[header[i]], float(r[i]))

        return data