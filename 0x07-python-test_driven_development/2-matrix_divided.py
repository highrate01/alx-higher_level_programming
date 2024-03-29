#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
    Args:
        Lists: A list of integers or floats.
        div: The divisor
    Raises:
        TypeError: if the matrix contains rows of different sizes
        TypeError: if the values are not int or float
        ZeroDivisionError: if the divisor is 0
    Returns:
        The result of the division in a matrix form
    """

    if (not isinstance(matrix, list) or matrix == [] or not
            all(isinstance(row, list) for row in matrix) or not
            all((isinstance(ele, int) or isinstance(ele, float))
                for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
