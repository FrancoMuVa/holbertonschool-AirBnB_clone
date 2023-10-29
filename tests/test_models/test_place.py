#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):

    def testInitializatoion(self):
        self.place = Place()

        self.assertIsInstance(self.place, BaseModel)

        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def tsetAssignment(self):
        self.place = Place()
        self.city = City()
        self.user = User()

        self.ids_amenity = []
        self.amenity1 = Amenity()
        self.ids_amenity.append(self.amenity1.id)

        self.amenity2 = Amenity()
        self.ids_amenity.append(self.amenity2.id)

        self.amenity3 = Amenity()
        self.ids_amenity.append(self.amenity3.id)

        self.place.city_id = self.city.id
        self.place.user_id = self.user.id
        self.place.name = "Name Place"
        self.place.description = "Description of place"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 24153.70986
        self.place.longitude = 67098.54213
        self.place.amenity_ids = self.ids_amenity

        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, self.city.id)
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, self.user.id)
        self.assertEqual(self.place.name, "Name Place")
        self.assertEqual(self.place.name, "Description of place")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, "Name Place")
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 24153.70986)
        self.assertEqual(self.place.longitude, 67098.54213)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.amenity_ids, self.ids_amenity)
