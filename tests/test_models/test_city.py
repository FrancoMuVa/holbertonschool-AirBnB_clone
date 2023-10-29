#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
from models.state import State


class TestCity(unittest.TestCase):

    def testInitialization(self):
        self.city = City()

        self.assertIsInstance(self.city, BaseModel)

        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

        self.state = State()
        self.city.state_id = self.state.id
        self.state_id = self.state.id
        self.assertEqual(self.city.state_id, self.state_id)
        self.assertEqual(self.city.name, "")

        self.city.name = "Madrid"
        self.assertEqual(self.city.state_id, self.state_id)
        self.assertEqual(self.city.name, "Madrid")
