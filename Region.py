from dataclasses import dataclass

import numpy as np


@dataclass
class Region:
    start_x: float
    start_y: float
    amount_x: int
    amount_y: int
    step: int
    list_of_source: np.ndarray


def create_region(start_x, start_y, end_x, end_y, step):
    amount_x = int((end_x - start_x) / step)
    amount_y = int((end_y - start_y) / step)
    return Region(start_x,
                  start_y,
                  amount_x,
                  amount_y,
                  step,
                  np.array([(x * step + start_x, y * step + start_y) for x in range(amount_x) for y in
                   range(amount_y)]))
