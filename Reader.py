# Reader.py
"""This file containts the functions used to read the json files"""
import json
from CloudCtx import CloudCtx


def read_json(file_name=""):
    result = []
    try:
        data = open(file_name,)
        data = json.load(data)
    except FileNotFoundError:
        print("There is no file inside the project folder,try using the full path ")
    else:
        for x in data['imdata']:
            result.append(CloudCtx(x))
    return result
