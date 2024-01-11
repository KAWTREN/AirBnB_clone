#!/usr/bin/python3
""" serialization amd deserialization Instances """
import os
import json
import datetime


class FileStorage:
    """ Define class filestorage """
    __file_path = "files.json"
    __objects = {}

    def all(self):
        """ return dictionary """
        return (FileStorage.__objects)

    def new(self, obj):
        """ sets in objects new key /value """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            dict1 = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dict1, f)

    def reload(self):
        """  deserializes the JSON file to __objects """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
            dict1 = json.load(f)
            for key, value in dict1.items():
                class_name, obj_id = key.split('.')
                class_ = globals()[class_name]
                obj = class_(**value)
                FileStorage.__objects[key] = obj
