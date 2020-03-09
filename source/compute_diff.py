import sys
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


temp = sys.argv[1]
cell = 20
simtime = 100000


data_path = f'../Data/cell.{cell}.time.{simtime}/temp.{temp}'
results_path = f'../Results/cell.{cell}.time.{simtime}/temp.{temp}'


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


def diff_coef(duration_of_part, x, y, z, results_path, hist='no'):
    total_time = len(x) - 1
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


def traced_diff_coef(input_path):
    data = np.genfromtxt(f'{input_path}/thermo_msd.txt',
                         delimiter=';', names=True)
    time = np.array(data['time'])
    msd = np.array(data['sia_msd'])
    temp = np.array(data['temp'])
    press = np.array(data['press'])
    a, b = np.polyfit(time, msd, 1)
    return (a/6, temp.mean(), press.mean(), temp.std(), press.std())


data = np.genfromtxt(f'{results_path}/coords_unwraped.txt',
                     delimiter=';', names=True)
time = np.array(data['time'])
x_coords = np.array(data['x'])
y_coords = np.array(data['y'])
z_coords = np.array(data['z'])

wsa_diff = plot_conv(5, 500, 1, x_coords, y_coords, z_coords, results_path)
thermo_data = traced_diff_coef(data_path)
traced_diff = thermo_data[0]
temp_mean = thermo_data[1]
press_mean = thermo_data[2]
print(f'WSA_diff = {wsa_diff};\n'
    f'Traced_diff = {traced_diff};\n'
    f'Corr_f = {traced_diff/wsa_diff};\n'
    f'Temp = {temp_mean};\n'
    f'Press = {press_mean};\n')
with open(f'../final_result.txt', 'a') as file:
    file.write(f'WSA_diff = {wsa_diff};\n'
                f'Traced_diff = {traced_diff};\n'
                f'Corr_f = {traced_diff/wsa_diff};\n'
                f'Temp = {temp_mean};\n'
                f'Press = {temp_mean};\n\n')

diff_coef(100, x_coords, y_coords, z_coords, results_path, hist='yes')
diff_coef(500, x_coords, y_coords, z_coords, results_path, hist='yes')
diff_coef(1000, x_coords, y_coords, z_coords, results_path, hist='yes')
