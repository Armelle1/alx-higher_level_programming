#!/usr/bin/python3
''' this module '''


def save_to_json_file(my_obj, filename):
    ''' this module'''
    with open(filename, 'w', encoding="utf-8") as f:
        import json
        json.dump(my_obj, f)
