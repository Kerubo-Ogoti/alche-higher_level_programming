#!/usr/bin/python3
"""
This module provides a function to verify class inheritance.
It checks for relationships within the object hierarchy.
"""


def inherits_from(obj, a_class):
    """
    This function checks if an object is an instance of a subclass.
    It returns True if the object's class inherited from a_class.
    It returns False if the object is exactly an instance of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
