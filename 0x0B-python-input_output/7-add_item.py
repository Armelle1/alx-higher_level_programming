#!/usr/bin/python3
''' this module save anf load object '''
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
liste = []
a = len(sys.argv) - 1
filename = "add_item.json"
liste = load_from_json_file(filename)
for i in range(a):
    # data = load_from_json_file(element)
    liste.append(sys.argv[i + 1])
save_to_json_file(liste, filename)
