import sys
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


temp = sys.argv[1]
cell = 20
simtime = 100000


def plot_conv(start, end, step, x, y, z, results_path):
    time, diff_coef = make_conv_table(step, x, y, z, results_path)
    fig, ax = plt.subplots()
    ax.scatter(time[start:end], diff_coef[start:end])
    ax.set(xlabel='Duration of part (ps)',
           ylabel='Diff coed (Ang^2/ps)',
           title='plot_diff_coef')
    ax.grid()
    fig.savefig(f'{results_path}/conv.{start}-{end}.png')
    return np.mean(diff_coef[start:end])


def make_conv_table(step, x, y, z, results_path):
    with open(f'{results_path}/dif_coef_table.txt', 'w') as file:
        time_list = []
        diff_coef_list = []
        for ts in range(5, 1000, step):
            diff_c = diff_coef(ts, x, y, z, results_path)
            time_list.append(ts)
            diff_coef_list.append(diff_c)
            file.write(f'{ts};{diff_c}\n')
    return (time_list, diff_coef_list)


def radius_square(i, k, x, y, z):
    return (x[(i+1)*k]-x[i*k]) ** 2 +\
           (y[(i+1)*k]-y[i*k]) ** 2 +\
           (z[(i+1)*k]-z[i*k]) ** 2


def diff_coef(duration_of_part, x, y, z, results_path, total_time=25000, hist='no'):
    diff_coef_list = []
    number_of_part = total_time//duration_of_part
    for i in range(number_of_part):
        R = radius_square(i, duration_of_part, x, y, z)
        D = R/6/duration_of_part
        diff_coef_list.append(D)
    if hist == 'yes':
        fig, ax = plt.subplots()
        ax.hist(diff_coef_list/np.mean(diff_coef_list),
                bins=len(diff_coef_list)//10)
        fig.savefig(f'{results_path}/hist_dt{duration_of_part}.png')
    return np.mean(diff_coef_list)


results_path = f'../Results/cell.{cell}.time.{simtime}/temp.{temp}'

data = np.genfromtxt(f'{results_path}/coords_unwraped.txt',
                     delimiter=';', names=True)
time = np.array(data['time'])
x_coords = np.array(data['x'])
y_coords = np.array(data['y'])
z_coords = np.array(data['z'])

print(plot_conv(5, 500, 1, x_coords, y_coords, z_coords, results_path))
diff_coef(100, x_coords, y_coords, z_coords, results_path, hist='yes')
diff_coef(500, x_coords, y_coords, z_coords, results_path, hist='yes')
diff_coef(1000, x_coords, y_coords, z_coords, results_path, hist='yes')
