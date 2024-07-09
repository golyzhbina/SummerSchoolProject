import lasio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


class LasParser:

    @staticmethod
    def get_depths_and_speeds(filename: str) -> tuple:

        las_file = lasio.read(filename)
        DTP = las_file.df()["DTP"].values
        DTP = gaussian_filter(DTP, 50)
        TVDSS = np.round(las_file.df()["TVDSS"].values)
        _, TVDSS_indexes = np.unique(TVDSS, return_index=True)

        depths = list()
        speeds = list()

        for i in TVDSS_indexes:
            if not np.isnan(DTP[i]) and not np.isnan(TVDSS[i]):
                depths.append(-TVDSS[i])
                speeds.append(1e6 / DTP[i])
        return depths, speeds
