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
