#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 0
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("{} arguments." .format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
    else:
        print("{} arguments:".format(num_args))
    for i in sys.argv[1:]:
        counter += 1
        print("{}: {}".format(counter, i))
