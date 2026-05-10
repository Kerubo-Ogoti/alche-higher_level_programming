#!/usr/bin/python3
"""
This module provides a function for general type checking.
It identifies if an object belongs to a class or any of its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of a specified class.
    It returns True if the object matches the class or its inherited types.
    Otherwise, the function returns False.
    """
    return isinstance(obj, a_class)
