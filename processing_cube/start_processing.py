from processing import read_cube, find_max, get_graphic_detect_func, get_slice, get_slices

filename = input()
cube, shape, start_time = read_cube(filename)

command = input()
while command != "stop":
    if command == "fm":
        print("enter interval")
        interval = tuple([int(v) for v in input().split()])
        find_max(cube, interval)
    elif command == "gg":
        print("enter x, y")
        x, y = [int(v) for v in input().split()]
        print("enter interval")
        interval = tuple([int(v) for v in input().split()])
        get_graphic_detect_func(cube, x, y, interval, start_time)
    elif command == "gsl":
        print("enter time")
        t = int(input())
        get_slice(cube, t)
    elif command == "gsls":
        print("enter interval")
        interval = tuple([int(v) for v in input().split()])
        get_slices(cube, interval)
    command = input()