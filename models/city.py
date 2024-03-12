#!/usr/bin/python3
"""the defenetion of the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """the Representation of a city class

    Attributes:
        state_id (str): state id number
        name (str): name of the city
    """

    state_id = ""
    name = ""
