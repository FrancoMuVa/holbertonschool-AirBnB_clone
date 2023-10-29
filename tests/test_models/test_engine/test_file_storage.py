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

    def testSaveAndReload(self):
        user = User()
        user.first_name = "John"
        storage.new(user)
        storage.save()
        base = BaseModel()
        storage.reload()
        keyU = f"User.{user.id}"
        keyB = f"BaseModel.{base.id}"

        self.assertTrue(keyU in storage.all())
        user_reload = storage.all()[keyU]
        self.assertEqual(user.first_name, user_reload.first_name)
        self.assertTrue(keyB in storage.all())

        self.assertTrue(base.updated_at > user.updated_at)
