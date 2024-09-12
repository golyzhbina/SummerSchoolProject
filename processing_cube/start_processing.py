from processing_cube.processing import read_cube, find_max, get_graphic_detect_func, get_slice, save_cube

def start(cube, shape):
    print("enter command")
    command = input()
    while command != "stop":
        if command == "fm":
            print("enter interval")
            interval = tuple([int(v) for v in input().split()])
            find_max(cube, interval)
        elif command == "gg":
            print("enter interval")
            interval = tuple([int(v) for v in input().split()])
            get_graphic_detect_func(cube, interval)
        elif command == "gsl":
            print("enter time")
            t = int(input())
            get_slice(cube, t)
        elif command == "sc":
            print("input filename")
            filename = input()
            save_cube(cube, filename)

        print("enter command")
        command = input()