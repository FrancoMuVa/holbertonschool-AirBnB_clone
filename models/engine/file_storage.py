#!/usr/bin/python3
"""

"""
import json


class FileStorage():
    """

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  """
        return self.__objects
    
    def new(self, obj):
        """  """
        key = f"{self.__clas__.__name__}.{obj.id}"
        self.__objects = {key: obj}
    
    def save(self):
        """  """
        with open(self.__file_path, "w", encoding="utf8") as f:
            dict_f = {}
            for key, item in self.__objects.items():
                f_dict[key] = item.to_dict()
            json.dumps(f_dict, f())

    def reload(self):
        """  """
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)

                for key, item in data.items():
                    self.__objects[key] = item
                return self.__objects
        except FileNotFoundError:
            pass