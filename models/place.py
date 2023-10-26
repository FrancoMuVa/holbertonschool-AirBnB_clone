#!/usr/bin/python3
""" class Place """
from models.base_model import BaseModel


class Place(BaseModel):
    """ class that inherits from BaseModel """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
