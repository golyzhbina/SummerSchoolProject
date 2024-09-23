import numpy as np
import matplotlib.pyplot as plt


def read_cube(filename):
    return np.load(filename)


def find_max(cube: np.array, interval: tuple):
    m = np.unravel_index(np.argmax(cube[:, :, interval[0] : interval[1]], axis=None), (cube.shape[0], cube.shape[1], interval[1] - interval[0]))
    m = (m[0], m[1], m[2], cube[m[0]][m[1]][m[2] + interval[0]])
    print(m)


def get_graphic_detect_func(cube: np.ndarray, interval: tuple, filename):
    cube = cube.reshape(cube.shape[0] * cube.shape[1], cube.shape[2])
    np.save(filename, np.amax(cube[:, :, interval[0]:interval[1]], axis=0))
    


def get_slice(cube: np.ndarray, t, filename):
    plt.imshow(cube[:, :, t])
    plt.savefig(f"{filename}.png")


def save_cube(cube, filename):
    np.save(filename, cube)
