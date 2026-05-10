#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
It provides a specialized representation of a four-sided polygon.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a square, which is a specific type of rectangle.
    It ensures all sides are equal during initialization.
    """

    def __init__(self, size):
        """
        This method initializes a new Square instance.
        The size is validated as a positive integer before storage.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        This method calculates and returns the area of the square.
        It overrides the parent area method for specific square logic.
        """
        return self.__size ** 2
