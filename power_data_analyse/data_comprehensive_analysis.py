import os
import numpy as np
import matplotlib.pyplot as plt
from .data_set import nc_data_set


def data_comprehensive_analysis(in_data_set: nc_data_set, in_name: str, in_title: str):
    plt.clf()
    x_axis_data = [2017.01, 2017.02, 2017.03, 2017.04, 2017.05, 2017.06, 2017.07, 2017.08, 2017.09, 2017.10, 2017.11,
                   2017.12,
                   2018.01, 2018.02, 2018.03, 2018.04, 2018.05, 2018.06, 2018.07, 2018.08, 2018.09, 2018.10, 2018.11,
                   2018.12,
                   2019.01, 2019.02, 2019.03, 2019.04, 2019.05, 2019.06, 2019.07, 2019.08, 2019.09, 2019.10, 2019.11,
                   2019.12,
                   2020.01, 2020.02, 2020.03, 2020.04, 2020.05, 2020.06, 2020.07, 2020.08, 2020.09, 2020.10, 2020.11,
                   2020.12,
                   2021.01, 2021.02, 2021.03, 2021.04, 2021.05, 2021.06, 2021.07, 2021.08, 2021.09, 2021.10, 2021.11,
                   2021.12]  # x
    use_data_set = in_data_set
    y_axis_data = []  # y
    for item in use_data_set:
        for i in range(12):
            data_variables = item.data_variables_data[in_name][:]
            data = np.array(data_variables)
            data_plt = data[i, :, :]
            y_axis_data += [np.mean(data_plt)]

    plt.plot(x_axis_data, y_axis_data, 'b*--', alpha=0.5, linewidth=1, label='acc')

    plt.legend()
    plt.xlabel("time")
    plt.ylabel("data")
    plt.title(in_title)
    os.chdir("../.cache")
    plt.savefig("data_com_img.jpg")
