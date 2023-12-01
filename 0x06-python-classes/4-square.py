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

    def area(self):
        """
        This is a public class method
        Returns: Area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ This method is the property getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ This method is the size setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
