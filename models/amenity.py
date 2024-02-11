#!/usr/bin/python3
import uuid
import copy
import datetime
from models import storage
from models.base_model import BaseModel

"""amenity class"""


class Amenity(BaseModel):
    """amenity class"""
    name = ""
