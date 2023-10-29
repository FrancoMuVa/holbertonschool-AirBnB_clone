#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def testInitialization(self):
        self.user = User()

        self.assertIsInstance(self.user, BaseModel)

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def testAssignment(self):
        self.user = User()
        self.user.email = "johnlee@gmail.com"
        self.assertEqual(self.user.email, "johnlee@gmail.com")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

        self.user.password = "12examPle;"
        self.assertEqual(self.user.email, "johnlee@gmail.com")
        self.assertEqual(self.user.password, "12examPle;")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

        self.user.first_name = "John"
        self.assertEqual(self.user.email, "johnlee@gmail.com")
        self.assertEqual(self.user.password, "12examPle;")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "")

        self.user.last_name = "Lee"
        self.assertEqual(self.user.email, "johnlee@gmail.com")
        self.assertEqual(self.user.password, "12examPle;")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Lee")

    def testToDict(self):
        self.user = User()
        self.user.email = "johnlee@gmail.com"
        self.user.password = "12examPle;"
        self.user.first_name = "John"
        self.user.last_name = "Lee"
        self.user_dict = self.user.to_dict()

        self.assertIn("email", self.user_dict)
        self.assertIn("password", self.user_dict)
        self.assertIn("last_name", self.user_dict)
        self.assertIn("first_name", self.user_dict)

        self.assertEqual(self.user_dict["email"], "johnlee@gmail.com")
        self.assertEqual(self.user_dict["password"], "12examPle;")
        self.assertEqual(self.user_dict["first_name"], "John")
        self.assertEqual(self.user_dict["last_name"], "Lee")
