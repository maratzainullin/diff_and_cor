# python read_and_shift.py 2.8712 1300
from numpy import mean
import sys
import matplotlib
import matplotlib.pyplot as plt

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

def radius_square(i, k):
    return (x_coord[(i+1)*k]-x_coord[i*k])**2 + (y_coord[(i+1)*k]-y_coord[i*k])**2 + (z_coord[(i+1)*k]-z_coord[i*k])**2

def diff_coef(duration_of_part, total_time=50000, restart_step=1):
    diff_coef_list = []
    number_of_part = total_time//duration_of_part
    for i in range(number_of_part):
        R = radius_square(i, duration_of_part)
        diff_coef_list.append(R/6/duration_of_part)
    # n_bins = len(diff_coef_list)
    # plt.hist(diff_coef_list/mean(diff_coef_list), bins=n_bins)
    # plt.show()
    return mean(diff_coef_list)


lattice_lenght = float(sys.argv[1])
temp = sys.argv[2]
duration_of_part = int(sys.argv[3])


size_of_sell = 10
data = read_table('ws_700_coords_unwraped')
x_coord = data[1]
y_coord = data[2]
z_coord = data[3]


print(diff_coef(duration_of_part))
with open('data_diff', 'a') as file:
    str = str(duration_of_part) + ';' + str(diff_coef(duration_of_part)) + '\n'
    file.write(str)
