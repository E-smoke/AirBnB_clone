#!/usr/bin/python3
import uuid
import copy
import datetime
from models import storage
from models.base_model import BaseModel

"""state module"""


class State(BaseModel):
    """state class"""
    name = ""
