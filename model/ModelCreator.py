import numpy as np
from scipy import interpolate
from parsing.DocParser import DocParser, cut_list
from model.Model import Model


class ModelCreator:
    def read_model(self, filename_depths: str, receiver_coords: np.ndarray, step: int):
        parser = DocParser(filename_depths)
        max_depth, abs_depths = self.__get_abs_depths(parser)
        speeds = self.__get_speeds(parser, abs_depths)
        speed_func = self.__regularization_data(abs_depths, speeds)
        field = self.__create_field(0,
                                    speed_func,
                                    self.__calc_size(0, max_depth, step),
                                    self.__calc_weigh(receiver_coords, step),
                                    step)
        return Model(step, field, max_depth)

    def __get_abs_depths(self, parser: DocParser) -> tuple:
        abs_depths = [float(elem) for elem in cut_list(parser.get_column_data(2))]
        max_depth = abs(min(abs_depths))
        abs_depths = [elem + max_depth for elem in abs_depths]
        return max(abs_depths), abs_depths

    def __get_speeds(self, parser: DocParser, abs_depths: np.ndarray) -> np.ndarray:
        speeds = [float(elem) for elem in parser.get_column_data(8)]
        return np.array(cut_list(speeds, len(speeds) - len(abs_depths)))

    def __regularization_data(self, abs_depth: np.ndarray, speeds: np.ndarray):
        return interpolate.interp1d(abs_depth, speeds)

    def __create_field(self, start_depth: int, speed_func, length: int, weigh: int, step: int) -> np.ndarray:
        field = np.ones((length, weigh))
        for i in range(length):
            field[i] = field[i] / speed_func(start_depth + step * i)
        return field

    def __calc_size(self, start: float, end: float, step: int) -> int:
        size = (int(end - start)) // step
        if (int(end - start)) % step:
            size += 1
        return size

    def __calc_weigh(self, coords: np.ndarray, step: int) -> int:
        return self.__calc_size(min(coords, key=lambda arr: arr[0])[0], max(coords, key=lambda arr: arr[0])[0], step)
