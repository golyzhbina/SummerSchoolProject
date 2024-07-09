from dataclasses import dataclass

import numpy as np

from region.Region import Region


@dataclass
class CoherenceCube:
    cube: np.ndarray
    region: Region
    interval: tuple     # in milliseconds
    interval_step: int  # in milliseconds
    depth: [int, float]
