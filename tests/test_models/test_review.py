#!/usr/bin/python3
import unittest
from models.review import Review
"""test module"""


class Test_BaseModel(unittest.TestCase):
    """test class"""
    def test_init(self):
        """testfunction"""
        obj = Review()
        self.assertEqual(obj.__class__.__name__, "Review")
