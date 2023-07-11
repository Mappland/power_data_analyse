import numpy as np
import matplotlib.pyplot as plt
from .data_set import nc_data_set
import os


# 数据处理
def data_analyse(in_data_set: nc_data_set, in_name: str, in_title: str):
    plt.clf()
    x_axis_data = [2017, 2018, 2019, 2020, 2021]  # x
    y_axis_data = []  # y

    for item in in_data_set:
        data_variables = item.data_variables_data[in_name][:]
        data = np.array(data_variables)
        data_plt = data[12, :, :]
        y_axis_data += [np.mean(data_plt)]

    plt.plot(x_axis_data, y_axis_data, 'b*--', alpha=0.5, linewidth=1, label='acc')

    plt.legend()
    plt.xlabel("time")
    plt.ylabel("data")
    plt.title(in_title)
    os.chdir("../.cache")
    plt.savefig("data_img.jpg")
