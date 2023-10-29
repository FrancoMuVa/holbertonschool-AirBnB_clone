#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    base_model = BaseModel()

    def testInitialization(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def testSave(self):
        updated_at_1 = self.base_model.updated_at
        self.base_model.save()
        updated_at_2 = self.base_model.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def testStr(self):
        obj_str = str(self.base_model)
        self.assertEqual(obj_str, self.base_model.__str__())

    def testToDict(self):
        obj_dict = self.base_model.to_dict()

        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertIn("__class__", obj_dict)

        self.assertEqual(obj_dict["__class__"], "BaseModel")

        created_at = self.base_model.created_at.isoformat()
        self.assertEqual(obj_dict["created_at"], created_at)

        updated_at = self.base_model.updated_at.isoformat()
        self.assertEqual(obj_dict["updated_at"], updated_at)

        self.assertEqual(obj_dict["id"], self.base_model.id)
