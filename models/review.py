#!/usr/bin/python3
""" class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
