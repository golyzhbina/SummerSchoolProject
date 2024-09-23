from processing_for_cluster.processing import find_max, get_graphic_detect_func, get_slice, save_cube

def start(cube):
    print("enter command")
    command = input()
    while command != "stop":
        if command == "fm":
            interval = tuple([int(v) for v in input("enter interval\n").split()])
            find_max(cube, interval)
        elif command == "gg":
            interval = tuple([int(v) for v in input("enter interval\n").split()])
            filename = input("input filename\n")
            get_graphic_detect_func(cube, interval, filename)
        elif command == "gsl":
            t = int(input("enter time\n"))
            filename = input("input filename\n")
            get_slice(cube, t, filename)
        elif command == "sc":
            filename = input("input filename\n")
            save_cube(cube, filename)

        print("enter command")
        command = input()