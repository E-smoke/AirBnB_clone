#!/usr/bin/python3
import unittest
from models.city import City
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        obj = City()
        self.assertEqual(obj.__class__.__name__, "City")
