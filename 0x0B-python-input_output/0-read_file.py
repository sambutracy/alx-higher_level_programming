#!/usr/bin/python3
"""Reads and prints the content of a text file"""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
