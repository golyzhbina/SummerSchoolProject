import numpy as np
import pandas as pd


class ExcelParser:

    def __init__(self, filename: str):
        file = pd.read_excel(filename, skiprows=2, index_col=[0, 1])
        self.values = np.hsplit(file.values, 2)

    def get_GaussKruger_coords(self) -> np.ndarray:
        return self.values[0]

    def get_WSG84_coords(self) -> np.ndarray:
        return self.values[1]
