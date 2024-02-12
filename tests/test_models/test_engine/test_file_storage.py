#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """test function"""
        obj = FileStorage()
        self.assertEqual(obj.__class__.__name__, "FileStorage")
