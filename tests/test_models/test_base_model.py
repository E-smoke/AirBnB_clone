#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        obj = BaseModel()
        self.assertEqual(obj.__class__.__name__, "BaseModel")
