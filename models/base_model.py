#!/usr/bin/python3
"""Airbnb clone"""
import uuid
from datetime import datetime
from . import storage


class BaseModel():
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        """
            Initializes a new instance of the BaseModel class.

            Args:
                args.
                kwargs.
        """
        date = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, date)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns string representation of object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates attribute with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dict with all key/value of instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
