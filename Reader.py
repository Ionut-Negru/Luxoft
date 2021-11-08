# Reader.py
"""This file containts the functions used to read the json files"""
import json
from CloudCtx import CloudCtx


def read_json(file_name=""):
    result = []
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        for x in data['imdata']:
            entry = CloudCtx()
            entry.parse_json(x)
            result.append(entry)

    return result
