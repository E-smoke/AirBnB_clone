#!/usr/bin/python3
import unittest
from models.user import User
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        obj = User()
        self.assertEqual(obj.__class__.__name__, "User")
