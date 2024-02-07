#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """returning a dict"""
    return obj.__dict__
