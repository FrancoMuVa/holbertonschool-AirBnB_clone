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
        self.__objects = {key: obj}

    def save(self):
        """ Save the objects to the JSON file. """
        with open(self.__file_path, "w") as f:
            dict_rep = {}
            for key, item in self.__objects.items():
                dict_rep[key] = item.to_dict()
            json.dump(dict_rep, f)

    def reload(self):
        """ Reload objects from the JSON file. """
        try:
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                for key, item in objects.items():
                    from models.base_model import BaseModel

                    k, v = key.split(".")
                    if k == "BaseModel":
                        self.new(BaseModel(**item))

        except Exception:
            pass
