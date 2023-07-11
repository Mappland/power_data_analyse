from .nc_data import nc_data


# nc_data_set class
class nc_data_set:
    # 使该类成为可迭代类，使用for items in nc_data_set便利
    def __init__(self, data_1: nc_data, data_2: nc_data,
                 data_3: nc_data, data_4: nc_data, data_5: nc_data):
        self.data = [data_1, data_2, data_3, data_4, data_5]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        current_data = self.data[self.index]
        self.index += 1
        return current_data
