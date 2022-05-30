from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

def plot(data, xaxis, y_props, title, xlabel, font_size, fig_size, legend, **opt):
    """2次元直交座標のプロット
    
    Parameters
    ----------
    """

    plt.rcParams['font.size'] = font_size

    fig, ax = plt.subplots(figsize=fig_size)
    ax.set_title(title)

    ax.set_xlabel(xlabel)

    if 'xmax' in opt:
        ax.set_xlim([opt['xmin'], opt['xmax']])
    if 'ymax' in opt:
        ax.set_ylim([opt['ymin'], opt['ymax']])


    for i in range(len(y_props)):
        if y_props[i].is_enabled:
            ax.plot(
                data[xaxis], 
                data[y_props[i].name],
                label=y_props[i].label,
                color=y_props[i].color,
                lw=y_props[i].lw,
                linestyle=y_props[i].style
            )


    if legend:
        fig.legend()

    plt.show()