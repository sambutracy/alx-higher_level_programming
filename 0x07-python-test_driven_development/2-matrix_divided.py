#!/usr/bin/python3
"""
Module providing a function for dividing all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Parameters:
    - matrix: a list of lists of integers or floats
    - div: a number (integer or float) to divide the elements of the matrix by

    Returns:
    - A new matrix with elements rounded to 2 decimal places.

    Raises:
    - TypeError: If matrix is not a list of lists of integers or floats,
                if each row of the matrix is not of the same size,
                or if div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix

