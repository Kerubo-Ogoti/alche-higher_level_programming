#!/usr/bin/python3
"""
This module provides a function for precise type checking.
It helps determine if an object is an exact match for a class.
"""


def is_same_class(obj, a_class):
    """
    This function compares the type of an object to a specified class.
    It returns True only if the object is exactly an instance of that class.
    It returns False if the object is a subclass or a different type.
    """
    return type(obj) is a_class
