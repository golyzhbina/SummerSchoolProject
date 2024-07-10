from dataclasses import dataclass

import numpy as np

from region.Region import Region


@dataclass
class CoherenceCube:
    cube: np.ndarray
    start_point_source: tuple
    amount_point: tuple
    step_on_net: int
    time_interval: tuple     # in milliseconds
    time_step: int  # in milliseconds
    depth: int
