#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("0")
    else:
        total = sum(float(arg) for arg in sys.argv[1:])
        num = int(total)
        print("{}".format(num))
