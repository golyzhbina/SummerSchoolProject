from dataclasses import dataclass
import numpy as np


@dataclass
class Model:
    step: int
    field: np.ndarray
    max_depth: float


"""
model = Model("C:\\Users\\golub\\test2\\pythonProject1\\vel.docx",
              10,
              0,
              2219,
              0,
              1000)
print(model.field)
"""
