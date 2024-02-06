#!/usr/bin/python3
"""from JSON string to object"""


import json


def from_json_string(my_str):
    """converting JSON str into pyObj"""
    return json.loads(my_str)
