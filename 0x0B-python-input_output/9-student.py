#!/usr/bin/python3
"""Class student"""


class Student():
    """student representation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieving student dict"""
        return self.__dict__
