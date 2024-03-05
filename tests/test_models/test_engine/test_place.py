import unittest

from models.place import Place


class TestUser(unittest.TestCase):
    """Test for class Place"""

    def test_city_id(self):
        """Test class attributes named city_id"""
        obj = Place()
        self.assertEqual(obj.city_id, "")
        obj.city_id = "bayamon"
        self.assertEqual(obj.city_id, "bayamon")

    def test_user_id(self):
        """Test class attributes named user_id"""
        obj = Place()
        self.assertEqual(obj.user_id, "")
        obj.user_id = "bayamon"
        self.assertEqual(obj.user_id, "bayamon")

    def test_name(self):
        """Test class attributes named name"""
        obj = Place()
        self.assertEqual(obj.name, "")
        obj.name = "bayamon"
        self.assertEqual(obj.name, "bayamon")

    def test_description(self):
        """Test class attributes named description"""
        obj = Place()
        self.assertEqual(obj.description, "")
        obj.description = "bayamon"
        self.assertEqual(obj.description, "bayamon")

    def test_number_rooms(self):
        """Test class attributes named number_rooms"""
        obj = Place()
        self.assertEqual(obj.number_rooms, 0)
        obj.number_rooms = 69
        self.assertEqual(obj.number_rooms, 69)

    def test_number_bathrooms(self):
        """Test class attributes named number_bathrooms"""
        obj = Place()
        self.assertEqual(obj.number_bathrooms, 0)
        obj.number_bathrooms = 69
        self.assertEqual(obj.number_bathrooms, 69)

    def test_max_guest(self):
        """Test class attributes named max_guest"""
        obj = Place()
        self.assertEqual(obj.max_guest, 0)
        obj.max_guest = 69
        self.assertEqual(obj.max_guest, 69)

    def test_price_by_night(self):
        """Test class attributes named price_by_night"""
        obj = Place()
        self.assertEqual(obj.price_by_night, 0)
        obj.price_by_night = 69
        self.assertEqual(obj.price_by_night, 69)

    def test_latitude(self):
        """Test class attributes named latitude"""
        obj = Place()
        self.assertEqual(obj.latitude, 0.0)
        obj.latitude = 69.69
        self.assertEqual(obj.latitude, 69.69)

    def test_longitude(self):
        """Test class attributes named longitude"""
        obj = Place()
        self.assertEqual(obj.longitude, 0.0)
        obj.longitude = 69.69
        self.assertEqual(obj.longitude, 69.69)

    def test_amenity_ids(self):
        """Test class attributes named amenity_ids"""
        obj = Place()
        self.assertEqual(obj.amenity_ids, [])
        obj.amenity_ids = ["bayamon"]
        self.assertEqual(obj.amenity_ids, ["bayamon"])


if __name__ == '__main__':
    unittest.main()