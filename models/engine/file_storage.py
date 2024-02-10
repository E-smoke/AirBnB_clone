#!/bin/python3
"""file storage module"""
import json


class FileStorage:
    """file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns objects"""
        return self.__objects

    def new(self, obj):
        """adds an object to the objects"""
        obj_cls = obj.__class__.__name__
        key = obj_cls + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """dumps objects to a json file"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """fetches a json string from a json file"""
        try:
            with open(self.__file_path) as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
