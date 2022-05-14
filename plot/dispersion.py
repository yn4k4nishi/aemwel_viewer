
from cProfile import label
from telnetlib import TM


def plot(axes, data, data_port, ncell, m):
    """分散曲線のプロット

    Parameters
    ----------
    axes : :obj:`matplotlib.Axes`
        プロットする軸
    data : dict
        .s2pから読み込んだ回路全体のデータ
    data_port : dict
        .s2pから読み込んだポート成分のみのデータ
    ncell : int
        単位セル数
    m : int
        角度の不定性(2 pi m)を補正するための変数
    """

    axes.set_xlim([-0.5, 0.5])

    freq = data['freq_GHz']

    beta_p =  (data['S12_deg'] - data_port['S12_deg']) / 180 / ncell + m / ncell
    beta_m = -(data['S21_deg'] - data_port['S21_deg']) / 180 / ncell - m / ncell

    beta_d = (beta_p + beta_m)/2

    ## Wrap phase
    tp = 0
    tm = 0
    for i in range(len(beta_p)):
        beta_p[i] += tp
        beta_m[i] += tm

        if abs(beta_p[i]) > 0.5:
            tp += 1

        if abs(beta_m[i]) > 0.5:
            tm -= 1


    axes.scatter(beta_d, freq, label=r'$\Delta\beta$')
    axes.scatter(beta_p, freq, label=r'$\beta_p$')
    axes.scatter(beta_m, freq, label=r'$\beta_m$')



