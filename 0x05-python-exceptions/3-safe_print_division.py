#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = float(a) / float(b)
        return result
    except ZeroDivisionError:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
