import numpy as np
import netCDF4 as nc


# nc_data class set
class nc_data:

    def __init__(self, in_path: str):
        # Basic data set
        self.info = {}
        self.dataset = nc.Dataset
        self.file_path = str
        self.data_variables_data = dict

        # data get
        self.file_path = in_path
        self.dataset = nc.Dataset(self.file_path)
        self.data_variables_data = self.dataset.variables
        self.get_info()

    # base_map paint subprocess
    def paint_sub_process(self, in_name: str, in_month: int):
        plt_data = self.data_variables_data[in_name][:]
        plt_lat = self.data_variables_data['lat'][:]
        plt_lon = self.data_variables_data['lon'][:]

        plt_array_lat = np.array(plt_lat)
        plt_array_lon = np.array(plt_lon)
        data_project = np.array(plt_data)
        data_plt_project = data_project[in_month, :, :]
        plt_x, plt_y = np.meshgrid(plt_array_lon, plt_array_lat)
        return plt_x, plt_y, data_plt_project

    # 查看当前数据集重要参数
    def get_info(self):
        dataset = self.dataset
        info = self.info
        info.update({"acknowledgement": dataset.acknowledgement,
                     "comment": dataset.comment,
                     "conventions": dataset.conventions,
                     "creator email": dataset.creator_email,
                     "creator name": dataset.creator_name,
                     "date created": dataset.date_created,
                     "derived from": dataset.derived_from,
                     "derived info": dataset.derived_info,
                     "derived link": dataset.derived_link,
                     "keywords: {}": dataset.keywords,
                     "keywords vocabulary": dataset.keywords_vocabulary,
                     "publisher email": dataset.publisher_email,
                     "publisher name" :dataset.publisher_name,
                     "references": dataset.references,
                     "time coverage end": dataset.time_coverage_end,
                     "time_coverage_start": dataset.time_coverage_start,
                     "time_standard": dataset.time_standard,
                     "version": dataset.version,
                     "variables": "Use nc_data.dataset.variables['item_name'] to get the data"})
