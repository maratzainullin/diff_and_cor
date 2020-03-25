import numpy as np
import matplotlib.pyplot as plt


cell = 12
Lenght = {700: 34.5016 - 0.0583803,
          800: 0,
          900: 34.5481 - 0.0119028,
          1000: 0,
          1100: 34.5979 + 0.0378508,
          1200: 0,
          1300: 0,
          1400: 0,
          1500: 0,
          1600: 0,
          1700: 0,
          1800: 0}
lattice = 2.88


input_path = f'./'
output_path = f'./'


def get_diff(_filename='final_result.txt'):
    _diff_data = np.genfromtxt(_filename, delimiter=';', names=True)
    _diff_col = np.array(_diff_data['WSA_diff'])
    _temp_col = np.array(np.around(_diff_data['Temp'], -2))
    _diffusion_coef = dict(zip(_temp_col, _diff_col))
    return _diffusion_coef


def analysis(_data, _s=600):
    _time = np.array(_data['time'])
    _time = np.sort(_time)
    _count = np.array(range(len(_time), 0, -1))
    log_count = np.log(_count)
    a, b = np.polyfit(_time[:_s], log_count[:_s], 1)
    return (_time, _count, log_count, -a, b)


def make_plot(x, y, _output_file, _s=600, _show=0):
    fig, (ax_temp) = plt.subplots(1, 1, figsize=(8, 6))
    ax_temp.plot(x[:_s], y[:_s], linewidth=1, color='lightcoral')
    ax_temp.set_xlabel('time')
    ax_temp.set_ylabel('count')
    ax_temp.grid(True)
    fig.savefig(_output_file + '.png')
    if _show:
        plt.show()


def comp_radius(_lenght, _diffusion, _lambd):
    volume = _lenght**3
    _recomb_radius = volume*_lambd/_diffusion/4/np.pi
    return _recomb_radius


def do_all(_filename, _temp, _output_path, _s):
    _data = np.genfromtxt(_filename, delimiter=';', names=True)
    _diff = get_diff()
    (_time, _count, _log_count, _k, _n_start) = analysis(_data, _s)
    make_plot(_time, _count, f'{_output_path}{_temp}.lin', _s)
    make_plot(_time, _log_count, f'{_output_path}{_temp}.log', _s)
    _radius = comp_radius(Lenght[_temp], _diff[_temp], _k)
    _radius_lat = _radius/Lenght[_temp]*12
    return (_radius, _radius_lat, _k, _n_start)


for temp in (700, 900, 1100):
    (radius, radius_lat, k, n_start) = do_all(f'time_data_{temp}.txt',
                                              temp, './res/', _s=-1)
    print(f'Temp = {temp} K; Rad = {radius} ang; Rad/lat = {radius_lat};'
          f'k = {k}; N_start = {n_start}')
