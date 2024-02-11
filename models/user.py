#!/usr/bin/python3
import uuid
import copy
import datetime
from models import storage
from models.base_model import BaseModel

"""first user class"""


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
