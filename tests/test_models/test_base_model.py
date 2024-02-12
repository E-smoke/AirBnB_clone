import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    def test_init(self):
        obj = BaseModel()
        self.assertEqual(obj.__class__.__name__, "BaseModel")
