import numpy as np
import matplotlib.pyplot as plt


def read_cube(filename):
    file = open(filename, "r")
    size = [int(num) for num in file.readline().split()]
    shape = (size[0], size[1], size[3] - size[2])
    cube = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            arr = [float(num) for num in file.readline().split()]
            for k in range(size[3] - size[2]):
                cube[i][j][k] = arr[k]
    file.close()
    return cube, shape, size[2]


def find_max(cube: np.array, interval: tuple):
    shape = cube.shape
    maxes = list()
    for i in range(shape[0]):
        for j in range(shape[1]):
            m = max(cube[i][j][interval[0]:interval[1]], key=lambda x: abs(x))
            for k in range(interval[0], interval[1]):
                if cube[i][j][k] == m:
                    maxes.append((i, j, k, m))
                    break
    print(maxes)
    m = max(maxes, key=lambda t: abs(t[0]))
    print(m)


def get_graphic_detect_func(cube: np.ndarray, y: int, x: int, interval: tuple, start_time: int):
    values = [abs(v) for v in cube[y][x][interval[0]:interval[1]]]
    plt.plot([start_time + interval[0] + i for i in range(len(values))], values)
    plt.show()


def get_slice(cube: np.ndarray, t):
    sl = np.ones((cube.shape[0], cube.shape[1]))
    for i in range(cube.shape[0]):
        for j in range(cube.shape[1]):
            sl[i][j] *= abs(cube[i][j][t])
    plt.contourf(sl)
    plt.show()


def get_slices(cube: np.ndarray, interval):
    slices = list()
    for t in range(interval[0], interval[1]):
        slices.append(get_slice(cube, t))
    i = interval[0]
    for sl in slices:
        save(sl, f"got_data/imgs/{i}.jpg")
        i += 1


def save(arr, name):
    plt.contourf(arr)
    plt.savefig(name)

