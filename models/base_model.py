
#!/usr/bin/python3
"""BaseModel class Blueprint for all subclasses"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """This class represents the BaseModel of the
     AirBnBClone Project

     Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
    """

    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """When called, it returns the string representation
        of the Instance of the BaseModel"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """This method updatse the updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns the Dictionary of the instance of the BaseModel.
        It includes the key/value pair of __class__ representing the
        class name of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
