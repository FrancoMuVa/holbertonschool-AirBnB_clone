#!/usr/bin/python3
import unittest
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):

    def testInitialization(self):
        self.review = Review()

        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def testAssignment(self):
        self.review = Review()
        self.place = Review()
        self.user = User()

        self.review.place_id = self.place.id
        self.review.user_id = self.user.id
        self.review.text = "The review"

        self.assertEqual(self.review.place_id, self.place.id)
        self.assertEqual(self.review.user_id, self.user.id)
        self.assertEqual(self.review.text, "The review")
