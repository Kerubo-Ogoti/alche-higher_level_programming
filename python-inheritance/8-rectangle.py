#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
It focuses on the initialization and validation of rectangle dimensions.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """
        This method initializes a new Rectangle instance.
        It validates the dimensions before assigning them to private attributes.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
