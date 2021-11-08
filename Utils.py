# utils.py
"""This file contains utilitary functions for the project"""


def show_cloudCtx_data(data=[]):
    for x in data:
        print(x)
        print('*'*60)


def sort_by_last_modified_date(data=[]):
    return data.sort(key=lambda x: x.lastModified, reverse=True)


def sort_by_current_health(data=[]):
    return data.sort(key=lambda x: x.HealthInst.current_health, reverse=False)
