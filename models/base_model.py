#!/usr/bin/python3
import uuid
import copy
import datetime
from models import storage

storage.save()

"""BaseModel class module"""


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
            self.created_at = datetime.datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.datetime.fromisoformat(self.updated_at)
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
        key = self.__class__.__name__ + "." + self.id
        if key not in storage.all():
            storage.new(self)

    def __str__(self):
        """object value"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates self.update to current date and time"""
        self.updated_at = datetime.datetime.now()
        self.to_dict()
        storage.save()

    def to_dict(self):
        """returns a dictionary containg all key
        value pair of the attributes of the instance
        and also adds __class__ which is the name of
        the class of the object"""
        dictionary = copy.deepcopy(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        created_at = datetime.datetime.isoformat(self.created_at)
        updated_at = datetime.datetime.isoformat(self.updated_at)
        dictionary["created_at"] = created_at
        dictionary["updated_at"] = updated_at
        return dictionary

    def __str__(self):
        """str rep"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
