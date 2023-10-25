#!/usr/bin/python3
"""
    Class FileStorage
"""
import json


class FileStorage():
    """
        This class manages the storage of objects in a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Retrieve all stored objects. """
        return self.__objects

    def new(self, obj):
        """ Add a new object to the storage. """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects = {key: obj.to_dict()}

    def save(self):
        """ Save the objects to the JSON file. """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """ Reload objects from the JSON file. """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except Exception:
            pass
