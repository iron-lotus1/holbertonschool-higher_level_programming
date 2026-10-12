#!/usr/bin/env python3
"""Serialize and deserialize, using pickle module"""

import pickle

class CustomObject:
    """Represent a custom object with attributes"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError, TypeError, AttributeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if not isinstance(obj, cls):
                return None
            return obj
        except (OSError, pickle.PickleError, EOFError, TypeError, AttributeError, ImportError, ValueError):
            return None
