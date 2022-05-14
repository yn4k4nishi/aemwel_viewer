
from cProfile import label
from operator import le
from telnetlib import TM
from turtle import color


def plot(axes, data, data_port, ncell, lcell, m, **kwargs):
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
    lcell : float
        単セルの長さ
    m : int
        角度の不定性(2 pi m)を補正するための変数
    """

    axes.set_xlabel(r'$\Delta \beta / \pi$')
    axes.set_ylabel('Frequency [GHz]')
    axes.set_xlim([-0.5, 0.5])

    if 'xmax' in kwargs:
        axes.set_xlim([kwargs['xmin'], kwargs['xmax']])
    if 'ymax' in kwargs:
        axes.set_ylim([kwargs['ymin'], kwargs['ymax']])

    freq = data['freq_GHz']

    beta_p =  (data['S12_deg'] - data_port['S12_deg']) / 180 / ncell + m / ncell
    beta_m = -(data['S21_deg'] - data_port['S21_deg']) / 180 / ncell - m / ncell

    beta_d = (beta_p + beta_m)/2

    data_p = [[]]
    data_m = [[]]

    ## Wrap phase
    tp = 0
    tm = 0
    for i in range(len(beta_p)):
        data_p[tp].append(beta_p[i] + tp)
        data_m[tm].append(beta_m[i] - tm)

        if abs(beta_p[i] + tp) > 0.5:
            data_p.append([])
            tp += 1

        if abs(beta_m[i] - tm) > 0.5:
            data_m.append([])
            tm += 1

    ip = 0
    im = 0

    axes.plot(data_p[0][0], freq[0], label=r'$\beta_p$', color='blue')
    axes.plot(data_m[0][0], freq[0], label=r'$\beta_m$', color='red')

    for bp, bm in zip(data_p, data_m):
        axes.plot(bp, freq[ip:ip+len(bp)], color='blue')
        axes.plot(bm, freq[im:im+len(bm)], color='red')

        ip += len(bp)
        im += len(bm)

    axes.plot(beta_d, freq, label=r'$\Delta\beta$', color='black')
