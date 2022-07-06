#!/usr/bin/python3
''' this class'''


def load_from_json_file(filename):
    ''' this module '''
    with open(filename, "r") as f:
        import json
        json.load(f)
