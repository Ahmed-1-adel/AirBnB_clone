#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a Amenity.
    
    Attributes:
        state_id (str): The state id.
        name (str): The name of the Amenity.
    """
    name = ""