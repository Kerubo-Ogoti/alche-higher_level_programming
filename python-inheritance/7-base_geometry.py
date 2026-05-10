#!/usr/bin/python3
"""
This module defines a base class for geometry-related objects.
It includes methods for area calculation and attribute validation.
"""


class BaseGeometry:
    """
    This class serves as a foundational structure for geometric shapes.
    It provides shared validation logic for all inheriting subclasses.
    """

    def area(self):
        """
        This method acts as a placeholder for area calculations.
        It raises an exception to ensure subclasses provide their own logic.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates that a given value is a positive integer.
        It checks both the data type and the mathematical value range.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
