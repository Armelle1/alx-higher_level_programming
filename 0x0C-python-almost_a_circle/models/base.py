#!/usr/bin/python3
''' This Module defines Base class'''
import models


class Base:
    ''' this class defines Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        ''' static method that returns the JSON string '''
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        ''' method that writes the JSON string of list_objs to a file '''
        list_save = []
        if type(list_objs[0]) is models.rectangle.Rectangle:
            filename = "Rectangle.json"
        elif type(list_objs[0]) is models.square.Square:
            filename = "Square.json"
        if list_objs is not None:
            for rect in list_objs:
                list_save.append(rect.to_dictionary())
        with open(filename, 'w', encoding="utf-8") as f:
            f.writelines(Base.to_json_string(list_save))

    def from_json_string(json_string):
        ''' method that returns the list of the JSON string representation'''
        list_json = []
        if json_string is not None:
            import json
            for js in json.loads(json_string):
                list_json.append(js)
        return list_json
