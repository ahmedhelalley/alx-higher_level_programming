#!/usr/bin/python3
"""reading from a file"""


def read_file(filename=""):
    """Function to read from a file"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
