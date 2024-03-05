import unittest

from models.state import State


class TestCity(unittest.TestCase):
    """Test for class State"""

    def test_name(self):
        """Test class attributes named name"""
        obj = State()
        self.assertEqual(obj.name, "")
        obj.name = "Bitcoin"
        self.assertEqual(obj.name, "Bitcoin")


if __name__ == '__main__':
    unittest.main()