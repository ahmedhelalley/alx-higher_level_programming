#!/usr/bin/python3
"""creating obj from JSON file"""


import json


def load_from_json_file(filename):
    """loading from JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
