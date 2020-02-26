import sys
import numpy as np
import matplotlib.pyplot as plt


cell = sys.argv[1]
simtime = sys.argv[2]
temp = sys.argv[3]
data_path = f'../Data/cell.{cell}.time.{simtime}/temp.{temp}/'
results_path = f'../Results/cell.{cell}.time.{simtime}/temp.{temp}/'


def make_plot(filename):
    data = np.genfromtxt(filename, delimiter=';', skip_header=1)
    time = data[0:10, 0]
    temp = data[0:10, 2]
    press = data[0:10, 3]
    print(temp)
    ave_temp = np.mean(temp)
    ave_press = np.mean(press)
    fig, axs = plt.subplots(2, 1)
    axs[0].scatter(time, temp)
    axs[0].set_xlim(0, 10)
    axs[0].set_xlabel('Time, ps')
    axs[0].set_ylabel('Temp, K')
    axs[0].grid(True)
    axs[1].plot(time, press)
    axs[1].set_xlim(0, 10)
    axs[1].set_xlabel('Time, ps')
    axs[1].set_ylabel('Press, K')
    axs[1].grid(True)
    fig.savefig('plot')
    plt.show()
    return (ave_temp, ave_press)


print(make_plot(data_path + 'thermo_msd'))
# TODO: mean error for temp and press
