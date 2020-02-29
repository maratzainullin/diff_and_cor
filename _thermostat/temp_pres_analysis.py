# import sys
import numpy as np
import matplotlib.pyplot as plt


# cell = sys.argv[1]
# simtime = sys.argv[2]
# temp = sys.argv[3]
cell = 10
simtime = 100
temp = 900
input_file = f'./Data/{cell}.{simtime}.{temp}.data'
output_file = f'./Results/{cell}.{simtime}.{temp}.'


def add_titlebox(ax, text):
    ax.text(.55, .8, text,
            horizontalalignment='center',
            transform=ax.transAxes,
            bbox=dict(facecolor='white', alpha=0.6),
            fontsize=12.5)
    return ax


def do_anal(x, y, x_name, y_name, output_file, start=0):
    x = x[start:]
    y = y[start:]
    y_std = y.std()
    y_mean = y.mean()
    err = y - y.mean()
    fig, (ax_err, ax_hist) = plt.subplots(2, 1, figsize=(8, 8))
    ax_err.plot(x, err)
    ax_err.set_title(f'{y_name}_err_std vs {x_name}')
    ax_err.set_xlabel(x_name)
    ax_err.set_ylabel(f'{y_name}_err_std')
    ax_err.grid(True)
    ax_hist.hist(y, bins=len(y))
    ax_hist.set_title(f'{y_name} distribution')
    add_titlebox(ax_hist, f'mean={y_mean}, std_err={y_std}')
    fig.savefig(output_file + y_name + '.png')
    plt.show()


data = np.genfromtxt(input_file, delimiter=';', skip_header=1)
temp = np.array(data[:, 1])
press = np.array(data[:, 2])
do_anal(data[:, 0], temp, 'Time', 'Temp', output_file, start=150)
do_anal(data[:, 0], press, 'Time', 'Press', output_file, start=150)
