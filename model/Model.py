from dataclasses import dataclass
import numpy as np


@dataclass
class Model:
    step: int
    field: np.ndarray
    max_depth: float

