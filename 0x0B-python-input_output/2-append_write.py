#!/usr/bin/python3
"""Appends a string at the end of a txt file and returns no of characters"""


def append_write(filename="", text=""):
    """Appends text file and returns no of characters added"""
    with open(filename, mode-"a", encoding="utf-8") as file:
        return file.write(text)
