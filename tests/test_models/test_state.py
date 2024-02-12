#!/usr/bin/python3
import unittest
from models.state import State
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        obj = State()
        self.assertEqual(obj.__class__.__name__, "State")
