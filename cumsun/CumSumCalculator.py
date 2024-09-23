import numpy as np


class CumSumCalculator:
    @staticmethod
    def get_cumsum(cube: np.ndarray, kernel_size: int) -> np.array:
        cube = np.hstack([np.zeros((cube.shape[0], kernel_size)), cube])
        cube = np.cumsum(cube, axis=1)
        cube = cube[:, kernel_size:] - cube[:, :-kernel_size]

        for i in range(1, kernel_size):
            cube[:, i] /= (i+1)
        
        cube[:, kernel_size:] /= float(kernel_size)
        return cube
