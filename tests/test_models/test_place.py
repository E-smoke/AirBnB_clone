#!/usr/bin/python3
import unittest
from models.place import Place
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        obj = Place()
        self.assertEqual(obj.__class__.__name__, "Place")
