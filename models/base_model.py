#!/usr/bin/python3
"""Documentation Module"""
import uuid
from datetime import datetime

import models


class BaseModel:
    """Class that defines all common
    attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for keys, value in kwargs.items():
                if keys in ['created_at', 'updated_at']:
                    self.__dict__[keys] = (datetime.strptime
                                            (value,  '%Y-%m-%dT%H:%M:%S.%f'))                                            
                elif keys != '__class__':
                    self.__dict__[keys] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the time of instance atribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict