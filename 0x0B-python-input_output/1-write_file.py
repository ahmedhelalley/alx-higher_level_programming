#!/usr/bin/python3
"""writing to a file and creating if doesn't exist"""


def write_file(filename="", text=""):
    """writing text to a file"""
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
