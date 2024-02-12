import unittest
from models.engine.file_storage import FileStorage


class Test_BaseModel(unittest.TestCase):
    def test_init(self):
        obj = FileStorage()
        self.assertEqual(obj.__class__.__name__, "FileStorage")
