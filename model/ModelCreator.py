import numpy as np
from numpy.ma import ceil
from scipy import interpolate

from region.Region import Region
from model.Model import Model
from parsing.ReceiversCoordsHandler import distance


class ModelCreator:

    @staticmethod
    def create_model(depths: np.ndarray,
                     speeds: np.ndarray,
                     receiver_coords: np.ndarray,
                     region: Region,
                     step: int):
        max_depth, depths = ModelCreator.__get_abs_depths(depths)
        speed_func = ModelCreator.__regularization_data(depths, speeds)
        field = ModelCreator.__create_field(0,
                                            speed_func,
                                            int(ceil(max(depths) / step)),
                                            ModelCreator.__calc_weigh(receiver_coords, region, step),
                                            step)
        return Model(step, field, max_depth)

    @staticmethod
    def __get_abs_depths(depths: np.ndarray) -> tuple:
        max_depth = min(depths)
        depths -= max_depth
        return max_depth, depths

    @staticmethod
    def __regularization_data(abs_depth: np.ndarray, speeds: np.ndarray):
        return interpolate.interp1d(abs_depth, speeds)

    @staticmethod
    def __create_field(start_depth: int, speed_func, length: int, weigh: int, step: int) -> np.ndarray:
        field = np.ones((length, weigh))
        for i in range(length):
            field[i] *= speed_func(start_depth + step * i)
        return field

    @staticmethod
    def __calc_weigh(receivers_coords: np.ndarray, region: Region, step: int) -> int:
        weigh = max([distance(point1[0], point1[1], point2[0], point2[1])
                     for point1 in receivers_coords for point2 in region.list_of_source])
        return int(ceil(weigh / step))
