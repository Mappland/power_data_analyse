# import power_data_analyse as pa
# import os
#
# if __name__ == "__main__":
#     os.chdir(r"./files")
#     nc_data_17 = pa.nc_data(r"power_901_monthly_2017_ceres_utc.nc")
#     nc_data_18 = pa.nc_data(r"power_901_monthly_2018_ceres_utc.nc")
#     nc_data_19 = pa.nc_data(r"power_901_monthly_2019_ceres_utc.nc")
#     nc_data_20 = pa.nc_data(r"power_901_monthly_2020_ceres_utc.nc")
#     nc_data_21 = pa.nc_data(r"power_901_monthly_2021_ceres_utc.nc")
#     name = "SKY_BRIGHTNESS"
#
#     # 绘制热力图
#     pa.map_paint(nc_data_17, "AIRMASS", 6, "AIRMASS_MAP")
#
#     # 设置数据集并进行绘制
#     data_set_1 = pa.nc_data_set(nc_data_17, nc_data_18, nc_data_19, nc_data_20, nc_data_21)
#     pa.data_analyse(data_set_1, "AIRMASS", "AIRMASS 2017-2021")
