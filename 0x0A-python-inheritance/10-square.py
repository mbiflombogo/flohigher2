#!/usr/bin/python3

"""Write a class Square that inherits Rectangle"""


class Square(Rectangle):
    """Square extends Rectangle"""
    def __init__(self, size):
        """Initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self, size):
        """Finds area of a square"""
        return size ** 2
