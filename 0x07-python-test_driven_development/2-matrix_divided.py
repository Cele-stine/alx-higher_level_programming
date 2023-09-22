#!/usr/bin/python3
"""Define the function."""


def matrix_divided(matrix, div):
    """This is a function that divides each element of a matrix.

    Args:
        matrix: The matrix to divide.
        div: the divisor.

    Raise:
        TypeError: if the rows of rhe matrix have diffrient sizes.
        ZeroDIvisionError: if the divisor is Zero
    """

    result = []
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
