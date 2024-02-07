#!/usr/bin/python3
"""function that returns a list of lists"""


def pascal_triangle(n):
    """generates the pascal's triangle of size n"""
    if n<= 0:
        return []

    triangle = []
    for i in range(n):
        row =[1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """print the triangle"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
