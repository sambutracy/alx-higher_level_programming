#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, filling with 0 if needed
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Sum the corresponding elements of the tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
