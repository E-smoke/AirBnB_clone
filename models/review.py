#!/usr/bin/python3
import uuid
import copy
import datetime
from models import storage
from models.base_model import BaseModel

"""review class"""


class Review(BaseModel):
    """review class"""
    place_id = ""
    user_id = ""
    text = ""
