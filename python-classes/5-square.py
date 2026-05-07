#!/usr/bin/python3
"""Module that defines a Square class with printing capabilities."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): The width/height of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character to stdout."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
