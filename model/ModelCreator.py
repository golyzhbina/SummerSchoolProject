import numpy as np
from numpy.ma import ceil
from scipy import interpolate

from Region import Region
from parsing.DocParser import DocParser, cut_list
from model.Model import Model
from parsing.ReceiversCoordsHandler import distance


class ModelCreator:
    def create_model(self, filename_depths: str, receiver_coords: np.ndarray, region: Region, step: int):
        parser = DocParser(filename_depths)
        max_depth, abs_depths = self.__get_abs_depths(parser)
        speeds = self.__get_speeds(parser, abs_depths)
        speed_func = self.__regularization_data(abs_depths, speeds)
        field = self.__create_field(0,
                                    speed_func,
                                    int(ceil(max_depth/step)),
                                    self.__calc_weigh(receiver_coords, region, step),
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
        field = np.ones((length, weigh)) * 1000
        for i in range(length):
            field[i] = field[i] / speed_func(start_depth + step * i)
        return field

    def __calc_weigh(self, receivers_coords: np.ndarray, region: Region, step: int) -> int:
        weigh = max([distance(point1[0], point1[1], point2[0], point2[1])
                     for point1 in receivers_coords for point2 in region.list_op_points])
        print()
        return int(ceil(weigh / step))

