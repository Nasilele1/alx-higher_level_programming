#!/usr/bin/python3
"""Defines a student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialise a new student.

        Args:
            first_name (str): The first name of a student.
            last_name (str): The last name of a student.
            age (int): The age of a student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the student.

        If attrs is a list of strings, represent only those attributes
        included in the list

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
