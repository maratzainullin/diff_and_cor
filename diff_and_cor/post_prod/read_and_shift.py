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
            time.append(float(line.split(';')[0]))
            x_coord.append(float(line.split(';')[1]))
            y_coord.append(float(line.split(';')[2]))
            z_coord.append(float(line.split(';')[3][:-1]))
    return [time, x_coord, y_coord, z_coord]

def shift_coords(list_coord, L, a):
    for i in range(len(list_coord)-1):
        if list_coord[i+1]-list_coord[i] <= (0-L*a/2):
            list_coord = list_coord[:i+1] + [j+L*a for j in list_coord[i+1:]]
        elif list_coord[i+1]-list_coord[i] >= L*a/2:
            list_coord = list_coord[:i+1] + [j-L*a for j in list_coord[i+1:]]
    return list_coord

def radius_square(i, k):
    return (x_coord[(i+1)*k]-x_coord[i*k])**2 + (y_coord[(i+1)*k]-y_coord[i*k])**2 + (z_coord[(i+1)*k]-z_coord[i*k])**2

# def radius_square(i, k):
#     return (x_coord[(i+1)*k-1]-x_coord[i*k])**2 + (y_coord[(i+1)*k-1]-y_coord[i*k])**2 + (z_coord[(i+1)*k-1]-z_coord[i*k])**2
#  but you need to add initial coord of sia in coord list ie 4.5 4.5 4.5 * lattice lenght = 12.9204

# def diff_coef(number_of_part, total_time=100000, restart_step=10):
#     """
#     number_of_part -- число разбиений траектории на равные по времени отрезки
#     restart_step -- временной шаг, с которым делаются рестарты
#     restarts_in_part -- число рестартов в одном отрезке
#     duration_of_part -- длительность одного отрезка в пс
#     number_of_restarts -- число рестартов на всей траектоии
#     total_time -- длительность всей траектории в пс
#     """
#     diff_coef_list = []
#     #R_list = []
#     number_of_restarts = total_time/restart_step
#     restarts_in_part = int(number_of_restarts//number_of_part)
#     duration_of_part = restarts_in_part*restart_step
#     #print(number_of_restarts, duration_of_part, restarts_in_part)
#     for i in range(number_of_part):
#         R = radius_square(i, restarts_in_part)
#         #R_list.append(R)
#         diff_coef_list.append(R/6/duration_of_part)
#     # n_bins = len(diff_coef_list)
#     # plt.hist(diff_coef_list, bins=n_bins)
#     # plt.show()
#     return mean(diff_coef_list)

def diff_coef(duration_of_part, total_time=1000, restart_step=10):
    """
    number_of_part -- число разбиений траектории на равные по времени отрезки
    restart_step -- временной шаг, с которым делаются рестарты
    restarts_in_part -- число рестартов в одном отрезке
    duration_of_part -- длительность одного отрезка в пс
    number_of_restarts -- число рестартов на всей траектоии
    total_time=100000 -- длительность всей траектории в пс
    """
    diff_coef_list = []
    number_of_part = total_time//duration_of_part
    number_of_restarts = total_time/restart_step
    restarts_in_part = duration_of_part//restart_step
    # restarts_in_part = int(number_of_restarts//number_of_part)
    for i in range(number_of_part):
        R = radius_square(i, restarts_in_part)
        diff_coef_list.append(R/6/duration_of_part)
    n_bins = len(diff_coef_list)
    plt.hist(diff_coef_list/mean(diff_coef_list), bins=n_bins)
    plt.show()
    return mean(diff_coef_list)


lattice_lenght = float(sys.argv[1])
temp = sys.argv[2]
duration_of_part = int(sys.argv[3])
# lattice_lenght = int(input())
# temp = input()

size_of_sell = 12
# lattice_lenght = 2.8712
data = read_table('./coords/coords_' + temp)

x_coord = shift_coords(data[1], size_of_sell, lattice_lenght) #учет пгу
y_coord = shift_coords(data[2], size_of_sell, lattice_lenght)
z_coord = shift_coords(data[3], size_of_sell, lattice_lenght)

for i in range(100):
    print('old=', data[1][i], ' new=', x_coord[i], ' delta=', data[1][i]-x_coord[i])


# print(diff_coef(duration_of_part))
# with open('data_diff', 'a') as file:
#     str = str(duration_of_part) + ';' + str(diff_coef(duration_of_part)) + '\n'
#     file.write(str)
