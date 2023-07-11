import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from .nc_data import nc_data


# 绘制热力图
def map_paint(in_data: nc_data, in_name: str, in_month: int, in_map_name: str):
    plt.clf()
    name = in_map_name
    x, y, data_plt_data = in_data.paint_sub_process(in_name, in_month)
    hot_map: Basemap = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90,
                               llcrnrlon=0, urcrnrlon=360, resolution='l')
    hot_map.drawmapboundary()
    hot_map.drawstates()
    hot_map.drawcoastlines()
    hot_map.drawparallels(np.arange(-90., 91., 15.), labels=[1, 0, 0, 0], fontsize=12)
    hot_map.drawmeridians(np.arange(0., 361., 50.), labels=[0, 0, 0, 1], fontsize=12)
    cmap_color = plt.cm.get_cmap("Accent_r")
    curve = hot_map.contour(x, y, data_plt_data, latlon=True)
    shade = hot_map.contourf(x, y, data_plt_data, cmap=cmap_color, latlon=True)

    cbar = hot_map.colorbar(shade, location='right')
    cbar.ax.tick_params(labelsize=12)
    plt.title(name)
    os.chdir("../.cache")
    plt.savefig("heat_map.jpg")
