#!/usr/bin/python3

"""
 Create class called square
"""


class Square:
    """ This is a class with a private attribute"""
    def __init__(self, size=0):
        """
        Class method with a private attribute
        Raises:
                TypeError : if size is not int
                ValueError : if size is less than 0
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
