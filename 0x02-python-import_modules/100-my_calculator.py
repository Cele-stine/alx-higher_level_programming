#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = float(sys.argv[1])
    operator = sys.argv[2]
    b = float(sys.argv[3])

    if operator == "+":
        print("{} + {} = {}".format(int(a),int(b), int(add(a, b))))
    elif operator == "-":
        print("{} - {} = {}".format(int(a), int(b), int(sub(a, b))))
    elif operator == "*":
        print("{} * {} = {}".format(int(a), int(b), int(mul(a, b))))
    elif operator == "/":
        print("{} / {} = {}".format(int(a), int(b), int(div(a, b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    sys.exit(0)
