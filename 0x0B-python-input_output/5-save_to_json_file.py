#!/usr/bin/python3
"""save obj to a file"""


import json


def save_to_json_file(my_obj, filename):
    """saving to JSON file"""
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(my_obj, file)
