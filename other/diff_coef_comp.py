# python read_and_shift.py 2.8712 1300
from numpy import mean
import sys
import matplotlib
import matplotlib.pyplot as plt
cell = sys.argv[1]
simtime = sys.argv[2]
temp = sys.argv[3]

dumps_path = f'../Data/cell.{cell}.time.{simtime}/temp.{temp}'
output_path = f'../Results/cell.{cell}.time.{simtime}/temp.{temp}'

def read_table(file_name):
    time = []
    x_coord = []
    y_coord = []
    z_coord = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            time.append(float(line.split(' ')[0]))
            x_coord.append(float(line.split(' ')[2]))
            y_coord.append(float(line.split(' ')[3]))
            z_coord.append(float(line.split(' ')[4][:-1]))
    return [time, x_coord, y_coord, z_coord]


def plot_conv(start, end, step):
    x, y = make_conv_table(step)
    # plt.plot(x[start:end],y[start:end])
    fig, ax = plt.subplots()
    ax.plot(x[start:end], y[start:end])
    ax.set(xlabel='Duration of part (ps)', ylabel='Diff coed (Ang^2/ps)', title='plot_diff_coef_' + temp)
    ax.grid()
    fig.savefig(f'{output_path}/conv.{start}-{end}.png')
    return mean(y[start:end])


def make_conv_table(step):
    with open(f'{output_path}/dif_coef_table.txt', 'w') as file:
        x = []
        y = []
        for i in range(5, 1000, step):
            D = diff_coef(i)
            x.append(i)
            y.append(D)
            n = i
            strg = str(n) + ';' + str(D) + '\n'
            file.write(strg)
    return x, y


def radius_square(i, k):
    return (x_coord[(i+1)*k]-x_coord[i*k]) ** 2 + (y_coord[(i+1)*k]-y_coord[i*k]) ** 2 + (z_coord[(i+1)*k]-z_coord[i*k]) ** 2

# lamda radius_square i,k:(x_coord[(i+1)*k]-x_coord[i*k]) ** 2 + (y_coord[(i+1)*k]-y_coord[i*k]) ** 2 + (z_coord[(i+1)*k]-z_coord[i*k]) ** 2


def diff_coef(duration_of_part, total_time=25000, restart_step=1, hist='no'):
    diff_coef_list = []
    number_of_part = total_time//duration_of_part
    for i in range(number_of_part):
        R = radius_square(i, duration_of_part)
        D = R/6/duration_of_part
        diff_coef_list.append(D)
    if hist == 'yes':
        fig, ax = plt.subplots()
        n_bins = len(diff_coef_list)//10
        ax.hist(diff_coef_list/mean(diff_coef_list), bins=n_bins)
        fig.savefig(f'{output_path}/hist.png')
    return mean(diff_coef_list)


data = read_table(f'{output_path}/coords_unwraped.txt')
x_coord = data[1]
y_coord = data[2]
z_coord = data[3]

print(plot_conv(100, 200, 1))
diff_coef(100, hist='yes')
