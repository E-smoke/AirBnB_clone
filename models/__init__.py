#!/bin/python3
"""instance of file storage"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
