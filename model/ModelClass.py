import numpy as np
from parsing.DataClass import Data


class Model:
    def __init__(self,
                 filename: str,
                 step: int,
                 start_depth: int,
                 end_depth: int,
                 start_weigh: float,
                 end_weigh: float):
        self.step = step
        self.length = self.__calc_size(abs(start_depth), abs(end_depth))
        self.weigh = self.__calc_size(start_weigh, end_weigh)
        self.data = Data(filename)
        self.data.regularization_data()
        self.__create_field(start_depth)

    def __calc_size(self, start: [int, float], end: [int, float]) -> int:
        size = (int(end - start)) // self.step
        if (int(end - start)) % self.step:
            size += 1
        return size

    def __create_field(self, start_depth: int):
        self.field = np.ones((self.length, self.weigh))
        for i in range(self.length):
            self.field[i] = self.field[i] / np.sqrt(self.data.speed_func(start_depth + self.step * i))


"""
model = Model("C:\\Users\\golub\\test2\\pythonProject1\\vel.docx",
              10,
              0,
              2219,
              0,
              1000)
print(model.field)
"""