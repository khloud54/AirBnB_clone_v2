#!/usr/bin/python3
from models.base_model import BaseModel

class place(BaseModel):
    """Class representing a place"""

    def __init__(self, *args, **kwargs):
        """Initializes place"""
        super().__init__(*args, **kwargs)
        name = ""
        city_id = ""
        user_id = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
