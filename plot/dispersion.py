
from operator import le


def plot(axes, data, data_port, ncell, lcell, m1, m2, **kwargs):
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

    axes.set_xlabel(r'$\Delta \beta p / \pi$')
    axes.set_ylabel('Frequency [GHz]')
    axes.set_xlim([-0.5, 0.5])

    if 'xmax' in kwargs:
        axes.set_xlim([kwargs['xmin'], kwargs['xmax']])
    if 'ymax' in kwargs:
        axes.set_ylim([kwargs['ymin'], kwargs['ymax']])

    freq = data['freq_GHz']

    beta_p =  (data['S21_deg'] - data_port['S21_deg']) / 180 / ncell - m1 / ncell
    beta_m = -(data['S12_deg'] - data_port['S12_deg']) / 180 / ncell + m2 / ncell

    beta_d = (beta_p + beta_m)/2

    data_p = [[]]
    data_m = [[]]

    ## Wrap phase
    for i in range(len(beta_p)):
        while beta_p[i] < 0.5:
            beta_p[i] += 1
        
        while beta_p[i] > 0.5:
            beta_p[i] -= 1

        while beta_m[i] < 0.5:
            beta_m[i] += 1
    
        while beta_m[i] > 0.5:
            beta_m[i] -= 1
    
    for i in range(len(beta_p)-1):
        data_p[-1].append(beta_p[i])
        data_m[-1].append(beta_m[i])

        if abs(beta_p[i+1] - beta_p[i]) > 0.5:
            data_p.append([])
        
        if abs(beta_m[i+1] - beta_m[i]) > 0.5:
            data_m.append([])
        

    # for i in range(len(beta_p)):

    #     if abs(beta_p[i] + tp) > 0.5:
    #         data_p.append([])
    #         tp += 1

    #     if abs(beta_m[i] + tm) > 0.5:
    #         data_m.append([])
    #         tm -= 1

    #     data_p[-1].append(beta_p[i] + tp)
    #     data_m[-1].append(beta_m[i] + tm)

    ip = 0
    im = 0

    axes.plot(data_p[0][0], freq[0], label=r'$\beta_p$', color='blue', lw=3)
    axes.plot(data_m[0][0], freq[0], label=r'$\beta_m$', color='red' , lw=3)

    for bp in data_p:
        axes.plot(bp, freq[ip:ip+len(bp)], color='blue', lw=3)
        ip += len(bp)
    
    for bm in data_m:
        axes.plot(bm, freq[im:im+len(bm)], color='red' , lw=3)
        im += len(bm)

    axes.plot(beta_d, freq, label=r'$\Delta\beta$', color='black', lw=3)
