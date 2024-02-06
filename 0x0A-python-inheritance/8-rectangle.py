#!/usr/bin/python3
'''Module Description for Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing the rectangle.'''
    def __init__(self, width, height):
        '''The Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
