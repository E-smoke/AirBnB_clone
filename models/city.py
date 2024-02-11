#!/usr/bin/python3
import uuid
import copy
import datetime
from models import storage
from models.base_model import BaseModel

"""city module"""


class City(BaseModel):
    """city class"""
    name = ""
    state_id = ""
