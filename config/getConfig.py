"""
a simple and easy loader to return the configs as a dict
"""
import json


def getSettings():
    """
    return configs
    >>> getSettings()
    {...}
    """
    with open('config/settings.json') as json_data_file:
        data = json.load(json_data_file)
        return data
