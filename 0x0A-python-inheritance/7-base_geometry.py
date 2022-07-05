#!/usr/bin/python3

""" defines class BaseGeometry """


class BaseGeometry:
    """ Geometry class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not value.__class__ == int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
