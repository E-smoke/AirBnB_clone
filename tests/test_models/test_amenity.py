#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        obj = Amenity()
        self.assertEqual(obj.__class__.__name__, "Amenity")
