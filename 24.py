import random

def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
            return defualt
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
            except ValueError as err:
                pritn(err)

                rows = get_int("rows", 1, None)
                columns = get_int("columns", 1, None)
                minimum = get_int("minimum(or Enter for 0):", -100000, 0)


                default = 1000
                if default < minimum:
                    default = 2 * minimum
                maximum = get_int("maximum(or Enter for" + str(default) + "):", minimum, defualt)
