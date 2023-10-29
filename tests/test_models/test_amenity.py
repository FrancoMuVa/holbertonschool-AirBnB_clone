#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def testInitialization(self):
        self.amenity = Amenity()

        self.assertIsInstance(self.amenity, BaseModel)

        self.assertEqual(self.amenity.name, "")

        self.amenity.name = "Amenity"
        self.assertEqual(self.amenity.name, "Amenity")
