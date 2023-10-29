#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def testInitialization(self):
        self.state = State()

        self.assertIsInstance(self.state, BaseModel)

        self.assertEqual(self.state.name, "")

        self.state.name = "Montevideo"
        self.assertEqual(self.state.name, "Montevideo")
