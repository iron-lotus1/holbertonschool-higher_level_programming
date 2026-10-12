#!/usr/bin/env python3
"""Module for basic JSON serialization and deserialization."""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python object and save it to a JSON file."""
    with open(filename, "w", encoding="utf-8") as JFILE:
        json.dump(data, JFILE)
    

def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it into a Python object."""
    with open(filename, "r", encoding="utf-8") as JFILE:
        return json.load(JFILE)
