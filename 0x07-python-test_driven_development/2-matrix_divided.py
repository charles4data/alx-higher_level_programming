#!/usr/bin/python3

"""
Module for matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Divides a matrix by div

    args:
        matrix: matrix to be divided
        div: divisor

    return:
        matrix: matrix * div

    raises:
        TypeError: If matrix has non-integers or non-float elements
        TypeError: if div is not an integer or float
        TypeError: If matrix rows are of different sizes
        ZeroDivisionError: If div is 0

    """

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check if each row of the matrix has the same size
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
