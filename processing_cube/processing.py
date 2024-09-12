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
    shape = cube.shape
    maxes = list()
    for i in range(shape[0]):
        for j in range(shape[1]):
            m = max(cube[i][j][interval[0]:interval[1]], key=lambda x: abs(x))
            for k in range(interval[0], interval[1]):
                if cube[i][j][k] == m:
                    maxes.append((i, j, k, m))
                    break
    m = max(maxes, key=lambda t: abs(t[3]))
    print(m)


def get_graphic_detect_func(cube: np.ndarray, interval: tuple):
    cube = cube.reshape(cube.shape[0] * cube.shape[1], cube.shape[2])
    plt.plot(np.amax(cube.T[interval[0]:interval[1]].T, axis=0))
    plt.show()


def get_slice(cube: np.ndarray, t):
    sl = np.ones((cube.shape[0], cube.shape[1]))
    for i in range(cube.shape[0]):
        for j in range(cube.shape[1]):
            sl[i][j] *= abs(cube[i][j][t])
    plt.contourf(sl)
    plt.show()


def save_cube(cube, filename):
    file = open(filename, "w")
    print(cube.shape[0], cube.shape[1], cube.shape[2], file=file, end="\n")
    for i in range(cube.shape[0]):
        for j in range(cube.shape[1]):
            print(*cube[i][j], sep=" ", end="\n", file=file)

    file.close()