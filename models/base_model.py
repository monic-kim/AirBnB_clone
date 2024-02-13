#!/usr/bin/python3
"""this is the basemodel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    '''all other classes inheri from this class'''

    def __init__(self, *args, **kwargs):
        """initializzes instance attributes

        Args:
            - *args:list of arguments
            - **kwargs: dict of key value arguments
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created _at":
                    self.__dict__["created_at"] = datetime.srptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] =
                    datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self)
    return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at'''
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys of __dict__'''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
