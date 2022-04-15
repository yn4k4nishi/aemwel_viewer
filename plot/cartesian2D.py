

def plot(axes, data, x_axis, y_axes):
    axes.set_xlabel(x_axis)

    for y_axis in y_axes:
        axes.plot(data[x_axis], data[y_axis], label=y_axis)
