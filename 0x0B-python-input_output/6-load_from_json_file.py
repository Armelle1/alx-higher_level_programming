#!/usr/bin/python3
''' this class'''


def load_from_json_file(filename):
    ''' this module '''
    with open(filename, "r", encoding="utf-8") as f:
        import json
        return json.load(f)
