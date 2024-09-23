import numpy as np
import matplotlib.pyplot as plt


def read_cube(filename):
    file = open(filename, "r")
    size = [int(num) for num in file.readline().split()]
    shape = (size[0], size[1], size[2])
    cube = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            arr = [float(num) for num in file.readline().split()]
            for k in range(shape[2]):
                cube[j][i][k] = arr[k]
    file.close()
    return cube


def find_max(cube: np.array, interval: tuple):
    m = np.unravel_index(np.argmax(cube[:, :, interval[0] : interval[1]], axis=None), (cube.shape[0], cube.shape[1], interval[1] - interval[0]))
    m = (m[0], m[1], m[2], cube[m[0]][m[1]][m[2] + interval[0]])
    print(m)


def get_graphic_detect_func(cube: np.ndarray, interval: tuple):
    cube = cube.reshape(cube.shape[0] * cube.shape[1], cube.shape[2])
    plt.plot(np.amax(cube[:, :, interval[0]:interval[1]], axis=0))
    plt.show()


def get_slice(cube: np.ndarray, t):
    plt.imshow(cube[:, :, t])
    plt.show()


def save_cube(cube, filename):
    np.save(filename, cube)
