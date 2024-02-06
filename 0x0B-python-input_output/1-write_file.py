#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
