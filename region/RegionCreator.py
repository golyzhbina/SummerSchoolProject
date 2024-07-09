from region.Region import Region
import numpy as np


class RegionCreator:

    @staticmethod
    def create_region(start_x, start_y, end_x, end_y, step) -> Region:
        amount_x = int((end_x - start_x) / step)
        amount_y = int((end_y - start_y) / step)
        return Region(start_x,
                      start_y,
                      amount_x,
                      amount_y,
                      step,
                      np.array([(x * step + start_x, y * step + start_y) for x in range(amount_x) for y in
                                range(amount_y)]))