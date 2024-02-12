#!/usr/bin/python3
import unittest
from models import storage
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        self.assertEqual(storage.__class__.__name__, "FileStorage")
