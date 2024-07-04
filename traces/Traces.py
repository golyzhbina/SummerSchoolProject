from dataclasses import dataclass

import numpy as np


# all times in milliseconds
@dataclass
class Traces:
    sample_interval: int
    amount_samples: int
    length_of_trace: int
    traces: np.array
