#!/usr/bin/python3
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):

    def testFileExist(self):
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def testInstanceAll(self):
        self.assertIsInstance(storage.all(), dict)
        storage.reload()
        self.assertIsInstance(storage.all(), dict)

    def testNew(self):
        user = User()

        storage.new(user)
        key = f"User.{user.id}"
        self.assertTrue(key in storage.all())

    def testSave(self):
        user = User()
        user.first_name = "Pepe"
        storage.new(user)
        storage.save()
        key = f"User.{user.id}"
        self.assertTrue(key in storage.all())

        user2 = User()
        user2.first_name = "Robert"
        storage.new(user2)
        storage.save()
        key2 = f"User.{user2.id}"
        self.assertTrue(key2 in storage.all())
        self.assertTrue(key in storage.all())

    def testReload(self):
        base_model = BaseModel()
        key = f"BaseModel.{base_model.id}"
        storage.new(base_model)
        storage.save()

        del storage._FileStorage__objects[key]

        storage.reload()
        objects = storage.all()
        self.assertTrue(key in objects)
        reloaded_object = objects[key]
        self.assertEqual(reloaded_object.id, base_model.id)

    def testBaseModel(self):
        base_model = BaseModel()
        first_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(first_updated_at, base_model.updated_at)
