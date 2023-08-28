#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            count += 1
            print("{}".format(my_list[x]), end="")
        except IndexError:
            print("indexing error")
        print("")
        return count

