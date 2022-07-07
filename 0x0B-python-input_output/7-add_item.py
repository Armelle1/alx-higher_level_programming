#!/usr/bin/python3
''' this module save anf load object '''
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
liste = []
for element in sys.argv:
    data = load_from_json_file(element)
    liste.append(data)

save_to_json_file(liste, "add_item.json")

