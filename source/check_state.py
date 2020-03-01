import sys
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


temp = sys.argv[1]
cell = 20
simtime = 500

input_file = f'./Data/{cell}.{simtime}.{temp}.data'
output_file = f'./Results/{cell}.{simtime}.{temp}.'



def add_titlebox(ax, text):
    ax.text(.8, .8, text,
            horizontalalignment='center',
            transform=ax.transAxes,
            bbox=dict(facecolor='white', alpha=0.6),
            fontsize=11)
    return ax


def do_anal(x, y, z, output_file, s=0):
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


data = np.genfromtxt(input_file, delimiter=';', skip_header=1)
temp = np.array(data[:, 1])
press = np.array(data[:, 2])
print(f'{temp[500:].mean()}±{temp[500:].std()}, {press[500:].mean()}±{press[500:].std()}')
#do_anal(data[:, 0], temp, press, output_file, s=500)
