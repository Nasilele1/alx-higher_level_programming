#!/usr/bin/python3
"""Defines a python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary respresentation of a simple data structure."""
    return obj.__dict__
