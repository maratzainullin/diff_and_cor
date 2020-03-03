import sys
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


cell = 20
simtime = 1000000


def add_titlebox(ax, text):
    ax.text(.8, .8, text,
            horizontalalignment='center',
            transform=ax.transAxes,
            bbox=dict(facecolor='white', alpha=0.6),
            fontsize=11)
    return ax


def make_plot(x, y, z, output_file, s=0):
    y_std = y[s:].std()
    z_std = z[s:].std()
    y_mean = y[s:].mean()
    z_mean = z[s:].mean()
    y_wr = y.mean()
    z_wr = z.mean()
    fig, (ax_temp, ax_press) = plt.subplots(2, 1, figsize=(6, 8))
    ax_temp.plot(x[:s], z[:s], linewidth=0.5, color='lightcoral')
    ax_temp.set_xlabel('Time')
    ax_temp.set_ylabel(f'Press')
    ax_temp.grid(True)
    ax_press.plot(x, z, linewidth=0.5, color='lightcoral')
    ax_press.set_xlabel('Time')
    ax_press.set_ylabel(f'Press')
    ax_press.grid(True)
    add_titlebox(ax_temp, f'mean={y_mean}\nerr={y_std}\nwr={y_wr}')
    add_titlebox(ax_press, f'mean={z_mean}\nerr={z_std}\nwr={z_wr}')
    fig.savefig(output_file + '.png')
    plt.show()


def analysis(temp):
    input_path = f'../Data/cell.{cell}.time.{simtime}/temp.{temp}/'
    output_path = f'../Results/cell.{cell}.time.{simtime}/temp.{temp}/'
    data = np.genfromtxt(f'{input_path}thermo_msd.txt',
                         delimiter=';', names=True)
    time = np.array(data['time'])
    msd = np.array(data['sia_msd'])
    temp = np.array(data['temp'])
    press = np.array(data['press'])
    a, b = np.polyfit(time, msd, 1)
    print(a/6, b, time[-1])
    print(f'{temp.mean()}±{temp.std()}, {press.mean()}±{press.std()}\n')


for temp in (700, 900, 1100, 1300):
    analysis(temp)
