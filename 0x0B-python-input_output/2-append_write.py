#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """append_write function"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
