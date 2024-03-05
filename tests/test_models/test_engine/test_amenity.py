import unittest

from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """Test for class Amenity"""

    def test_name(self):
        """Test class attributes named name"""
        obj = Amenity()
        self.assertEqual(obj.name, "")
        obj.name = "yahdielo"
        self.assertEqual(obj.name, "yahdielo")


if __name__ == '__main__':
    unittest.main()