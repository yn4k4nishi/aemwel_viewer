import csv


def load_data(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        for r in reader:
            print(r)

def plot(axes):
    axes.plot([0,1,2,3,4], [10,1,20,3,40])
