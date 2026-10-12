#!/usr/bin/env python3
"""Convert CSV data to JSON"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert and save to json file"""
    try:
        data = []
        with open(csv_filename, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except (OSError, csv.Error, TypeError, ValueError):
        return False
